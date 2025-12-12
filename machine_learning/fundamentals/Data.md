# Data Techniques

## Sets

- training set - data used to tune model parameters $𝑤$ and $𝑏$ in training or fitting;
- cross-validation set - data used to tune other model parameters like degree of polynomial, regularization or the architecture of a neural network;
- test set - data used to test the model after tuning to gauge performance on new data.

## Data techniques

Sometimes, focusing more time on your data can be the most efficient way to help your learning algorithm improve its performance.

1. Downloading related to task data from internet.
   
2. Labeling unlabeled data.
   
3. Data augmentation: modifying an existing training example to create a new training example. This technique is extremely popular in image recognition and speech recognition. Some data augmentation techniques are: enlarning image, rotating image, applying distortions,  random grid warpings, changing colors (image classification), adding noise/noisy background, random power, etc. (speech recognition)

    **Remember**: introduced distortions in the training set should be representation of the type of noise/distortions in the test set! It is usually does not help to add purely random/meaningless noise to your data.

    ![image](https://user-images.githubusercontent.com/73081144/193437009-998e81d8-b55d-47a0-86e6-993f64bfcf42.png)

    *Fig. 1. Image distortions in train and test sets.*

4. Data synthesis: using artificial data inputs to create a new training example. For example, in photo OCR problem, one way to create artificial data for this task is if you go to your computer's text editor, you find that it has a lot of different fonts and what you can do is take these fonts and basically type of random text in your text editor. And screenshotted using different colors and different contrasts and very different fonts and you get synthetic data like that on the right.

    ![image](https://user-images.githubusercontent.com/73081144/193437060-43fa1fca-c723-4492-96d9-9ad91290ab81.png)

    *Fig. 2. Artificial data synthesis example.*

5. Engineering the data used by your system.

## Skewed Datasets

Sometimes you will have datasets, where there are much more labels of one type than other. These datasets are called **unbalanced** or **skewed**. 

To evaluate your algorithm's perfomance on unbalanced dataset, use confusion matrix and precision/recall metrics.

By raising prediction threshold in skewed datasets, you end up with higher precision, but lower recall.

If you want to avoid missing too many cases of, e.g., rare disease, then, when in doubt, predict $y=1$, so you should lower your threshold to, for instance, $0.3$, so that you don't leave patients untreated.

When lowering prediction threshold, you end up with lower precision, but higher recall.

## Mini-batching

Mini-batching is a technique, where on every step gradient descent step, instead of using all data examples, we would pick some subset, e.g. 1,000 or $m'$ examples to update model parameters. The inner term of updating parameters $w$ becomes $w=w-\alpha \frac{\partial}{\partial w}\frac{1}{2m'}\sum^{m'}_{i=1}(f_{w,b}(x^{(i)} - y^{(i)})^2$ (example with the squared error loss function). Now each iteration through gradient descent requires looking only at the $m'$ rather than $m$ examples, and every step takes much less time and just leads to a more efficient algorithm.

![image](https://user-images.githubusercontent.com/73081144/200239253-8baf5096-1803-4c72-a97e-2bb61ea30652.png)

*Fig. 3. Mini-batch learning.*

On average, mini-batch gradient descent will tend toward the global minimum, not reliably and somewhat noisily, but every iteration is much more computationally inexpensive and so mini-batch learning or mini-batch gradient descent turns out to be a much faster algorithm when you have a very large training set.
