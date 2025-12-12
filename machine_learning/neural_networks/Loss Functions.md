# Loss Functions

*Note: cost function is the average across all values of loss functions for each example:*

$J(w,b) = \frac{1}{m}\sum_{i=1}^mL(f_{w,b}(x), y)$

*Note: it is better to use **from_logits=True** (here logit is $z=wx + b$) when implementing loss function due to the numerical roundoff errors. In other words, make last layer activation function linear and compute activation during loss.*

![image](https://user-images.githubusercontent.com/73081144/191156481-56d23fca-91b6-4d5e-8990-0623f5160815.png)

*Fig. 1. Numerical roundoff errors with sigmoid function.*

![image](https://user-images.githubusercontent.com/73081144/191156705-c5b84c4a-1335-47a7-b0fe-c40f32cb817f.png)

*Fig. 2. Numerical roundoff errors with softmax function.*

## Squared Error

$$L(w,b) = (\hat{y}^{(i)}-y^{(i)})^2$$

- $m$ - number of training examples, 
- $\hat{y}^{(i)} = f_{w,b}(x^i)$ - $i^{th}$ prediction, 
- $y^{(i)}$ - $y^{th}$ true value.

```
def mse_loss(y_true, y_pred):
    """
    mean squared error loss function.

    parameters
    ----------
        y_true : array
            array of true output values.

        y_pred : array
            array of predicted values for each true value.

    returns
    -------
        mse : float
            value of the mse
    """

    mse = np.substract(y_true, y_pred)
    mse = mse**2

    return mse
```

## Logistic (Binary Crossentropy)

Logistic loss is also known as *binary cross entropy*.

$$L(f_{w,b}(x^i), y^i) = \begin{cases} 
    -log(f_{w,b}(x^i)), & \text{if } y^i=1 \\ 
    -log(1 - f_{w,b}(x^i)), & \text{if } y^i=0 \end{cases}$$

$$or$$

$$L(f_{\mathbf{w},b}(\mathbf{x}^{(i)}), y^{(i)}) = (-y^{(i)} \log\left(f_{\mathbf{w},b}\left( \mathbf{x}^{(i)} \right) \right) - \left( 1 - y^{(i)}\right) \log \left( 1 - f_{\mathbf{w},b}\left( \mathbf{x}^{(i)} \right) \right)$$

, where

- $f_{w,b}(x^i) = \frac{1}{1 + e^{\vec{w} * \vec{x} + b}}$;

*Note that $y^i$ can only take two values: 0 and 1*

For the first case, when $y^i = 1$:

![image](https://user-images.githubusercontent.com/73081144/185816661-8dbc7c4e-4c84-4d77-bd08-0ad470861c8f.png)

*Fig. 3. Logistic loss function: case if y=1*

For the first case, when $y^i = 0$:

![image](https://user-images.githubusercontent.com/73081144/185817281-b8330103-e419-484d-ac78-6debeb946037.png)

*Fig. 4. Logistic loss function: case if y=0*

```
def logistic_loss(y_true, y_pred):
    """
    computes logistic loss function.

    parameters
    ----------
        y_true : array
            array of true output values.

        y_pred : array
            array of predicted values for each true value.

    returns
    -------
        logistic : float
            value of the logistic cost function
    """

    logistic = -1 * y_true * np.log(y_pred) - (1 - y_true) * np.log(1 - y_pred)

    return logistic
```

## Softmax Regression (Crossentropy)

The softmax regression algorithm is a generalization of logistic regression, which is a binary classification algorithm to the **multiclass** classification contexts.

$$L = -loga_j, \space if \space y=j$$

$$a_j=\frac{e^{z_j}}{\sum_{k=1}^Ne^{z_k}}=P(y=j|\vec{x})$$

The output $\mathbf{a}$ is a vector of length N, so for softmax regression, you could also write:

$$\mathbf{a}(x) =
\begin{bmatrix}
P(y = 1 | \mathbf{x}; \mathbf{w},b) \\
\vdots \\
P(y = N | \mathbf{x}; \mathbf{w},b)
\end{bmatrix}
=
\frac{1}{ \sum_{k=1}^{N}{e^{z_k} }}
\begin{bmatrix}
e^{z_1} \\
\vdots \\
e^{z_{N}} \\
\end{bmatrix}$$

![image](https://user-images.githubusercontent.com/73081144/189252010-90105ea7-7991-41c6-8cf5-d9da256d46df.png)

*Fig. 5. Softmax regression.*

Cost function for softmax cross-entropy loss:

$$J(\mathbf{w},b) = -\frac{1}{m} \left[ \sum_{i=1}^{m} \sum_{j=1}^{N}  1\left\{y^{(i)} == j\right\} \log \frac{e^{z^{(i)}_j}}{\sum_{k=1}^N e^{z^{(i)}_k} }\right]$$

, where

- m - number of examples;
- N - number of outputs;
- $1\left\{y^{(i)} == j\right\}$ - indicator function that equals $1$ when the index matches the target and $0$ otherwise.
