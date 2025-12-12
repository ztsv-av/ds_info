# Supervised Learning

Supervised learning - algorithms that learn input to output mapping (Input(X) -> Output(Y)). In this type of learning, you give your algorithm examples to learn from that include correct labels for a particular input. For example, you might provide your algorithm with AD and USER INFO data and get CLICK (0/1) probability (used in online advertising).

## Types of Supervised Learning Algorithms

- Regression: the task is to predict a number based on some input. For example, predicting house price based on its size. In regression, there are infinetely many possible outputs.

- Classification: the task is to classify, predict a label, category of something. For example, predicting whether a tumor is malignant type1 (1), malignant type2 (2) or benign (0) based on its diameter and age of a patient. Classification predicts small, finity number of possible outputs.
  - binary classification: target $y$ can take only $2$ possible values - $0$ and $1$;
  - multiclass classification: target $y$ can take on more than $2$ **single** possible values (from $1...N$): $y = [0, 0, 1, 0, 0];

    ![image](https://user-images.githubusercontent.com/73081144/189250162-d77ad845-5f20-4e23-b9c9-bbdef404d850.png)

    *Fig. 1. Binary and multiclass classification.*

  - multi-label classification: target $y$ can take on more than $2$ **multiple** possible values (from $1...N$): $y = [1, 0, 1, 0, 1]$

    ![image](https://user-images.githubusercontent.com/73081144/191157322-39104e78-3e38-4c67-882e-0063a4b44166.png)

    *Fig. 2. Multi-label classification example.*

    In multi-label classification, use sigmoid activation function at each unit at the last layer (number of units equals to number of classes).

## Training Process

There are 3 main steps when training an supervised model:

1. specify how to compute output given input $x$ and parameters $w, b$ (define model):

    $f_{\vec{w}, b}(\vec{x}) = ?$

2. specify loss and cost functions:

    $L(_{\vec{w}, b}(\vec{x}), y) = ?$

    $J(\vec{w}, b) = \frac{1}{m}\sum_{i=1}^mL(_{\vec{w}, b}(\vec{x}^{(i)}), y^{(i)}) = ?$

3. train on data to minimize $J(\vec{w}, b)$


![image](https://user-images.githubusercontent.com/73081144/189243410-af71bfcc-34c6-4cc4-a86f-9ce3e863e444.png)

*Fig. 3. Supervised model training steps.*
