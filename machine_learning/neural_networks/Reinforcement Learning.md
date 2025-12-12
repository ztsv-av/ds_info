# Reinforcement Learning

Reinforcement learning is a machine learning training method based on rewarding desired behaviors and/or punishing undesired ones. In general, a reinforcement learning agent is able to perceive and interpret its environment, take actions and learn through trial and error.

In reinforcement learning, you tell an algorithm **what** to do, instead of how to do it with the help of a reward function.

For example, think of an autonomous helicopter. The reward function is going to look something like this:
- positive reward: helicopter flying well $+1$;
- negative reward: helicopter flying poorly/crushes $-1000$.

*Note: in reinforcement learning, if you take some hyperparameters not as good, then the model will actually take much more time to train than in supervised learning.*

## Terminology

- $s=$ state.
- $a=$ action.
- $R(s)=$ *immediate reward* = reward associated with state $s$.
- $s'=$ state you get after taking action $a$.
- $a' =$ action you take in state $s'$.
- $\gamma =$ discount factor, describes patience of an algorithm.
- $R_t =$ terminal state - state where an algorithm gets a reward, but nothing happens after that. For example, states 1 and 6 are terminal states.

![image](https://user-images.githubusercontent.com/73081144/199886789-21ed03d7-c519-4490-be16-83c15cfc476c.png)

*Fig. 1. Terminal state examples.*

- Markov Decision Process (MDP) - MDP states that the future only depends on the current state and not on anything that might have occurred prior to getting to the current state.

## The Return

The Return in reinforcement learning allows algorithm to understand which particular set of rewards is better or worse than different set of rewards. Based on the return value, your algorithm will know which action to take.

Return function:

$$return = R_1 + \gamma R_2 + \gamma^2R_3 + ... + \gamma^{t - 1}R_t$$

, where

- $R_n =$ reward at state $n$;
- $\gamma =$ discount factor.

Common choice for discount factor $\gamma$ is usually pretty close to $1$, like $0.9, 0.99, 0.999$, etc.

![image](https://user-images.githubusercontent.com/73081144/199888571-1ebac6d8-c4c7-4556-b4bb-5a12a70b65fb.png)

*Fig. 2. Example of the return.*

Negative rewards cause the algorithm to push out negative rewards as far into the future as possible.

## Policy

In reinforcement learning, our goal is to come up with a function which is called a policy $\pi$, whose job it is to take as input any state $s$ and map it to some action $a$ that it wants us to take to **maximize the return**.

For example, in figure below the policy will tell us to go left if we are in states 1,2,3,4, because the reward is greater. If we are in states 5 and 6, then the policy will tell us to go right. So, policy maps every state to an action to maximize the return.

![image](https://user-images.githubusercontent.com/73081144/199889126-55466b01-7ae3-4f26-8e17-243cf8236f59.png)

*Fig. 3. Policy explained.*

## State-action Value Function | Optimal $Q$ Function

State-action value function $Q(s,a) = Q^* =$ optimal $Q$ function $=$ *max return* if you:

- start in state $s$;
- take action $a$ (once);
- then behave optimally after that (actions that will result in highest possible return).

Example:

|   Reward   | 100 | 0 | 0 | 0 | 0 | 40 |
| ---------- | --- | - | - | - | - | -- |
| State $s$  |  1  | 2 | 3 | 4 | 5 | 6  | 

$Q(2, <=) = 0 + \gamma * 100 = \gamma * 100$

$Q(2, =>) = 0 + \gamma * 0 + \gamma^2 * 0 + \gamma^3 * 100 = \gamma^3 * 100$ (go right, left, left, left, since going left is still better then going right all the way down to the terminal state)

$Q(4, <=) = 0 + \gamma * 0 + \gamma^2 * 0 + \gamma^3 * 100 = \gamma^3 * 100$

Thereby, the best possible *return* from state $s$ is $max_aQ(s,a)$ ($Q(4, <=) = 12.5 > Q(4, =>) = 10$)

The best possible action in state $s$ is the action $a$ that gives $max_aQ(s,a)$

$\pi(s) = a = max_aQ(s,a)$

In some sence, building a table with optimal $Q$ function values (each state going right and left) is a recursive function.

## Bellman Equation

Bellman equation helps to compute the state-action value function $Q(s,a)$.

$$Q(s,a) = R(s) + \gamma max_{a'}Q(s', a')$$

, where

- $R(s) =$ immediate reward;
- $\gamma max_{a'}Q(s', a') =$ return from behaving optimally starting from state $s'$.

## Random (stochastic) Environment

Stochatic environment is an environment where actions you take have a probability where the result of that action is not what you expect it to be. For example, if you go left, you have 90% of succeeding (going left) and 10% of perfoming another action, like going right or slippering.

So, in a stochastic reinforcement learning problem, what we're interested in is not maximizing the return because that's a random number. What we're interested in is maximizing the average value of the sum of discounted rewards. By average value, we mean if you were to take your policy and try it out a thousand times or a 100,000 times or a million times, you get lots of different reward sequences and if you were to take the average over all of these different sequences of the sum of discounted rewards, then that's what we call the expected return.

Then, the return function is going to change to:

$$expected \space return = avg(R_1 + \gamma R_2 + \gamma^2R_3 + ... + \gamma^{t - 1}R_t) = E[R_1 + \gamma R_2 + \gamma^2R_3 + ... + \gamma^{t - 1}R_t]$$

And Bellman equation:

$$Q(s,a) = R(s) + \gamma E[max_{a'}Q(s', a')]$$

The higher the misstep probability, the lower the $Q(s,a)$ at each state.

*Funny fact: if the misstep probablity is $>0.5$, it is actually better to go the opposite direction you would normally go.*

## Continious State Spaces

Most system can be in continious number of states/positions (such as system location). 

For example, for a car, the state might include 6 numbers: $x$ position, $y$ position, $\theta$ orientation (where it faces), $\dot{x}$ how quickly $x$ coordinate changing, $\dot{y}$ how quickly $y$ coordinate changing, $\dot{\theta}$ how quickly angle of a car changing. Each number here can take any value of a valid number range.

For an autonomous helicopter, we will have 12 numbers associating the state of the system: $x, y, z,$ $\phi$ (row), $\theta$ (pitch), $\omega$ (yaw), $\dot{x}, \dot{y}, \dot{z}, \dot{\phi}, \dot{\theta}, \dot{\omega}$.

## Learning State-action Value Function | Deep $Q$ Network

When starting building $Q(s,a)$ it is obvious you don't know which action leads to the best possible reward. So, when calculating $Q(s,a)$ first actions can be taken randomly. The algorithm will work nonetheless. In every step, $Q$ will be some random guess. It'll get better over time what the actual $Q$ function is. By building $Q(s,a)$ table you actually create a dataset for the supervised learning algorithm.

First, you are in a state $s_1$. You take some action $a_1$ and end up getting reward $R(s_1)$ and in state $s'_1$. So, you created first training example: $x_1 = (s_1, a_1), y_1 = R(s_1) + \gamma max_{a'}Q(s_1', a')$. Remember, we don't know what next action $a'$ to take, so we will take it randomly.

Here is the full learning algorithm:

1. Initialize neural network randomly as guess of $Q(s,a)$. The algorithm will then improve its parameters to get better estimate.
2. Repeat {
   1. Take actions (randomly) in the lunar lander. You will get a lot of data $(s, a, R(s), s')$.
   2. Store $n$ (e.g. $10000$) most recent $(s, a, R(s), s')$ tuples. Remembering $10000$ most recent tries is just to make sure not to use excessive memory. This technique is called **Replay Buffer**.
   3. Train neural network:
      1. Create training set of $1000$ (**mini-batching**) examples using $x = (s, a)$ and $y = R(s) + \gamma max_{a'}Q(s', a')$. $Q(s', a')$ may not be the best guess, but it is a guess, created from previously storing $10000$ tries.
      2. Train $Q_{new}$ such that $Q_{new}(s,a) \approx y$. This neural network $Q_{new}$ should be a slightly better estimates of what the $Q$ function or the state action value function should be. 
      3. Set $Q = Q_{new}$ by using **Soft Update** technique. With this technique, you set parameters $w$ and $b$ as follows:
           - $w = 0.01 w_{new} + 0.99w$
           - $b = 0.01 b_{new} + 0.99b$

            $0.01$ and $0.99$ control how aggressively you move parameters to parameters of the newly trained model. This is done, because sometimes new models turn out to be worse than previously trained models and we don't want to take steps back. **Soft update** method causes the reinforcement learning algorithm to converge more reliably. It makes it less likely that the reinforcement learning algorithm will oscillate or divert or have other undesirable properties.

It turns out that if you run this algorithm where you start with a really random guess of the $Q$ function, then use Bellman's equations to repeatedly try to improve the estimates of the $Q$ function, and by doing this over and over, taking lots of actions, training a model, that will improve your guess for the $Q$ function. For the next model you train, you now have a slightly better estimate of what is the $Q$ function. Then the next model you train will be even better when you update $Q$ equals $Q_{new}$. For the next time you train a model $Q(s', a')$ will be an even better estimate. As you run this algorithm on every iteration, $Q(s', a')$ hopefully becomes an even better estimate of the $Q$ function so that when you run the algorithm long enough, this will actually become a pretty good estimate of the true value of $Q(s, a)$ so that you can then use this to pick, hopefully good actions for the MTP.

We call this neural network a $𝑄 -Network$ and it can be trained by adjusting its weights at each iteration to minimize the mean-squared error in the Bellman equation.

Unfortunately, using neural networks in reinforcement learning to estimate action-value functions has proven to be highly unstable. Luckily, there's a couple of techniques that can be employed to avoid instabilities. These techniques consist of using a **Target Network** and **Experience Replay**.

### Target Network

We can train the $Q$-Network by adjusting it's weights at each iteration to minimize the mean-squared error in the Bellman equation, where the target values are given by:

$$
y = R + \gamma \max_{a'}Q(s',a';w)
$$

where $w$ are the weights of the $Q$-Network. This means that we are adjusting the weights $w$ at each iteration to minimize the following error:

$$
\overbrace{\underbrace{R + \gamma \max_{a'}Q(s',a'; w)}_{\rm {y~target}} - Q(s,a;w)}^{\rm {Error}}
$$

Notice that this forms a problem because the $y$ target is changing on every iteration. Having a constantly moving target can lead to oscillations and instabilities. To avoid this, we can create
a separate neural network for generating the $y$ targets. We call this separate neural network the **target $\hat Q$-Network** and it will have the same architecture as the original $Q$-Network. By using the target $\hat Q$-Network, the above error becomes:

$$
\overbrace{\underbrace{R + \gamma \max_{a'}\hat{Q}(s',a'; w^-)}_{\rm {y~target}} - Q(s,a;w)}^{\rm {Error}}
$$

where $w^-$ and $w$ are the weights the target $\hat Q$-Network and $Q$-Network, respectively.

In practice, we will use the following algorithm: every $C$ time steps we will use the $\hat Q$-Network to generate the $y$ targets and update the weights of the target $\hat Q$-Network using the weights of the $Q$-Network. We will update the weights $w^-$ of the the target $\hat Q$-Network using a **soft update**. This means that we will update the weights $w^-$ using the following rule:
 
$$
w^-\leftarrow \tau w + (1 - \tau) w^-
$$

where $\tau\ll 1$. By using the soft update, we are ensuring that the target values, $y$, change slowly, which greatly improves the stability of our learning algorithm.

### Experience Replay

When an agent interacts with the environment, the states, actions, and rewards the agent experiences are sequential by nature. If the agent tries to learn from these consecutive experiences it can run into problems due to the strong correlations between them. To avoid this, we employ a technique known as **Experience Replay** to generate uncorrelated experiences for training our agent. Experience replay consists of storing the agent's experiences (i.e the states, actions, and rewards the agent receives) in a memory buffer and then sampling a random mini-batch of experiences from the buffer to do the learning. The experience tuples $(S_t, A_t, R_t, S_{t+1})$ will be added to the memory buffer at each time step as the agent interacts with the environment.

By using experience replay we avoid problematic correlations, oscillations and instabilities. In addition, experience replay also allows the agent to potentially use the same experience in multiple weight updates, which increases data efficiency.

## Deep $Q$ Network Refinements

- At the last layer in the network, output all possible actions corresponding to the current state. For example, if you have 4 total actions, then the last dense layer will have 4 neurons.
- **$\epsilon-$ greedy Policy**: $\epsilon-$ greedy policy helps to pick best actions even during actions learning. What most people do, is to with probability of $0.95$ pick the action that maximizes $Q(s,a)$, and with probability $0.05$ pich an action $a$ randomly. This way, you will explore greater number of possible actions and their rewards. Because of the random initialization, if the neural network somehow initially gets stuck in the mind that some things are bad idea, just by chance, it means that it will never try out some actions and discover that maybe is actually a good idea to take these actions. With small chance of taking actions randomly, the neural network can learn to overcome its own possible preconceptions about what might be a bad idea that turns out not to be the case. Random step is called **Exploration**. Step maximizing $Q(s,a)$ is called **Greedy** or **Exploitation**. Combination of these two steps is called **$\epsilon-$ greedy policy** ($\epsilon =$ 0.05 or some other number). Another trick with this policy is to gradually decrease $\epsilon$, starting with high value, so that you take more random actions at first and more actions that actually maximize $Q(s,a)$ later.

## Applications

Reinforcement learning has been applied in:
- controlling robots;
- factory optimization;
- financial (stock) trading;
- playing games.
 