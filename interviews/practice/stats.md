# Theory

## Conditional Probability

Let $(\Omega, F, P)$ be a probability space, and $B$ an event of non-zero measure.
Then for any event $A$, we call the quantity:
$$P(A|B) = \frac{P(A \cap B)}{P(B)}$$
It indicates the probability of an event $A$ occurring knowing that event $B$ has occurred.

$$(\Omega, F, P) \rightarrow (B, \mathcal{F}_B, P(\cdot | B))$$

$$\mathcal{F}_B = \{A \cap B \mid A \in F\}$$

### Complete System of Events

A family $\{B_1, \ldots, B_n\}$ is said to be a complete system of events if:

- $\forall i \in \{1, \ldots, n\}, P(B_i) \neq 0$ ($B_i \not ={\empty}$)

- $\forall i, j \in \{1, \ldots, n\}, P(B_i \cap B_j) = 0$ ($B_i \cap B_j = \empty$)

- $P\left(\bigcup_{i=1}^n B_i\right) = 1$ or equivalently $\sum_{i=1}^n P(B_i) = 1$ ($=> \cup B_i = \Omega$)

### Law of Total Probability (LTP)

Let $\{B_1, \ldots, B_n\}$ be a complete system of events, and $A$ be any event. Then:
$$P(A) = \sum_{i=1}^{n} P(B_i)P(A|B_i)$$

Example:\
We have 2 classes: $A$ and $B$. We are interested in probability of a students passing.\
$P(Pass|A) = 0.8;P(Pass|B)=0.6;P(A)=0.6$\
Thus, by LTP we have:\
$P(Pass)=P(A)P(Pass|A)+P(\overline{A})P(Pass|\overline{A})=P(A)P(Pass|A)+(1-P(A))P(Pass|B)=0.6*0.8+(1-0.6)0.6=0.72$

### Bayes' Formula

Let $A$ and $B$ be two events of non-zero probability. Then we have the identity:
$$P(A|B) = \frac{P(A)P(B|A)}{P(B)}$$

If the family $\{A_1, \ldots, A_n\}$ is a complete system of events, then for $1 \leq i \leq n$ we have:
$$P(A_i|B) = \frac{P(A_i)P(B|A_i)}{\sum_{i=1}^{n} P(A_i)P(B|A_i)}$$

Example:\
$P(Disease)=P(D)$ - probabiltiy that randomly selected person is sick.\
$P(P|D)$ - probablity of positive testing given sick person.\
$P(P|ND)$ - probability of positive testing given healthy person.\
We have $(D, ND)$ - compelete system of events. Thus:\
$P(D|P)=\frac{P(D)P(P|D)}{P(D)P(P|D) + P(ND)P(P|ND)}=\frac{P(D)P(P|D)}{P(D)P(P|D) + (1 -P(D))P(P|ND)}$

### Independence

$$P(A|B) = P(A)$$

$$P(A\cap B)=P(A)P(B), A \perp B$$

$$\mathcal{F}_1 \perp \mathcal{F}_2 \text{ if }\forall A \in \mathcal{F}_1, \forall B \in \mathcal{F}_2: P(A \cap B) = P(A)P(B)$$

## Counting

### Permutation

A set $\Omega$ is not ordered, there is no repetition:\
$\{a,b,c\} = \{b,c,a\} = \{a,c,b\} = \{a,b,c,b,c,a\}=...$

A permutation is a way to order the elements of $\Omega$. Alternatively, it is a bijetion from $\Omega$ to $\{1,2,3,..., n\}$ where $n = card(\Omega)$

If $\Omega$ has $n$ elements, then there are $n!$ number of permutations of $\Omega$.

$(w_1, w_2, w_3,..., w_n), n$ possible ways to choose $w_1$, $n-1$ possible ways to choose $w_2$, ..., $1$ possible way to choose $w_n$ = $n!$

*Question*: how many anagrams of the word MISSISSIPPI ? $\frac{11!}{4!4!2!}$

### Arrangement

An arrangement of $k$ elements from $n$ elements of a set $\Omega$ is an ordered sequence of $k$ distinct elements of $\Omega$. In arrangement, the order of selection matters. There are

$$A^k_n = n(n-1)(n-2)...(n-k + 1) = \frac{n!}{(n-k)!}$$

ways to arrange $k$ elements among $n$ elements.

### Combination

A combination of $k$ elements from $n$ elements of $\Omega$ is a subset of $\Omega$ with $k$ elements. In combination, the order does not matter ($\{1,2\} = \{2,1\}$).

$$C(n,k) = \frac{n!}{k!(n-k)!}$$

Proof:\
Given a combination of $k$ elements, we can form exactly $k!$ distinct arrangements by permuting the $k$ elements chosen. This gives the equality:

$A^k_n = \frac{n!}{(n-k)!}$

$k!\binom{n}{k} = A^n_k = \frac{n!}{k!(n-k)!}$

Example:\
$\Omega = \{ 1,2,3\}$\
$k=2, C(n,k)=\{\{1,2\},\{1,3\},\{2,3\}\}$ - the number of combinations of $k$ elements among a set of $n$ elements ($C(n,k)$ is called "$n$" choose "$k$").

## RVs

A random variable models the different values that the outcome of a random experiment can take.

- The roll of the dice. Consider the random variable $X : \Omega \rightarrow \{1, 2, 3, 4, 5, 6\}$ the application to which a given configuration associates the value of the dice.

For coin game, we have $X$ mapping: 

$$X: \Omega \to \{"Head", "Tail"\}, \omega \to x(\omega)$$

We have to ensure that $\{\omega \in \Omega: x(\omega) = "Tail"\}$ (*Notation: $\{\omega \in \Omega: x(\omega) = "Tail"\} = \{X = "Tail"\}$*) is an event, i.e. an element of the $\sigma$-algebra $\mathcal{F}$. Indeed, the proposition "the probability that the coin lands on tails is $1/2$" is written mathematically:

$$\mathbb{P}(X = "Tails") = 1/2$$

## Distributions

A probability distribution describes how probabilities are distributed over the values of the random variable.

### Distribution of Discrete Random Variable

Let $X$ be a discrete random variable with values in a countable space $E$. The distribution of $X$ is entirely characterized by the quantities for $e \in E$ ($X$ is a collection of quantities $\mathbb{P}(X=e)$):

$$P(X = e)$$

### Distribution of Real Random Variable

Let $X$ be a real random variable. The distribution of $X$ is entirely characterized by the quantities for $x \in \mathbb{R}$:

$$P(X \le x)$$

### Cumulative Distribution Function (CDF)

Let $X$ be a real random variable. The function $F$ is called the cumulative distribution function of the variable $X$:

$$F_X : \mathbb{R} \rightarrow [0, 1], x \mapsto P(X \leq x)$$

For $a<b$ and if $F$ does not have atoms:

$P(X\in[a,b])=P(X=a)_{=0 \text{ (no atoms)}}+P(X\in(a,b])=P(X\in(a,b])=P((X\le b) \cap(X>a))=P(X\le b)-P(X\le a)=F_X(b)-F_X(a)$

### Quantile Function

Let $F$ be a function verifying the three properties of CDF. We define the quantile function $F^{-1}: [0, 1] \rightarrow \mathbb{R}$ by
$$F^{-1}(u) = \inf \{x \in \mathbb{R} \,|\, F(x) \geq u\}$$
(in general: $F(x) = y \iff x=F^{-1}(y)$)

Let $U$ be a uniform distribution on $[0, 1]$. The quantile function $F^{-1}$ verifies the following properties:
- If $F$ is continuous and increasing, then $F^{-1}$ is the reciprocal bijection of $F$.
- The random variable $X = F^{-1}(U)$ has the cumulative distribution function $F$.

### Probability Density Function (PDF)

Let $X$ be a real random variable with a cumulative distribution function $F_X$. The random variable $X$ is said to have a density if there exists an integrable function $f_X$ such that

$$F_X(x) = P(X \leq x) = \int_{-\infty}^{x} f_X(t) \, dt$$

The function $F_X$ is a primitive of the function $f_X$. We deduce that $F_X$ is continuous, so $X$ is atom-free.

### CDF and PDF

Let $X$ be a real random variable. If its cumulative distribution function $F_X$ is continuous and piecewise derivable, then $X$ is a random variable with probability density $f$ and:

$$f_X = (F_X)' = \frac{d}{dx} F_X$$

### Expectation

Let $X$ and $Y$ be two integrable random variables defined on the same probability space $(\Omega, \mathcal{F}, \mathbb{P})$, and $\lambda$ a real number. Then,

- **Linearity** : For $\lambda \in \mathbb{R}$, we have

$$E[\lambda X + Y] = \lambda E[X] + E[Y]$$

- **Monotonicity** : If, for almost all $\omega \in \Omega$, we have $X(\omega) \leq Y(\omega)$, then

$$E[X] \leq E[Y]$$

- $E[1_A] = P[A]$

- $E[C]$ $=$ $C$.

### Expectation Discrete

$$\sum_{n=0}^\infty |x_n|P(X = x_n) < +\infty$$
$$E[X] = \sum_{n=0}^\infty x_nP(X = x_n)$$

### Expectation Density

$$\int_{-\infty}^{\infty} |x|f_X(x)dx < +\infty$$
$$E[X] = \int_{-\infty}^{\infty} xf_X(x)dx$$

### Transfer Theorem

Let $X$ be a random variable defined on a probability space $(\Omega, \mathcal{F}, P)$, and $g$ be a function from $\mathbb{R}$ to $\mathbb{R}$. Then, the quantity $E[g(X)]$ depends only on the function $g$ and the distribution of $X$.
$$E[g(X)] = \sum_{n=0}^\infty g(x_n)P(X = x_n)$$
$$E[g(X)] = \int_{-\infty}^{\infty} g(x)f_X(x)dx$$

### Markov's Inequality

$$P(X \geq \alpha) \leq \frac{E[X]}{\alpha}, \quad \alpha>0$$
$$P(X \geq \alpha) \leq \frac{E[g(X)]}{g(\alpha)}, \quad g \text{ is positive and strictly increasing}$$

### Median

$$P(X \leq m) \geq \frac{1}{2} \text{ and } P(X \geq m) \geq \frac{1}{2}$$

### Variance

$$\text{Var}(X) = E\left[(X - E[X])^2\right]$$

$$\text{Var}(X) = E[X^2] - E[X]^2$$

$$\sigma(X) = \sqrt{\text{Var}(X)} - \text{ standard deviation}$$

$$Var(X)(\text{discrete})=\left(\sum_{n=1}^{+\infty}x^2_nP(X=x_n)\right)-\left(\sum_{n=1}^{+\infty}x_nP(X=x_n)\right)^2$$

$$Var(X)(\text{real})=\left(\int_Rt^2f_X(t)dt\right)-\left(\int_Rtf_X(t)dt\right)^2$$

Let $X$ be a random variable with finite variance, and $\lambda$ a real number. We have:

- $\text{Var}(\lambda X) = \lambda^2 \text{Var}(X)$
- $\text{Var}(X + \lambda) = \text{Var}(X)$
- $X$ is almost surely (a.s.) constant if and only if $\text{Var}(X) = 0$
- $\text{Var}(X) = E[X^2] - E[X]^2$

### Chebyshev's Inequality

$$P(|X - E[X]| \geq \beta) \leq \frac{\text{Var}(X)}{\beta^2}, \quad \beta \in R \backslash 0$$

## Hypothesis Testing 

Hypothesis testing is a statistical method used to make inferences or decisions about a population based on sample data. It evaluates whether there is enough evidence to reject a null hypothesis in favor of an alternative hypothesis.

1. Define $H_0: p_0 = 0.5, H_1: p_0 < 0.5$
2. Calculate test statistic:
   1. For a $z-$test (when population std is known): $z = \frac{\overline{x}-\mu}{\frac{\sigma}{\sqrt{n}}}$ with $\overline{x}$ sample mean.
   2. For a $t-$test (when population std is unknown): $t=\frac{\overline{x}-\mu}{\frac{s}{\sqrt{n}}}$ with $s$ sample std.
3. For specific $\alpha$ and test statistic value look-up p-value in the table.
4. Find $p$-value: $\frac{10}{1024}$.
5. Check if $p$-value is less than significance level $\alpha$ $\to$ reject.

### Example

A company claims that the average time to assemble a product is 15 minutes. A sample of 25 workers has a mean assembly time of 14.5 minutes with a standard deviation of 0.8 minutes. At $\alpha=0.05$, is there enough evidence to reject the company’s claim?

$t=\frac{14.5-15}{\frac{0.8}{\sqrt{25}}}=-3.125$.

Check the p-value using a $t-$distribution table. If $p<0.05$, reject $H_0$.

## p-value

P-value is the probability of observing data under the null hypothesis.

## Confidence Intervals

A confidence interval provides a range of values within which the true population parameter (e.g., mean or proportion) is likely to fall with a certain level of confidence (usually 95%).

- When population standard deviation is known, $z-$distribution: $\overline{x}\plusmn z_{\alpha/2}\cdot\frac{\sigma}{\sqrt{n}}$
- When population standard deviation is unknown, $t-$distribution: $\overline{x}\plusmn t_{\alpha/2}\cdot\frac{s}{\sqrt{n}}$

### Example

Suppose a sample of 30 students has a mean exam score of 85 with a sample standard deviation of 5. Construct a 95% confidence interval for the true mean exam score. Then confidence interval is $85\plusmn t_{0.025, 29}\cdot\frac{5}{\sqrt{30}}$, where $t_{0.025, 29}\approx2.045$ (from $t-$table). Thus, we are 95% confident that the true population mean lies between 83.13 and 86.87.

## Distributions and Mean/Variance Calculation

## CLT

CLT and why used.
