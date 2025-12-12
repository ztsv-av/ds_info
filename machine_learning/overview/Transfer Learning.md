# Transfer Learning

Transfer learning is the process when you use a model previously trained on a big dataset and use it for your own problem, changing just classification/top layer/s if necessary.

For an application where you don't have that much data, transfer learning is a wonderful technique that lets you use data from a different task to help on your application.

There are two steps in transfer learning:
1. **supervised pretraining** - training a model on a task that has much more data than in final problem;
2. **fine tuning** - taking the parameters that you had initialized or gotten from supervised pretraining and then run gradient descent further to fine tune the weights to suit the specific application you want.

![image](https://user-images.githubusercontent.com/73081144/193437268-86ce7c07-3171-4cc7-89b4-d289ec3691db.png)

To apply transfer learning, what you do is then make a copy of supervised pretraining neural network where you would chip the parameters $W^1, b^1, W^2, b^2, W^3, b^3, W^4, b^4$, etc. But for the last layer, you would eliminate the output layer and replace it with a much smaller output layer with just $N$ rather than $K$ output units, where $K >> N$. Notice that the output parameters $W^N, b^N$ can't be copied over because the dimension of this layer has changed, so you need to come up with new parameters $W^N, b^N$ that you need to train from scratch rather than just copy it from the previous neural network.

In transfer learning, what you can do is use the parameters from the first layers, really all the layers except the final output layer as a starting point for the parameters and then run an optimization algorithm such as gradient descent or the Adam optimization algorithm with the parameters initialized using the values from this neural network up on top.

In detail, there are two options for how you can train this neural networks parameters. **Option 1** is you only train the output layers parameters. You would take the parameters $W^1, b^1, W^2, b^2$ through $W^{N-1}, b^{N-1}$ as the values from on top and just hold them fix and don't even bother to change them, and use an algorithm like Stochastic gradient descent or the Adam optimization algorithm to only update $W^N, b^N$ to lower the usual cost function that you use for learning. **Option 2** would be to train all the parameters in the network including $W^1, b^1, W^2, b^2$ all the way through $W^N, b^N$ but the first $N-1$ layers parameters would be initialized using the values that you had trained on top. If you have a very small training set then Option 1 might work a little bit better, but if you have a training set that's a little bit larger then Option 2 might work a little bit better.

## Why Transfer Learning Works?

First layers in neural network usually correspond to detecting basic features, such as image edges, corners, curves, basic shapes, etc. So, when you transfer this neural network layers to a task with new classification head, your new model is already pretrained to recognize these basic features, which increases and enhances training process significantly.

![image](https://user-images.githubusercontent.com/73081144/193437434-a2661e9a-c9aa-4296-a0d0-9b5e1fc8e0e7.png)

*Note: pretrained model and fine tuned model should be used for the same task. You cannot use a model for fine tuning, if pretrain task for image classification, and fine tuning task is audio recognition. However, sometimes it works...example: BIRDCLEF comptetition.*
