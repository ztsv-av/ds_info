# Decision Tree

Decision Tree (DT) is a non-parametric supervised learning method used for classification and regression. The goal is to create a model that predicts the value of a target variable by learning simple decision rules inferred from the data features. A tree can be seen as a piecewise constant approximation. As the name goes, it uses a tree-like model of decisions.

![image](https://user-images.githubusercontent.com/73081144/194198453-52e14485-b1aa-4905-a041-31fc419b4b88.png)

*Fig. 1. DT example.*

## Decision Tree Learning Process

1. start with all examples at the root node;
2. calculate information gain for all possible features, and pick the one with the highest information gain;
3. split dataset according to selected feature, and create left and right branches of the tree;
4. keep repeating splitting process until stopping criteria is met:
   - when a node is 100% one class;
   - when splitting a node will result in the tree exceeding a maximum depth;
   - information gain from additional splits is less than threshold;
   - when number of examples in a node is below a threshold.

Splitting in a decision tree is recursive process. You build the overall decision tree by building smaller sub-decision trees and then putting them all together.

## Splitting Decisions

1. Decision 1: How to choose what feature to split on at each node?
   - Maximuze **purity** (or minimize) based on **given features**.
2. Decision 2: When do you stop splitting?
   - When a node is 100% one class.
   - When splitting a node will result in the tree exceeding a maximum depth. E.g., if you decided that maximum depth of a tree is $2$, then depth 2 nodes will act as classes. *The smaller the tree, the less prone it is to overfitting*.
   - When improvements in purity score are below a threshold.
   - When number of examples in a node is below a threshold.

    ![image](https://user-images.githubusercontent.com/73081144/194199500-5765ece0-340d-46f8-9d39-afdeb9cc23f4.png)

    *Fig. 2. Number of examples in a node below threshold.*

    As you can see, there 2 dogs and 1 cat at the right node, meaning that it will assign all examples to *not-cat* at this node.

## Measuring Purity - Information Gain

When building a decision tree, the way we'll decide what feature to split on at a node will be based on what choice of feature reduces entropy the most. Reduces entropy or reduces impurity, or maximizes purity. In decision tree learning, the reduction of entropy is called **information gain**.

To meausre purity, people use entropy function. For example, imagine we are tasked to classify cats based on a set of feautres. In data, there are cats and dogs. 

$p_1 = \frac{3}{6} =$ fraction of examples that are cats.

Then, entropy is equal to $H(p_1)$. The graph of entropy function looks like this:


![image](https://user-images.githubusercontent.com/73081144/194200691-45755d0f-71b6-4d9f-8168-477f35e49d34.png)

*Fig. 43 Entropy function and purity.*


You can notice, that when data split is $50/50$, then the entropy is the most *impure*. The higher the value of entropy function, the more impure it is.

if $p_0 = 1 - p_1$, then

$$H(p_1) = -p_1log_2(p_1) - p_0log_2(p_0) = -p_1log_2(p_1) - (1 - p_1)log_2(1 - p_1)$$

*Note: in entropy, $0log(0) = 0$*

This function look like the function above.

There are other functions to measure purity, such as **Gini** or **Log loss**.

To correctly choose a feature by which we make a split, we compute purity of left and right splits. How important it is to have low entropy in, say, the left or right sub-branch also depends on how many examples went into the left or right sub-branch. Because if there are lots of examples in, say, the left sub-branch then it seems more important to make sure that that left sub-branch's entropy value is low. Which is why, after computing purity values, we compute their purity value by subracting higher node's entropy value with weighted average of current node entropy values and compare then with each other of each feature split, because that gives us the left and right sub-branches with the **lowest average weighted entropy**.

![image](https://user-images.githubusercontent.com/73081144/194202373-24e529c8-7354-4ba9-b6f2-43506e0fec78.png)

*Fig. 4. Information gain during split.*

These numbers that we just calculated, **0.28, 0.03, and 0.12**, these are called the **information gain**, and what it measures is the reduction in entropy that you get in your tree resulting from making a split. Choose split which has the higher entropy reduction. If the reduction in entropy (higher level node entropy minus current node entropy) is too small, than you are unnessecerely increasing tree size, which leads to overfitting.

Information gain formula:

$$IG = H(p_1^{root}) - (w^{left}H(p_1^{left}) + w^{right}H(p_1^{right}))$$

Then out of all the possible futures, you could choose to split on, you can then pick the one that gives you the highest information gain. That will result in, hopefully, increasing the purity of your subsets of data that you get on the left and right sub-branches of your decision tree and that will result in choosing a feature to split on that increases the purity of your subsets of data in both the left and right sub-branches of your decision tree.

## Regression with Decision Trees

If we have a regression problem, i.e. predicting some number, once at a leaf node, we take average of all target variables of all examples that are under the current node and use this number as a $y_{hat}$ based on data features for further predictions.

![image](https://user-images.githubusercontent.com/73081144/194222938-88960097-d642-4edf-828c-bae69ee477c9.png)

*Fig. 5. Regression with decision tree.*

The question is: how to properly choose a split, or how to compute information gain?

![image](https://user-images.githubusercontent.com/73081144/194223051-8e769425-864f-4fc2-bfda-5cdb38e82ca8.png)

*Fig. 6. Which split to choose in regression?*

As you can see, we splitted data based on different features. However, instead of classes, we have numerical values, so we can't compute entropy reduction the normal way. So, to evaluate the quality of a split, we will use the same formula, but instead of entropy, we will use **variance**. The **highest** the value of a **reduction in weighted variance**, the **better** the split.

![image](https://user-images.githubusercontent.com/73081144/194223675-111aee62-8731-45b1-9a3f-7cc369843bc4.png)

*Fig. 7. Variance in decision tree regression.*

## Data in Decision Trees

Data do not need to take only 2 possible values/features. If there are more than 2 features, then use *one-hot encoding*. In other words, if a categorical feature can take on $k$ values, create $k$ binary features (0 or 1 valued).

![image](https://user-images.githubusercontent.com/73081144/194221015-1da42711-b955-4dbd-a4a6-f85afa56d52f.png)

*Fig. 8. One-hot encoding in decision trees.*

You can also use *continuous variables* and split data based on the some threshold. During splitting, we'll try multiple values along the X axis. And one convention would be to sort all of the examples according to the weight or according to the value of this feature and take all the values that are mid points between the sorted list of training. Examples as the values for consideration for this threshold over here. This way, if you have 10 training examples, you will test nine different possible values for this threshold and then try to pick the one that gives you the highest information gain. And finally, if the information gained from splitting on a given value of this threshold is better than the information gain from splitting on any other feature, then you will decide to split that note at that feature.

![image](https://user-images.githubusercontent.com/73081144/194221974-c272904f-c3bb-4694-8212-7f18cdf0ad2a.png)

*Fig. 9. Splitting on a continous variable.*

## Useful Features of Decision Tree

- The smaller the tree, the less prone it is to overfitting.

## Tree Ensemble / Bagged DTs / Random Forest

Single decision tree can be highly sensitive to small changes in the data. One solution is to create a tree ensemble, sometimes called **forest**. Tree ensemble is a colletion of multiple decision trees. The idea is to run all decision trees on your data and get them to vote on whether the final prediction is.

![image](https://user-images.githubusercontent.com/73081144/194737677-a288d960-4a1f-4fea-8758-6b892186f3c0.png)

*Fig. 10. Tree ensemble.*

In order to build tree ensemble, we will need to use **sampling with replacement** technique. The way that sampling with replacement applies to building an ensemble of trees is as follows. We are going to construct multiple random training sets that are all slightly different from our original training set. In particular, we're going to take our 10 examples of cats and dogs. We're going to put the 10 training examples in a theoretical bag. We're going to create a new random training set of 10 examples of the exact same size as the original data set. The way we'll do so is we're reaching and pick out one random training example. Then we put it back into the bag, and then again randomly pick out one training example. You pick again and again and again. Notice now this fifth training example is identical to the second one that we had out there. But that's fine. You keep going and keep going, and we get another repeats the example, and so on and so forth. Until eventually you end up with 10 training examples, some of which are repeats. You notice also that this training set does not contain all 10 of the original training examples, but that's okay. The process of sampling with replacement lets you construct a new training set that's a little bit similar to, but also pretty different from your original training set.

![image](https://user-images.githubusercontent.com/73081144/194737781-6d445289-a193-415f-8378-88da7850eac7.png)

*Fig. 11. Sampling with replacement.*

Now that we have a way to use something with replacement to create new training sets that are a bit similar to but also quite different from the original training set. We're ready to build our first tree ensemble algorithm. Here is the process of building a **bagged decision trees**:

- given training set of size m:
  - for $b = 1$ to $B$:
    - use sampling with replacement to create a new training set of size $m$;
    - train a decision tree on the new dataset. 

Here, $B$ is the number of trees. Typical number of trees is $64 < B < 128$. After training, you use all trees to vote.

![image](https://user-images.githubusercontent.com/73081144/194738006-5222cf76-d3f3-4c93-8441-a53a3570f5ac.png)

*Fig. 12. Bagged random forest.*

To create a **random forest** classifier, at each node, when choosing a feature to use to split, if $n$ features are available, pick a random, subset of $k < n$ feature and allow the algorithm to only choose from thta subset of features. Basically, you **randomize feature choice**. So in other words, you would pick $K$ features as the allowed features and then out of those $K$ features choose the one with the highest information gain as the choice of feature to use the split. The typical choice of $K = \sqrt{n}$

## Boosted Trees / eXtreme Gradient Boosting (XGBoost)

XGBoost build procedure:

- given training set of size m:
  - for $b = 1$ to $B$:
    - use sampling with replacement to create a new training set of size $m$;
      - **but instead of picking from all examples with equal $(1/m)$ probability, make it more likely to pick misclassified examples from previously trained trees.** This is called **deliberate practice**.
    - train a decision tree on the new dataset. 

The boosting procedure will do this for a total of B times where on each iteration, you look at what the ensemble of trees for trees $1, 2$ up through $(b- 1)$, are not yet doing that well on. And when you're building tree number b, you will then have a higher probability of picking examples that the ensemble of the previously sample trees is still not yet doing well on.

XGBoost is superior to other decision tree algorithms.

## When to Use Decision Trees

- works well on tabular (structred) data;
- not recommended for unstructured data (images, audio, text);
- they are fast to train, so evaluating, debugging and diagnostics loop is fast to iterate through;
- small decision trees may be human interpretable.
