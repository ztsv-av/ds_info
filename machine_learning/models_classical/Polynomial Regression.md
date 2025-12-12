# Polynomial Regression

Polynomial regression is a form of linear regression known as a special case of multiple linear regression which estimates the relationship as an $n_{th}$ degree polynomial.

With polynomial regression, it is important to apply feature scailing to the data.

For example, if you predict price of a house based only on its size, you might convert this task from linear to polynomial regression by raising $x$ (size) to some power:

$y(x)=wx + b => y(x)=w_1x + w_2\sqrt{x} + w_3x^3 + b$

![image](https://user-images.githubusercontent.com/73081144/185279950-6ec28b88-a86a-4c74-bd9c-d211787bd29c.png)

*Fig. 1. Polynomial regression example.*
