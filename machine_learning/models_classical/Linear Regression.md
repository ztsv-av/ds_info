# Linear Regression

Linear regression is a supervised learning model, because it predicts numbers and trained on data paired with "right answers".

![image](https://user-images.githubusercontent.com/73081144/183325244-a41f5edc-7224-4dc1-879d-607a3985e192.png)

## Linear Regression with One Feature

*Fig.1. Example of a linear regression problem.*

$f_{w, b}(x) = wx + b$ - linear regression model, where w, b are parameters (coefficients/weights).

$\hat{y} = f_{w,b}(x)$ - prediction value.

So, linear regression task is to find $w,b$, where $\hat{y}^{(i)}$ is close to $y^{(i)}$ for all $(x^{(i)}, y^{(i)})$.

![image](https://user-images.githubusercontent.com/73081144/183329983-b987f367-da59-4df4-a65d-24bf1a6df09b.png)

*Fig.2. Linear regression with one variable, sometimes called **Univariate** linear regression.*

![image](https://user-images.githubusercontent.com/73081144/183331690-120d92d7-5bbc-4bd1-baa8-a123166e63cb.png)

*Fig. 3. Graph of $f(x)$ with different parameters values.*

![image](https://user-images.githubusercontent.com/73081144/183334657-b9bfd882-eb32-4a6a-98ab-dfc97d498b6a.png)

*Fig. 4. Goal of the linear regression model.*

## Cost Function

Cost function is the error, measurment of how a prediction distant from the truth value. The task is to minimize the cost function by variying parameters $w$ and $b$.

![image](https://user-images.githubusercontent.com/73081144/183335466-4a73fd89-be6d-41f4-aa59-27931ff57fef.png)

*Fig. 5. Linear regression function ($f(x) = wx$) values compared to MSE cost function values for variying values of $w$.*

![image](https://user-images.githubusercontent.com/73081144/183336601-0cf4fbae-bff5-4a64-802f-91d30dff24f4.png)

*Fig. 6. 3-D visualization of a cost function with specific parameter values.*

![image](https://user-images.githubusercontent.com/73081144/183336803-7500c4bc-b7d0-463c-829b-1451e16aa6c5.png)

*Fig. 7. 3-d visualization of a cost function with a pretty good parameter values that minimize the MSE cost function.*

## Gradient Descent for Linear Regression

![image](https://user-images.githubusercontent.com/73081144/183824683-7b2475ea-96b8-4ceb-8e68-3dd6b735ea16.png)

The squared error cost function has only 1 local minimum - global minimum, because of its 'bowl' shape (it is a convex function). As long as learning rate chosen appropriately, the cost function will always converge to the global minimum.

![image](https://user-images.githubusercontent.com/73081144/183825746-27927fd3-ecd4-4a7b-be01-ca0980703872.png)

*Fig. 8. Gradient descend in action.*


## Linear Regression with Multiple Feature (Multiple RegressionA)

The task is basically the same, but with multiple $x_j$, where $j=1,2,3...,n, n=$ number of features.

For example, for one feature we have:

$f_{w,b}(x)=wx+b$

With multple features we have:

$f_{w,b}(x)=wx_1 + wx_2 + ... + wx_n + b$, $n=$ number of features.

![image](https://user-images.githubusercontent.com/73081144/184567371-c84cda47-ea72-4bfb-afa8-881932cf57d9.png)

![image](https://user-images.githubusercontent.com/73081144/184567458-82eb342f-dd0b-492b-a3b7-55cc68a3bdd9.png)

*Fig. 9 and 10. Linear regression with multiple features example.*

You can think of multiple $w$ as weights for each feature. For example, as the size increases, the price of the house increases by 100 $ (1 unit - 1k $), as the number of bedrooms in a house increases, the price of the house increases too by 4k $, and so on, where b is the base price of a house.

You can write linear regression equation in the vector or matrix form:

![image](https://user-images.githubusercontent.com/73081144/184569037-361cfb3f-1aa0-4d97-9c3e-cbc1bb5d8bcc.png)

*Fig. 11. Multiple linear regression in vector form.*

### Gradient Descent for Multiple Linear Regression

The gradient descent functions look the same, but with slight differences: now, to update $w_j$ you will calculate partial derivative with respect to $x_j$. The formulas are in the figures below.

![image](https://user-images.githubusercontent.com/73081144/184570714-250d49b1-ad6d-41d8-b4d3-df6e16365b93.png)

![image](https://user-images.githubusercontent.com/73081144/184570880-0d7b893a-7bf5-4f30-ae4d-ff5b0230629b.png)

*Fig. 12 and 13. Gradient descent for multiple linear regression.*

## Linear Regression for Classification

You shouldn't use Linear Regression for classification purposes. One noisy example can shit the whole line making the function worse, because many examples will be misclassified. For classification you logistic regression.

For example, use linear regression when you need to estimate the weight of a cat based on its height, but do not use it if you need to decide whether an animal is a cat or not a cat.

![image](https://user-images.githubusercontent.com/73081144/185814014-ba55d986-8e19-4aa3-9f9c-ba9d6fb5a5dd.png)

*Fig. 14. Linear Regression in Classification.*
