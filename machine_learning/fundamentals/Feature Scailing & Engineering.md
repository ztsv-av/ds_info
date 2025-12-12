# Feature Scailing

Feature scailing is performed for a gradient descent to more easily find a path to the global minimum.

If you have features that take different ranges of values it can cause gradient descent to run slowly (descent jumps back and forth in the elypse shaped graph in the Fig. 1.). Rescailing features makes them take a comprable range of values, which can speed up gradient descent significantly.

![image](https://user-images.githubusercontent.com/73081144/184578099-f9b2d725-ae9f-4e75-8b42-8b1ff9bafdcc.png)

*Fig. 1. Gradient descent with rescaled features.*

![image](https://user-images.githubusercontent.com/73081144/184579219-753d5ddc-e17f-45ee-bfb2-7ad30a0977be.png)

*Fig. 2. When to rescale features.*

## Feature Scailing Methods

There are many ways of how you can rescale features.

- **division my maximum**:

![image](https://user-images.githubusercontent.com/73081144/184578359-ed1861c6-4a32-4b2b-86f2-b7bb1344e855.png)

*Fig. 2. Divide by maximum feature scailing.*

- **min-max normalization**:

$x_{normed} = \frac{x - x_{min}}{x_{max}}$

This formula normalizes all features to range $0 <= x <= 1$

- **mean normalization**:

![image](https://user-images.githubusercontent.com/73081144/184578770-e6bb396c-7243-48c1-a318-1fea24d2b682.png)

*Fig. 3. Mean normalization.*

$x_{normed} = \frac{x - x_{\mu}}{x_{max} - x_{min}}$, where $x_{\mu} =$ mean of feature x values.

In this type of normalization, all features are centered around $0$ (they have both negative and positive values).

- **Z-score normalization**

![image](https://user-images.githubusercontent.com/73081144/184579100-00759bc1-a3b4-4c8c-9ada-9cfaf7d20204.png)

*Fig. 4. Z-score normalization.*

$x_{normed} = \frac{x - x_{\mu}}{x_{\sigma}}$, where $x_{\mu} -$ mean of feature x values, $x_{\sigma} -$ standart deviation of x feature values.

***Implementation Note**: When normalizing the features, it is important to store the values used for normalization - the mean value and the standard deviation used for the computations. After learning the parameters from the model, we often want to predict the prices of houses we have not seen before. Given a new x value (living room area and number of bed- rooms), we must first normalize x using the mean and standard deviation that we had previously computed from the training set.*


## Feature Engineering

Feature engineering - using intuition to design new features, by transforming or combining original features.

![image](https://user-images.githubusercontent.com/73081144/185279561-335fd1d6-62dc-451f-a10c-5e7eb33f36b3.png)

*Fig. 5. Feature engineering example.*
