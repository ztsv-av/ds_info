# Overfitting & Undefitting

**Undefitting** - a model does not fit the training data very well. There is a trend in data that the algorithm is unable to capture. Another term is - the algorithm has **high bias**. This means that algorithm thinks that the function is, for example, linear, where in reality it looks like a log-function. When underfitting, train, validation and test costs are high. If a learning algorithm suffers from high bias, getting more training data will not (by itself) help much.


**Overfitting** - overfitting happens when a model fits data too well, meaning that it might not generalize to examples that it hasn't seen before. Another term is that an algorithm has **high variance**. The algorithm is trying very-very hard to fit every training example, which is bad for generalization. When overfitting, train cost is low, whereas validation/test cost is high.

The goal of machine learning is to find a model that neither overfits or underfits / a model has nor high bias nor high variance.

![image](https://user-images.githubusercontent.com/73081144/187054067-bd39325c-56c6-419b-bef0-86e680dd43e4.png)

*Fig. 1. Underfitting, generalization and overfitting. Regression example.*

![image](https://user-images.githubusercontent.com/73081144/187054111-fec7a951-6262-46a8-8eef-c6f320c53f25.png)

*Fig. 2. Underfitting, generalization and overfitting. Classification example.*

![image](https://user-images.githubusercontent.com/73081144/192172593-c8ed06fb-c29d-4ca4-b266-7b6aaeeff755.png)

*Fig. 3. Understanding bias and variance with polynomial.*

To understand whether your algorithm's overfits or/and underfits, compare training/validation/test error to human/baseline model error perfomance.

*Note: more training examples, higher overall training error, but lower cross validation error.*

![image](https://user-images.githubusercontent.com/73081144/192189396-2e8b875f-d7cb-4076-ad24-38a44f9af5e1.png)

*Fig. 2. Algorithm's perfomance compared to human/baseline model error perfomance.*

## Addressing Underfitting

- use bigger network;
- try getting additional features (fix *high bias*);
- try adding polynomial features (fix *high bias*):
  - $f_{\vec{w}, b}(\vec{x}) = w_1x + b$
  - $f_{\vec{w}, b}(\vec{x}) = w_1x + w_2x^2 + b$
  - $f_{\vec{w}, b}(\vec{x}) = w_1x + w_2x^2 + w_3x^3 + b$
  - ...
  - However, choosing polynomial degree based on the value of the test metric is faulty. This value is likely to be an optimistic estimate of generalization error (i.e. $J_{test}(w^{<5>}, b^{<5>}) < generalization \space error$), because extra parameter $d$ (degree of polynomial) was chosen using the test set. Use *validation* set instead of *test* set to see which polynomial degree to use. Then, $J_{test}$ will be a fair estimate of how good a model is at generalization.
- try decreasing (fix *high bias*) regularization parameter $\lambda$;

## Addressing Overfitting

- collect more data;
- see if you can use fewer/more features; *a lot of features + insufficient data = overfit*;
- reduce size of parameters - use regularization.

*Note: a **large** neural network will ususally do as well or **better** than a **smaller** one so long as **regularization** is chosen appropriately, but bigger network will slow down your training process.*
