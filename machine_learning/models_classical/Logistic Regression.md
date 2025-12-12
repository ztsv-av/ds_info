# Logistic Regression

Logistic regression outputs a number between zero and one. It takes linear regression function and applies sigmoid function to it:

- $l_{w, b}(x) = wx + b$ - linear regression;

- $sig(x) = \frac{1}{1 + e^{-x}}$ - sigmoid function;

- $f_{w, b}(x) = \frac{1}{1 + e^{-(wx + b)}}$ - logistic regression.

Another way of writing logistic regression is:

- $P(y=1|x;w,b)$ - probability that $y$ equals 1 given variable $x$ and parameters $w,b$.

![image](https://user-images.githubusercontent.com/73081144/185814606-65a12dff-6b5c-4380-a87a-969d017b055e.png)

*Fig. 1. Logistic regression.*

Logistic regression outputs a **probability** that class is 1.

![image](https://user-images.githubusercontent.com/73081144/185814741-548c2f9b-4e5b-45d5-b4d1-5fc5bce0a6b5.png)

*Fig. 2. Interpretation of logistic regression output.*

The logistic regression outputs values between $0$ and $1$. So, you will need to put a threshold on your predictions.

![image](https://user-images.githubusercontent.com/73081144/185815095-136ab655-3a72-4300-9fd0-9e18262bb1ad.png)

*Fig. 3. Logistic regression prediction threshold.*

The *decision boundary* of a logistic regression can be **non-linear**, unlike in linear regression.


## Cost Function for Linear Regression

Squared error cost function is not suitable for logistic regression, because, if we plot the cost function to logistic regression function, it will many local minimums.

![image](https://user-images.githubusercontent.com/73081144/185816036-d9fac1d2-792d-4352-9f42-c2ae216741fb.png)

*Fig. 4. Squared error cost function and logistic regression.*

For logistic regression, use **logistic loss function**

$L(f_{w,b}(x^i), y^i) = \begin{cases} 
    -log(f_{w,b}(x^i)), & \text{if } y^i=1 \\ 
    -log(1 - f_{w,b}(x^i)), & \text{if } y^i=0 \end{cases}$

$L(f_{\mathbf{w},b}(\mathbf{x}^{(i)}), y^{(i)}) = (-y^{(i)} \log\left(f_{\mathbf{w},b}\left( \mathbf{x}^{(i)} \right) \right) - \left( 1 - y^{(i)}\right) \log \left( 1 - f_{\mathbf{w},b}\left( \mathbf{x}^{(i)} \right) \right)$

For the first case, when $y^i = 1$:

![image](https://user-images.githubusercontent.com/73081144/185816661-8dbc7c4e-4c84-4d77-bd08-0ad470861c8f.png)

*Fig. 5. Logistic loss function: case if y=1*

For the first case, when $y^i = 0$:

![image](https://user-images.githubusercontent.com/73081144/185817281-b8330103-e419-484d-ac78-6debeb946037.png)

*Fig. 6. Logistic loss function: case if y=0*

Logistic loss for logistic regression is **convex** => can reach global minimum.

## Gradient Descent

Gradient descent is as usual, you take partial derivatives with respect to parameters and simultaneously update them.

![image](https://user-images.githubusercontent.com/73081144/187048033-fe173d76-e5c3-4483-9163-f81488b8f49e.png)

*Fig. 7. Gradient descent for logistic regression.*

![image](https://user-images.githubusercontent.com/73081144/187048083-e178ed5a-f0d9-4776-b122-4622a094867a.png)

*Fig. 8. Gradient descent for linear and logistic regression comparison and concepts.*
