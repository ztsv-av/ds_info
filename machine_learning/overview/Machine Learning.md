# Machine Learning

Machine learning - field of study that gives computers the ability to learn without being explicitly programmed (Andrew Samuel).

## Types of Machine Learning

- Supervised learning: algorithms that learn input to output mapping (Input(X) -> Output(Y)). In this type of learning, you give your algorithm examples to learn from that include correct labels for a particular input. For example, you might provide your algorithm with AD and USER INFO data and get CLICK (0/1) probability (used in online advertising).

- Unsupervised learning: in this type of learning, we are given data that is not associated with any output labels Y. In other words, data only comes with inputs X, but not output labels Y. The job here is to find some structure, pattern, or just something interesting about the unlabeled data.

- Recommender systems:

- Reinforcement learning: 

## Terminology

### Machine Learning

- training set - data used to train the model. Usually consists of features and targets (supervised learning);
- x - "input" variable; feature;
- y - "output", "target" variable;
- m - number of training examples;
- (x,y) - single training example;
- $(x^i, y^i)$ - $i^{th}$ training example;
- cost function - error, measurment of how a prediction is distant from the truth value;
- generalization - the ability of an algorithm for making predictions. You say you want your algorithm to generalize well, meaning make good prediction;
- regularization - prevents your model to choose high values for parameters, so there is no need to throw away important features if model overfits training data;
- batch: the batch size is a number of samples processed before the model is updated; the size of a batch must be more than or equal to one and less than or equal to the number of samples in the training dataset;

### Neural Networks

- input layer - layer that consists of all input features;
- hidden layer - middle layer, layer that constists of many neurons which perform some computations and output activations;
- output layer - last layer in the network
- activation - how much a neuron is sending a high output to other neurons downstream from it (output of a neuron)

    $a^{[l]}_j = g(\vec{w}^{[l]}_j * \vec{a}^{[l-1]} + b^{[l]}_j)$

- layer - grouping of neurons which takes as input the same or similar features, and that in turn outputs a few numbers together;
- multilayer perceptron - a neural network with multiple hidden layers;

### Neuroscience

- nucleus - cell body of a neuron;
- dendrite - wire that receives input (electrical impulse) from other neurons;
- axon - output wire that is used to send information (electrical impulse) to other neurons;
- activation - how much a neuron is sending a high output to other neurons downstream from it.

## Applications

### Supervised Learning

| Input(X) | Output(Y) | Application |
| -------- | --------- | ----------- |
| email | spam?(0/1) | spam filtering |
| audio | text transcripts | speech recognition |
| English | Spanish | machine translation |
| ad, user info | click?(0/1) | online advertising |
| image, radar info | position of other cars | self-driving car |
| image of phone | defect?(0/1) | visual inspection |

### Unsupervised Learning

| Input(X) | Output(Y) | Application |
| -------- | --------- | ----------- |
| DNA of an individual | - | **clustering** DNA data |
| customer data | - | **clustering** into different market segments |
| news articles | - | **clustering** into sets of articles about the same story |
| transcations | - | **anomaly detection** |
