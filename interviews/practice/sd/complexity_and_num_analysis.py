"""
1. Matrix multiplication
    1.1 [E] You have three matrices: and you need to calculate the product. In what order would you perform your multiplication and why?
        Out: Let A is pq, B is qr, C is rs. We have 2 possibilities: 
            1. A * (B * C) = pq * (qr*rs). Cost is (qrs) + pqs scalar multiplications.
            2. (A * B) * C = (pq*qr) * rs. Cost is (pqr) + prs scalar multiplications.
            3. With p=10, q=100, r=5, s=50, we have (qrs) + pqs = 75000, (pqr) + prs = 7500.
    1.2 [M] Now you need to calculate the product of matrices. How would you determine the order in which to perform the multiplication?
        Out: Task is minimize the number of scalar multiplications using only matricies dimensions. Use matrix_chain_multiplication() algorithm.
2. [E] What are some of the causes for numerical instability in deep learning?
    Out:
        1. Exploding and vanishing gradients. The gradient is a product of derivatives across layers. Repeated multiplication by large or small values. 
        2. Weights that are too large or too small at initialization can immediately push activations. Pre-activation z = W @ x large, activation e.g. sigma(z) = 1 / (1 + exp(-z)). Large positive z -> undeflow to 0, large negative z -> underflow to infinity. Then taking derivative sigma'(z) = sigma(z) * (1 - sigma(z)): if z >> 0 = 0, if z << 0 = 0. Then gradient dL/dz_0 = dL/dz_L * Π_k sigma'(z_k) * W_k. Leads to 0, the gradient is lost.
        3. Poor activation functions. Sigmoid or tanh saturate large absolute inputs, leading to near-zero gradients. ReLU can produce large activations.
        4. Division by very small numbers in loss, or unstable loss functions (e.g. exp(x) (x=1000), or log(x) (x=0)).
        5. Large learning rate. Causes W_new = W_old - lr * dL_dW large, z_new = W_new @ x large, exp(z) in activation overflow into infinity.
        6. Limited floating-point precision. E.g. float16 range ~ [1e-5, 65504]. Values below = 0, above = inf. If gradients are small -> leads to vanishing gradients, and vice versa.
        7. No batch norm. Pre activation z_k = W_k @ h_{k-1} (h_{k-1} is the output of activation at layer k-1). Activation h_k = phi(z_k). h_k has some mean mu_k and variance sigma_k. Notice that z_k[i] = sum_j W_k[i, j] * h_{k-1}[j], then Var(z_k) ~ num_inputs * Var(W_k) * Var(h_{k-1}). If Var(W_k) * num_inputs > 1, then Var(z_k) > Var(h_{k-1}). Variance grows. If Var(W_k) * num_inputs < 1, variance shinks. This happens every layer. E.g. Var(h_0) = sigma_0**2, Var(h_1) ~ c * sigma_0**2, Var(h_L) ~ c^L * sigma_0**2. BatchNorm enforces mean ~ 0, variance ~ 1: h_k_norm = (h_k - mean(h_k)) / sqrt(var(h_k) + epsilon)
3. [E] In many machine learning techniques (e.g. batch norm), we often see a small term added to the calculation. What's the purpose of that term?
    Out: To prevent numerical instability:
        1. Division by zero, which produces NaNs and infinities.
        2. Division by very small numbers, which explodes.
        3. Compensate for finite-precision math, called catastrophic cancelation. Suppose x = [1000.001, 1000.002, 1000.003], mean ~ 1000.002, var(x) = mean((x - mean(x))**2). Then x - mean ~ [-0.001, 0.000, 0.001]. The result keeps only a few low-precision bits. Then (x - mean)**2 ~ [1e-6, 0, 1e-6]. When we finally compute mean, we can get 0, even though mathematically var > 0. Later, e.g. in BatchNorm, we compute (h - mean) / sqrt(var). Or in backprop you compute 1 / (var)^3/2. So a tiny numerical error in var becomes a massive explosion in gradients. var + epsilon is guaranteed to be safely away from zero. epsilon is a lower bound on how small variance is allowed to be, regardless of floating-point noise.
"""

def matrix_chain_multiplication(dimensions):
    """
    Time: O(n^3)
    Space: O(n^2)
    """
    num_matrices = len(dimensions) - 1

    # dp[i][j] = minimum cost to multiply Ai..Aj
    dp = [[0] * num_matrices for _ in range(num_matrices)]

    # split[i][j] = index k where optimal split occurs
    split = [[0] * num_matrices for _ in range(num_matrices)]

    # chain_length is the length of the matrix sub-chain
    for chain_length in range(2, num_matrices + 1):
        for i in range(num_matrices - chain_length + 1):
            j = i + chain_length - 1
            dp[i][j] = float("inf")

            for k in range(i, j):
                cost_left = dp[i][k]
                cost_right = dp[k + 1][j]
                cost_multiply = (
                    dimensions[i]
                    * dimensions[k + 1]
                    * dimensions[j + 1]
                )

                total_cost = cost_left + cost_right + cost_multiply

                if total_cost < dp[i][j]:
                    dp[i][j] = total_cost
                    split[i][j] = k

    return dp, split
