# Terminology 
- training set - data used to train the model. Usually consists of features and targets (supervised learning);
- cost function - error, measurment of how a prediction is distant from the truth value;
- generalization - the ability of an algorithm for making predictions. You say you want your algorithm to generalize well, meaning make good prediction;
- regularization - prevents your model to choose high values for parameters, so there is no need to throw away important features if model overfits training data;
- input layer - layer that consists of all input features;
- hidden layer - middle layer, layer that constists of many neurons which perform some computations and output activations;
- output layer - last layer in the network
- activation - how much a neuron is sending a high output to other neurons downstream from it (output of a neuron)

    $a^{[l]}_j = g(\vec{w}^{[l]}_j * \vec{a}^{[l-1]} + b^{[l]}_j)$

- layer - grouping of neurons which takes as input the same or similar features, and that in turn outputs a few numbers together;
- multilayer perceptron - a neural network with multiple hidden layers;
- binary classification: target $y$ can take only $2$ possible values - $0$ and $1$;
- multiclass classification: target $y$ can take on more than $2$ **single** possible values (from $1...N$): $y = [0, 0, 1, 0, 0];
- multi-label classification: target $y$ can take on more than $2$ **multiple** possible values (from $1...N$): $y = [1, 0, 1, 0, 1]$;
- batch: the batch size is a number of samples processed before the model is updated; the size of a batch must be more than or equal to one and less than or equal to the number of samples in the training dataset;
