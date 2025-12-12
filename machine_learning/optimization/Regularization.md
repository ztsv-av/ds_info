# Regularization

Regularization is a form of regression, that constrains/ regularizes or shrinks the coefficient estimates (coefficients of parameters) towards zero. In other words, this technique discourages learning a more complex or flexible model, so as to avoid the risk of overfitting. For instance, if our model overfits because of the complexety of the generalization function, we might reduce the coefficients of higher order parameters by adding them with a high multiplier in a cost function:

![image](https://user-images.githubusercontent.com/73081144/187054399-8087e16a-92b3-467d-b111-0f6fd4f040b8.png)

*Fig. 1. Regularization in a cost function.*

The smaller the coefficients of parameters, the simpler the model, meaning the model less likely to overfit. However, we don't know with features to penalize in a cost function. So, we penalize every feature. This will usually result in a smoother, simpler function. You can penalize coefficients of features by adding this term to cost function:

$$\frac{\lambda}{2m}\sum_{j=1}^nw_j^2$$

, where
- $\lambda$ - regularization parameter, $\lambda > 0$

So, cost function will regularization will look like this:

$$J(w,b) = \frac{1}{2m}\sum_{i=1}^mL(f_{w,b}(x), y) + \frac{\lambda}{2m}\sum_{j=1}^nw_j^2$$

Some machine learning engineers will also **include** regularization term for parameter $b$:

$$J(w,b) = \frac{1}{2m}\sum_{i=1}^mL(f_{w,b}(x), y) + \frac{\lambda}{2m}\sum_{j=1}^nw_j^2 + \frac{\lambda}{2m}b^2$$

but this is makes **little difference** in pratice.

If $\lambda \approx 0$, then the model will overfit. If $\lambda$ is too large, then it will undefit.

![image](https://user-images.githubusercontent.com/73081144/187054701-a9fa68fb-43a1-4b5e-a3f5-8d5a6f8e029e.png)

*Fig. 2. Effects of regularization on cost function and choosing parameter $\lambda$.*

![image](https://user-images.githubusercontent.com/73081144/187055024-02789472-5d5c-44ce-b0e9-8f2e8afba726.png)

*Fig. 3. Regularized linear regression.*

![image](https://user-images.githubusercontent.com/73081144/187055108-9f856919-4abe-4330-9e79-831ed50e35a2.png)

*Fig. 4. Gradient descent with regularization.*

Choose regularization parameter $\lambda$ from $0$ up to $10$ (start from $0, 0.01, ...$ **doubling** the value every iteration) until you find the model that has the lowest cost value on validation set.

![image](https://user-images.githubusercontent.com/73081144/192173455-b859943c-0473-4a74-a5df-7bbb336f9526.png)

*Fig. 5. Choosing $\lambda$.*

![image](https://user-images.githubusercontent.com/73081144/192173689-a1f1a78f-9550-42e2-bdd6-1e21ebffdb2e.png)

*Fig. 6. How value of regularization parameter $\lambda$ corresponds to **bias** and **variance**.*
