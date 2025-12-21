# [E] Why Python slower than e.g. C++?

C++ is faster than Python because:

- Compiled -> no interpreter
- Static typing -> no runtime checks
- Lightweight primitive types:
  - Python int = a full object with reference count, type pointer, dynamic allocation, metadata
  - C++ int = just 4 bytes on the stack
- No garbage collector (destruction is deterministic)
- Highly optimized machine code
- Fast function calls:
  - Python has stack frame creation, argument parsing, python object creation
- True multithreading:
  - Python has GIL, which prevents multithreading
  - C++ has native support for atomics, locks, memory ordering, parallelism

# [E] You have three matrices: and you need to calculate the product. In what order would you perform your multiplication and why?

Let A is pq, B is qr, C is rs. We have 2 possibilities: 1. A _ (B _ C) = pq * (qr*rs). Cost is (qrs) + pqs scalar multiplications. 2. (A _ B) _ C = (pq*qr) * rs. Cost is (pqr) + prs scalar multiplications. 3. With p=10, q=100, r=5, s=50, we have (qrs) + pqs = 75000, (pqr) + prs = 7500.

# [M] Now you need to calculate the product of matrices. How would you determine the order in which to perform the multiplication?

Task is minimize the number of scalar multiplications using only matricies dimensions. Use matrix_chain_multiplication() algorithm.

# [E] What are some of the causes for numerical instability in deep learning?

1. Exploding and vanishing gradients. The gradient is a product of derivatives across layers. Repeated multiplication by large or small values.
2. Weights that are too large or too small at initialization can immediately push activations. Pre-activation z = W @ x large, activation e.g. sigma(z) = 1 / (1 + exp(-z)). Large positive z -> undeflow to 0, large negative z -> underflow to infinity. Then taking derivative sigma'(z) = sigma(z) _ (1 - sigma(z)): if z >> 0 = 0, if z << 0 = 0. Then gradient dL/dz_0 = dL/dz_L _ Π*k sigma'(z_k) * W\*k. Leads to 0, the gradient is lost.
3. Poor activation functions. Sigmoid or tanh saturate large absolute inputs, leading to near-zero gradients. ReLU can produce large activations.
4. Division by very small numbers in loss, or unstable loss functions (e.g. exp(x) (x=1000), or log(x) (x=0)).
5. Large learning rate. Causes W_new = W_old - lr * dL*dW large, z_new = W_new @ x large, exp(z) in activation overflow into infinity.
6. Limited floating-point precision. E.g. float16 range ~ [1e-5, 65504]. Values below = 0, above = inf. If gradients are small -> leads to vanishing gradients, and vice versa.
7. No batch norm. Pre activation $z_k = W_k * h_{k-1}$ ($h_{k-1}$ is the output of activation at layer $k-1$). Activation $h_k = \phi(z_k)$. $h_k$ has some mean $\mu_k$ and variance $\sigma_k$. Notice that $z_k[i] = \sum_j W_k[i, j] * h_{k-1}[j]$, then $\text{var}(z_k) \approx \text{num\_inputs} * \text{var}(W_k) * \text{var}(h_{k-1})$. If $\text{var}(W_k) * \text{num\_inputs} > 1$, then $\text{var}(z_k) > \text{var}(h_{k-1})$. Variance grows. If $\text{var}(W_k) * \text{num\_inputs} < 1$, variance shinks. This happens every layer. E.g. $\text{var}(h_0) = \sigma_0^2, \text{var}(h_1) \approx c * \sigma_0^2, \text{var}(h_L) ~ c^L * \sigma_0^2$. BatchNorm enforces $\text{mean} \approx 0, \text{var} \approx 1: h_{k_{norm}} = \frac{h_k - mean(h_k)}{\sqrt{\text{var}(h_k)} + epsilon}$

# [E] In many machine learning techniques (e.g. batch norm), we often see a small term added to the calculation. What's the purpose of that term?

1. To prevent numerical instability:
1. Division by zero, which produces NaNs and infinities.
1. Division by very small numbers, which explodes.
1. Compensate for finite-precision math, called catastrophic cancelation. Suppose $x = [1000.001, 1000.002, 1000.003], \text{mean} \approx 1000.002, \text{var}(x) = \text{mean}((x - \text{mean}(x))^2)$. Then $x - \text{mean} \approx [-0.001, 0.000, 0.001]$. The result keeps only a few low-precision bits. Then $(x - \text{mean})^2 \approx [1e-6, 0, 1e-6]$. When we finally compute mean, we can get 0, even though mathematically $\text{var} > 0$. Later, e.g. in BatchNorm, we compute $\frac{(h - \text{mean})}{\sqrt{\text{var}}}$. Or in backprop you compute $\frac{1}{\text{var}^\frac{3}{2}}$. So a tiny numerical error in var becomes a massive explosion in gradients. $\text{var} + \epsilon$ is guaranteed to be safely away from zero. $\epsilon$ is a lower bound on how small variance is allowed to be, regardless of floating-point noise.
