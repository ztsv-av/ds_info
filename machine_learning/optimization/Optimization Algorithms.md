# Optimization Algorithms

Optimization algorithm is used to update parameters of a network.

## Gradient Descent

Gradient descent is used to minimize any function by taking partial derivatives of function's parameters. Our goal is to find values of parameters that minimize the function's value as much as possible. Cost function should decrease after every gradient descent iteration.

Goal outline:
- start with some $w,b$ (set $w=0, b=0$)
- keep changing $w,b$ to reduce $J(w,b)$
- until we settle at or near a minimum (may have >1 minimums).

![image](https://user-images.githubusercontent.com/73081144/183818928-4790b926-c665-4146-8f1c-bcef567272dd.png)

*Fig. 1. Gradient descent process. In the process, you look around and take a step to the direction of the steepest descent until you reach **local minima**.*

### Gradient Descent Algorithm

Repeat these two steps until convergence (until all parameters, for example $w,b$, no longer change much with each additional step):

1. Update parameter $w$ by taking the current value of $w$ and adjusting it a small amount:

    $w=w-\alpha \frac{\partial}{\partial w}J(w,b)$, where
      - $\alpha$ - learning rate, or measure of how big of a step you take down the gradient descent hill;
      - $\frac{\partial}{\partial w}J(w,b)$ - partial derivative term of the cost function $J$ to w. It tells you in which direction you want to the descent step. In combination with $\alpha$ it tells you the size and the direction of the step downhill.


2. Update parameter $b$ by taking the current value of $b$ and adjusting it a small amount:

    $b=b-\alpha \frac{\partial}{\partial b}J(w,b)$, where
      - $\alpha$ - learning rate, or measure of how big of a step you take down the gradient descent hill;
      - $\frac{\partial}{\partial b}J(w,b)$ - partial derivative term of the cost function $J$ to b. It tells you in which direction you want to the descent step. In combination with $\alpha$ it tells you the size and the direction of the step downhill.

Remember to update all parameters **simultaneously**.

![image](https://user-images.githubusercontent.com/73081144/183820365-96c8ab42-8a59-43b9-9d99-258b87f59d30.png)

*Fig. 2. Gradient descent intuition.*

### Gradient Descent Intuition

Repeat until convergence:

- $w=w-\alpha \frac{\partial}{\partial w}J(w,b)$

- $b=b-\alpha \frac{\partial}{\partial b}J(w,b)$

Intuition example where there is only 1 parameter $w$:

- Derivative is the slope of the tangent line to the function $J$ at the point $w_1$. When tangent line is pointing upwards, the slope is positive, meaning that the derivative is $>0$. If you take $w=w-\alpha \times$(positive number), you decrease the value of $w$, moving it to the left,so the value of $J(w)$ will also decrease, going to the local minima. If the slope is negative, you add the derivative value * learning rate to the current value of w, increasing it.

![image](https://user-images.githubusercontent.com/73081144/183821778-ee8d7d45-38e2-4253-83a4-9f7f6abaeb88.png)

*Fig. 3. Role of derivative in gradient descent.*

If you are already at local minimum, then gradient descent will not change the value of a parameter, because the slope will be equal to 0.

![image](https://user-images.githubusercontent.com/73081144/183822800-9ad3234b-9469-4ef9-b6fa-4818646fb0eb.png)

*Fig. 4. Gradient descent at local minimum.*

The size of the step (value of the partial derivative) will also decrease after each iteration, because, usually, the slope will decrease as we descent towards a local minima.

![image](https://user-images.githubusercontent.com/73081144/183823461-b5e5fad9-0971-4261-9866-4cbd2c5b3d0b.png)

*Fig. 5. Role of a learning rate in gradient descent.*

## Adaptive Moment Estimation (Adam)

The Adam algorithm is almost the same as gradient descent, but it doesn't use a single global learning rate $\alpha$. It uses a different learning rates for every single parameter of your model.

![image](https://user-images.githubusercontent.com/73081144/191166838-38ac4b62-5e2d-46ca-a022-423216a48a1f.png)

*Fig. 6. Individual learning rate for each trainable parameter in Adam optimization algorithm.*

The intuition behind the Adam algorithm is, if a parameter $w_j$, or $b$ seems to keep on moving in roughly the same direction. This is what we see on the first example in the *Fig. 7*. But if it seems to keep on moving in roughly the same direction, let's increase the learning rate for that parameter. Let's go faster in that direction. Conversely, if a parameter keeps oscillating back and forth, this is what we see in the second example in the *Fig. 7*. Then let's not have it keep on oscillating or bouncing back and forth. Let's reduce $\alpha_j$ for that parameter a little bit.

![image](https://user-images.githubusercontent.com/73081144/191167193-3ef8b385-6b69-4e93-9c65-32bb17eb497c.png)

*Fig. 7. Adam intuition.*

The method combines the advantages of two popular optimization methods:

1. **AdaGrad**: Known for its ability to handle **sparse gradients**, which means it adjusts the learning rate for each parameter individually, allowing for larger updates on infrequent features and smaller updates on frequently occurring features. This is particularly useful in scenarios where the data has sparse or infrequent features, such as natural language processing or recommendation systems.

2. **RMSProp**: Known for its ability to handle **non-stationary objectives**, meaning it adapts the learning rate over time to deal with changes in the optimization landscape. RMSProp does this by maintaining a moving average of the squared gradients, which allows it to adjust the learning rate dynamically, preventing overly aggressive updates when gradients vary rapidly and allowing for smoother convergence.

By combining these two methods, the optimizer can effectively manage both **sparse gradients** (like AdaGrad) and **non-stationary objectives** (like RMSProp), making it versatile and well-suited for a wide range of machine learning tasks.

### Algorithm

- $g_t^2$ indicates the element-wise square $g_t \cdot g_t$. 
- Good default settings for the tested machine learning problems are $\alpha = 0.001$, $\beta_1 = 0.9$, $\beta_2 = 0.999$, and $\epsilon = 10^{-8}$. 
- All operations on vectors are element-wise. 
- With $\beta_1^t$ and $\beta_2^t$, we denote $\beta_1$ and $\beta_2$ raised to the power $t$.

**Require**:  
- $\alpha$: Stepsize  
- $\beta_1, \beta_2 \in [0, 1)$: Exponential decay rates for the moment estimates  
- $f(\theta)$: Stochastic objective function with parameters - $\theta$  
- $\theta_0$: Initial parameter vector

---

**Initialize**:  
$m_0 \leftarrow 0$ (Initialize 1st moment vector)  
$v_0 \leftarrow 0$ (Initialize 2nd moment vector)  
$t \leftarrow 0$ (Initialize timestep)

---

**while** $\theta_t$ not converged **do**  
&nbsp;&nbsp;&nbsp;&nbsp;$t \leftarrow t + 1$  
&nbsp;&nbsp;&nbsp;&nbsp;$g_t \leftarrow \nabla_\theta f_t(\theta_{t-1})$ (Get gradients w.r.t. stochastic objective at timestep $t$)  
&nbsp;&nbsp;&nbsp;&nbsp;$m_t \leftarrow \beta_1 \cdot m_{t-1} + (1 - \beta_1) \cdot g_t$ (Update biased 1st moment estimate, exponential moving average)  
&nbsp;&nbsp;&nbsp;&nbsp;$v_t \leftarrow \beta_2 \cdot v_{t-1} + (1 - \beta_2) \cdot g_t^2$ (Update biased 2nd raw moment estimate, exponential moving average)  
&nbsp;&nbsp;&nbsp;&nbsp;$\hat{m}_t \leftarrow m_t / (1 - \beta_1^t)$ (Compute bias-corrected 1st moment estimate) **NOTE**  
&nbsp;&nbsp;&nbsp;&nbsp;$\hat{v}_t \leftarrow v_t / (1 - \beta_2^t)$ (Compute bias-corrected 2nd raw moment estimate) **NOTE**  
&nbsp;&nbsp;&nbsp;&nbsp;$\theta_t \leftarrow \theta_{t-1} - \alpha \cdot \hat{m}_t / (\sqrt{\hat{v}_t} + \epsilon)$ (Update parameters)

**end while**

---

**return** $\theta_t$ (Resulting parameters)

**NOTE** The purpose of bias correction in Adam is to adjust the estimates of the first and second moments (mean and variance of the gradients) because, early in training, these estimates are biased toward zero due to the initial values of the moments. Bias correction is used to reduce the variance of the gradients in Adam. The first and the second moment estimates are initialized with 0's, which makes them zero-biased. By applying bias correction, the algorithm ensures that the moment estimates are more accurate, particularly in the early stages of training when $t$ is small.

## AdamW (Decoupled Weight Decay)

AdamW (Adam with Weight Decay) improves upon the original Adam optimizer by addressing a subtle but impactful issue with how weight decay is handled in Adam.

- Decouples weight decay and learning rate when updating model parameters $\to$ simplifies the problem of hyperparameter tuning in SGD and improves Adam's perfomance.
- The decoupling in AdamW provides more consistent and reliable regularization. In Adam, the regularization strength is modulated by both the learning rate and weight decay, which can lead to unpredictable effects. By separating these, AdamW can control regularization more directly and effectively, preventing overfitting without unnecessarily penalizing gradient-based learning.
- In Adam, weight decay being mixed with the gradient update can cause weights to drift over time. This drift comes from the fact that L2 regularization in Adam is actually applied to the moving average of the gradients. This may cause the weights to move in undesired directions, especially in deep networks, negatively impacting the model's ability to generalize. AdamW prevents this drift by applying weight decay directly to the weights, ensuring the decay behaves as intended. This leads to better generalization, especially in large-scale tasks like deep learning.
- Due to the proper application of weight decay and more controlled learning rate dynamics, AdamW leads to better generalization. It helps models avoid overfitting on training data, especially when dealing with large models or small datasets.

Adam computes an adaptive learning rate based on estimates of first and second moments of the gradients. The weight decay in Adam is effectively treated as an additional component in the gradient calculation:

$$g_t=\nabla L(\theta_t)+\lambda \theta_t$$
- $g_t$ is the modified gradient,
- $\nabla L(\theta_t)$ is the gradient of the loss function w.r.t. to the paramters $\theta_t$
- $\lambda \theta_t$ is the L2 regularization term (weight decay applied as part of the gradient).

### Algorithm (with L2)

Given:
- Learning rate: $\alpha$
- Weight decay coefficient: $\lambda$
- Exponential decay rates for moment estimates: $\beta_1, \beta_2$
- Small constant for numerical stability: $\epsilon$

Initialize:
- Initial parameters: $\theta_0$
- First moment vector: $m_0 = 0$
- Second moment vector: $v_0 = 0$
- Time step: $t = 0$
- Schedule multiplier $\mu_{t=0}\in\mathbb{R}$

Repeat for each iteration:

1. Increment time step: $t = t + 1$

2. Compute the gradient of the loss function w.r.t. parameters: 
$$
   g_t = \nabla L(\theta_{t-1}) + \lambda\theta_{t-1}
$$

3. Update biased first moment estimate:
$$
   m_t = \beta_1 \cdot m_{t-1} + (1 - \beta_1) \cdot g_t
$$

4. Update biased second moment estimate:
$$
   v_t = \beta_2 \cdot v_{t-1} + (1 - \beta_2) \cdot g_t^2
$$

5. Compute bias-corrected first moment estimate:
$$
   \hat{m}_t = \frac{m_t}{1 - \beta_1^t}
$$

6. Compute bias-corrected second moment estimate:
$$
   \hat{v}_t = \frac{v_t}{1 - \beta_2^t}
$$

7. Set schedule multiplier:
$$
  \mu_t = \text{SetScheduleMultiplier}(t)
$$

8. Update parameters:
$$
   \theta_{t} = \theta_{t-1} - \mu_t\left(\alpha \cdot \frac{\hat{m}_t}{\sqrt{\hat{v}_t} + \epsilon}+\lambda\theta_{t-1}\right)
$$

Repeat until convergence.

## AdamWR (Decoupled Weight Decay + Warm Restarts)
