# Learning Rate

Learning rate is the degree by how much you want to update network paramaters at each backpropagation step. $\alpha$ symbol is usually used to denote learning rate

If $\alpha$ is too **small**, then optimization algorithm will take tiny steps towards the local minima, and the whole training process may be **slow**.

If $\alpha$ is too **large**, then optimization algorithm will take big steps towards the local minima, and the whole training process may be **faster**, but it might constantly **miss** local minima, because steps are too big to descent lower.

![image](https://user-images.githubusercontent.com/73081144/183822563-2d14f851-8315-4e61-a29a-8270b88cbcf9.png)

*Fig. 1. Learning rate: small and large.*

![image](https://user-images.githubusercontent.com/73081144/185274638-bbde62ce-9628-4821-aa43-b199c4cccba8.png)

*Fig. 2. Choosing proper learning rate.*

![image](https://user-images.githubusercontent.com/73081144/185274846-22525b16-89d1-45a8-974b-9376cf2cd9cb.png)

*Fig. 3. Trying out different values of learning rate.*

If you cost function is constantly increasing, try choosing very small learning rate, to see if it still getting larger and larger. If it is, then something is wrong with the model or data or code.
