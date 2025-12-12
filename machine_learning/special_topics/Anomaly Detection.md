# Anomaly Detection

Anomaly detection is identification of rare items, events or observations which deviate significantly frEom the majority of the data and do not conform to a well defined notion of normal behaviour. It is primarly unsupervised learning algorithm.

The most common way to carry out anomaly detection is to use **density estimation**. With density estimation, you build a model for the **probability of x**. In other words, the learning algorithm will try to figure out what are the values of the data features that have high probability and what are the values that are less likely or have a lower chance or lower probability of being seen in the data set. Given test example, you would compute the probability of this example. If the probability of test example is less than some small threshold, we will raise a flag to say that this could be an anomaly.

![image](https://user-images.githubusercontent.com/73081144/196326307-1c193180-8de1-45bc-81bb-976bd4794abc.png)

*Fig. 1. Density estimation.*

Besides density estimation, we will use **Gaussian/normal/bell-shaped** distribution. Probability of number $x$ is determined by a Gaussian with mean $\mu$ and variance $\sigma^2$. If we had an infinite number of examples, we would end up essentially with a bell-shaped curve centered at $\mu$ and determined by parameter $\sigma$.

Probability of a number $x$ with **Univariate Gaussian** distribution:

$$p(x) = \frac{1}{\sqrt{2\pi}\sigma} exp^{-\frac{(x-\mu)^2}{2\sigma^2}}$$

, where

- $\mu = \frac{1}{M}\sum^m_{i=1}x^{(i)}$,
- $\sigma^2=\frac{1}{M}\sum^m_{i=1}(x^{(i)} - \mu)^2$

These are *maximum likelihood estimations for $\mu$ and $\sigma$*. Sometimes people would use $\frac{1}{M - 1}$ instead of $\frac{1}{M}$.

Probability of a number $x$ with **Multivariate Gaussian** distribution:

$$p(x) = (\frac{1}{2\pi})^{\frac{p}{2}} |\sum_{\sigma}|^{-\frac{1}{2}} exp^{(-\frac{1}{2}(x-\mu)^T\sum_{\sigma}^{-1}(x-\mu))}$$

, where

- $p$ - number of features,
- $|\sum_{\sigma}|$ - determinant of the variance-covariance matrix $\sum_{\sigma}$,
- $\sum_{\sigma}^{-1}$ - inverse of the variance-covariance matrix $\sum_{\sigma}$

The lower the variance, the higher and thinner the curve. The higher the variance, the wider the distribution.

![image](https://user-images.githubusercontent.com/73081144/196328299-e916738d-d8a4-47c7-802b-806ea6f2386f.png)

*Fig. 2. Gaussian distribution.*

Even if one of the features of $x$ is very large or very low compared to feature values of other examples, then still $p(x)$ would be very small, indicating an anomaly (e.g. features probabilities multipled together $0.9 * 0.8 * 0.9 * 0.1 = 0.0648$)

*Remember: the choice of features is very imporant in anomaly detection.*

## Anomaly Detection Algorithm

- Training set: {$\vec{x}^{(1)}, \vec{x}^{(2)}, ..., \vec{x}^{(m)}$}.
- Each example $\vec{x}^{(i)}$ has $n$ features.
- $\vec{x} = [x_1, x_2, ..., x_n]$

**Model**:

$p(\vec{x}) = p(x_1; \mu_1, \sigma_1^2) * p(x_2; \mu_2, \sigma_2^2) * ... * p(x_n; \mu_n, \sigma_n^2)=\prod^n_{j=1}p(x_j;\mu_j,\sigma_j^2)$

*Note: features $x^i$ should be statistically **independent**. However, it turns out, the algorithm works fine even if features are somewhat dependent.*

**Algorithm**:

1. Choose $n$ features $x_i$ that might be indicative of anomalous examples.
2. Fit parameters $\mu_1, \sigma_1^2, ..., \mu_n, \sigma_n^2$:
    - $\mu = \frac{1}{M}\sum^m_{i=1}x^{(i)}_j$,
   - $\sigma^2=\frac{1}{M}\sum^m_{i=1}(x^{(i)}_j - \mu_j)^2$
3. Given new example $x$, compute $p(x)$:
   - $\prod^n_{j=1}p(x_j;\mu_j,\sigma_j^2) = \prod^n_{j=1} \frac{1}{\sqrt{2\pi}\sigma_j} exp^{-\frac{(x_j-\mu_j)^2}{2\sigma_j^2}}$
4. Flag as anomaly if $p(x) < \epsilon$.

## Developing and Evaluating Anomaly Detection Algorithm

- Use cross validation and test sets, which include a few anomalous examples (assume dataset is labeled). For example, imagine we have 10000 good examples and 20 anomalies. Then, use 6000 good examples for training set, 2000 good 10 bad for CV and 2000 good 10 bad for test sets. Use CV set to see how many anomalous examples your model is identifying and tune $\epsilon$ and features $x_j$ accordingly. Alternatively, don't use test set at all (CV 4000 good 20 bad). Use this technique if you have very few labeled anomalous examples, because there is a higher risk of overfitting without test set evaluation.
- Possible evaliation metrics are: precision/recall, $F_1$-score, true positive/false positive/true negative/false negative (same metrics that are used for **skewed datasets**).
- If $p(x)$ is comparable for normal and anomalous examples, try to find a new feature that distinguishes anomalies from normal examples.

## What Features to Use

- Use Gaussian features. If feature distribution is not Gaussian, transform it in order to look more Gaussia. For example, take $log(x)$ and see new distribution. If new distribution turns out to be normal, replace old feature with it ($x_1 <= \log(x_1), x_2 <= \log(x_2 + c), x_3 <= x_3^{1/2}, x_4 <= x_4^{1/3}$, etc.):
```
plt.hist(x, bins=50)
# =>
plt.hist(x**0.4, bins=50)
# or
plt.hist(np.log(x+1), bins=50)
```
- Create new features that distinguish anomalies from normal examples.

    ![image](https://user-images.githubusercontent.com/73081144/196335767-a529dd81-23be-4596-8397-02145ccb0f0a.png)

    *Fig. 3. Creating new features.*

## Unsupervised vs. Supervised Anomaly Detection Algorithms

| Unsupervised | Supervised |
| ------ | ----------- |
| Very small number of positive ($y=1$) (anomalous) examples; Large number of negative ($y=0$) examples | Large number of positive and negative examples. |
| Many different "types" of anomalies. It is hard for any algorithm to learn from positive examples what the anomalies may look like; future anomalies may look nothing like any of the anomalous examples we have seen so far (e.g. **fraud, manufacturing (unknown, unseen defects), monitoring machines in a data center**). | If it is possible to learn all anomalies from small, enough positive examples that we have in the data; future positive examples likely to be similar to ones in training set (e.g. **spam, manufacturing (previously seen defects), weather prediciton, diseases classification**).  |

## Anomaly Detection Applications

- fraud detection (e.g. find fake accounts or identify financial fraud):
    - $x^{(i)} =$ features of user $i$'s activities (how often user logs in, how many web pages visited, transations, posts, typing speed, etc.);
    - model $p(x)$ from data;
    - identify unusual users by checking which have $p(x) < \epsilon$.
- manufacturing (airplane engine, circuit board, smartphone, monitoring computers in data centers, etc.):
  - $x^{(i)} =$ features of product $i$, such as:
    - $x_1=$ memory use;
    - $x_2=$ number of disk accesses/sec.;
    - $x_3=$ CPU load;
    - $x_4=$ network traffic.
