# Evaluating, Debugging & Diagnostics

**Diagnostic** is a test you run to gain insight into what is/isn't working with a learning algorithm, to gain guidance into improving its pefromance.

## Error Analysis

The error analysis process refers to manually looking through all misclassified cross validation examples and trying to gain insights into where the algorithm is going wrong, if it is possible. For example, imagine we have spam classification problem. Our model misclassified 100 examples, 21 of which are related to pharmaceutical, 18 to password stealing, 7 to unusual email routing, 3 to deliberate misspellings and 5 to where there is a spam embedded image. So, it is clear that we should figure out how to reduce error related to pharmaceutical and phishing emails.

If there is a large number of misclassified examples, take a random sample to perform error analysis on them (around 100-200).

After error analysis, you might want to add more data of the types where analysis has indicated it might help, such as pharma spam data.

## Evaluation

There is a simple technique which is used to evaluate your model through a test set. First, you take your dataset and split it into **train**, **validation** (optional) and **test** sets. You use *train* set to fit your model and then *test* set to evaluate it. Use any *metric* to evaluate your model. High & low cost and metric function values correspond to underfitting and overfitting of data by a model.

![image](https://user-images.githubusercontent.com/73081144/192172669-4e7e79b8-d0b6-4f83-85bd-3084d220211d.png)

*Fig. 1. Bias, variance and cost function value.*

To understand whether your algorithm's perfomance is poor or not, compare training/validation/test error to human/baseline model error perfomance.

![image](https://user-images.githubusercontent.com/73081144/192189396-2e8b875f-d7cb-4076-ad24-38a44f9af5e1.png)

*Fig. 2. Algorithm's perfomance compared to human/baseline model error perfomance.*

## Debugging

If a learning algorithm does not work well, there are some techniques that might increase the perfomance of a model:

- get more training data (fix *high variance*);
- simplify model architecture (fix *high variance*)
- try smaller sets of features (fix *high variance*);
- try getting additional features (fix *high bias*);
- try adding polynomial features (fix *high bias*):
  - $f_{\vec{w}, b}(\vec{x}) = w_1x + b$
  - $f_{\vec{w}, b}(\vec{x}) = w_1x + w_2x^2 + b$
  - $f_{\vec{w}, b}(\vec{x}) = w_1x + w_2x^2 + w_3x^3 + b$
  - ...
  - However, choosing polynomial degree based on the value of the test metric is faulty. This value is likely to be an optimistic estimate of generalization error (i.e. $J_{test}(w^{<5>}, b^{<5>}) < generalization \space error$), because extra parameter $d$ (degree of polynomial) was chosen using the test set. Use *validation* set instead of *test* set to see which polynomial degree to use. Then, $J_{test}$ will be a fair estimate of how good a model is at generalization.
- try decreasing (fix *high bias*) or increasing (fix *high variance*) regularization parameter $\lambda$;
