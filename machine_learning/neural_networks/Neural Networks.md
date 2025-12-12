# Neural Networks

## Motivation

In recent years, use of neural networks compared to fundamental machine learning algorithms has grown a lot.

![image](https://user-images.githubusercontent.com/73081144/187833423-10be35fa-2e23-4ade-9c0c-808552d9163f.png)

*Fig. 1. Why use neural networks now?*

Artificial neural networks use a very simplified mathematical model of what a biological neuron does. The mathematical model of a neuron takes an input, computes a function (for example logistic regression) and outputs some number (activation).

![image](https://user-images.githubusercontent.com/73081144/187833913-d15b2165-1dd9-4969-8391-8d7add8dae14.png)

*Fig. 2. Simple example of a demand prediction using a mathematical neuron.*

Every layer inputs a vector of numbers and applies a bunch of logistic regression units to it, and then computes another vector of numbers that then gets passed from layer to layer until you get to the final output layers computation, which is the prediction of the neural network. Then you can either threshold at 0.5 or not to come up with the final prediction.

In practice, in a neural network each neuron in a certain layer will have access to every feature, to every value from the previous layer. Each neuron will then learn which feaures it is best to ignore and on which to focus, which are the most relevant to it.

![image](https://user-images.githubusercontent.com/73081144/187835553-f94c79a6-5b63-427b-989e-84a36c3a39f0.png)

*Fig. 3. More advanced example of a demand prediction using a small neural network.*

One way to think of a neural network is as a modified function (e.g. logistic regression) which learns its own features that make it easier to predict something. In other words, it performs feature engineering all by itself.

![image](https://user-images.githubusercontent.com/73081144/187836298-68030d27-a388-4dc2-b5a1-33db28f2be01.png)

*Fig. 4. Multilayer perceptrons - neural networks with multiple hidden layers.*

## Computation Process in Neural Networks

![image](https://user-images.githubusercontent.com/73081144/187838376-1feed256-dc4b-414d-92d8-158fc3346aa9.png)

*Fig. 5. Neural network layer **1** computation process.*

![image](https://user-images.githubusercontent.com/73081144/187838552-f10f7c39-cb66-42f6-bcff-8fd779b9fe83.png)

*Fig. 6. Neural network layer **2** computation process.*

![image](https://user-images.githubusercontent.com/73081144/187838640-c3d8249c-901b-40e6-8552-d53b6bbc1b4e.png)

*Fig. 7. Neural network output.*

## Neural Networks Notation

Each hidden unit, neuron, outputs some number, called **activation**. Activation value of layer $l$, unit (neuron) $j$ is computed as follows:

$$a^{[l]}_j = g(\vec{w}^{[l]}_j * \vec{a}^{[l-1]} + b^{[l]}_j)$$

, where
- $\vec{w}^{[l]}_j$ - parameter $w$ of layer $l$, unit $j$,
- $b^{[l]}_j$ - parameter $b$ of layer $l$, unit $j$,
- $\vec{a}^{[l-1]}$ - activation value of previous layer $l-1$,
- $g(...)$ - activation function.

![image](https://user-images.githubusercontent.com/73081144/187840710-8f528f26-c80c-4a0f-a9e3-15473b54d32d.png)

*Fig. 8. Neural networks notation.*

## Parameters Dimensions and Numbers

The dimensions of parameters $W$ and $b$ are determined as follows:
- if network has $s_{in}$ units in a layer and $s_{out}$ units in the next layer, then: 
  - $W$ will be of dimension $s_{in} \times s_{out}$.
  - $b$ will a vector with $s_{out}$ elements
  
Therefore, if we have a NN with $25$ units in layer 1, $15$ units in layer 2 and $1$ output unit in layer 3, then the shapes of $W$, and $b$, are: 
- layer1: The shape of $W1$ is (400, 25) and the shape of $b1$ is (25,)
- layer2: The shape of $W2$ is (25, 15) and the shape of $b2$ is: (15,)
- layer3: The shape of $W3$ is (15, 1) and the shape of $b3$ is: (1,)

The number of parameters in each layer correspond to the following formula:

*num_params* = $s_{in} \times s_{out} + s_{out}$ 
, where
- $s_{in}$ - dimension of the inputs to the layer;
- $s_{out}$ - number of units in the layer.

## Forward Propagation

Forward propagation is the process of propagating the activations of the neurons. In neural networks, computations are made in the forward direction from left to right. And this is in contrast to a different algorithm called backward propagation or back propagation, which is used for learning.
