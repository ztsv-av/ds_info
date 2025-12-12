# Computer Vision

The first layers of a neural network you might find one neuron that is looking for the low vertical line or a vertical edge. A second neuron looking for a oriented line or oriented edge. The third neuron looking for a line at that orientation, and so on. In the earliest layers of a neural network, you might find that the neurons are looking for very short lines or very short edges in the image. At the next hidden layer, you find that these neurons might learn to group together lots of little short lines and little short edge segments in order to look for parts of something in the image, such as parts of a face. At the next hidden layer, the neural network is aggregating different parts of faces to then try to detect presence or absence of larger, coarser face shapes. Then finally, detecting how much the face corresponds to different face shapes creates a rich set of features that then helps the output layer try to determine the identity of the person in the picture. Neural network can learn these feature detectors at the different hidden layers all by itself.

![image](https://user-images.githubusercontent.com/73081144/187837278-d755681b-5032-4eb8-8b70-da8d5aa6f33d.png)

*Fig. 1. Motivation of neural networks in face recognition task.*

![image](https://user-images.githubusercontent.com/73081144/187837491-3fc85817-d577-4aa6-bbb4-f2526db3bc60.png)

*Fig. 2. Neural networks in car detection task.*
