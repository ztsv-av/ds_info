# K-Means

K-means is a clustering algorithm. The goal of K-means ('K' stands for number of clusters, or centroids) algorithm is to group similar data points into clusters and detect underlying patterns. K-means is a center-based clustering algorithm. This algorithm uses distance between points (that is values of their features) as a measure of similarity. The objective is to minimize the sum of distances of the points to their respective centroid.

K-means will repeatedly do two different things:
1. assign points to cluster centroids;
2. move cluster centroids.

The first thing that the K-means algorithm does is it will take a random guess at where might be the centers of the two clusters that you might ask it to find. For example, it might take these two points as random centers.

![image](https://user-images.githubusercontent.com/73081144/196016615-b9512548-3b9a-4d03-bb10-b78594d31461.png)

*Fig. 1. K-means first random center pick.*

Then, it will go through each of these points, look at whether it is closer to the red cross or to the blue cross and assign each point to its closest centroid (step 1).

![image](https://user-images.githubusercontent.com/73081144/196016713-eb9a40b6-bd95-48ef-b424-377ecf5d47ca.png)

*Fig. 2. K-means step 1: assigning poits to groups.*

After assigning points, it will look at every point in each group and take an average of them. It will move the centoid of each group to whatever is the average location of that group based on the assigned points related to it.

![image](https://user-images.githubusercontent.com/73081144/196016759-77339ad3-b767-46ca-b2ea-e24b49638c16.png)

*Fig. 3. K-means step 2: recomputing centroids.*

Finally, we will repeat steps 1 and 2 until there are no more changes to either the assignment of the points to the centroids or cluster centroids locations.

*Note: if there are no examples assigned to a cluster, then eliminate that cluster.*

![image](https://user-images.githubusercontent.com/73081144/196016822-b68e995c-8dc0-4ab2-83e7-6152d89ef175.png)

*Fig. 4. Final clusters.*

## K-means Algorithm and Math

1. Randomly initialize $K$ cluster centroids $\mu_1, \mu_2, ..., \mu_K$, where the dimension of $\mu_K$ equal to the dimension of a training example.
2. Repeat:
   1. Assign points to cluster centroids:
      - for $i=1$ to $m$:
        - $c^{(i)}:=$ index (from 1 to $K$) to cluster centroid closest to $x^{(i)}$ by computing distance between a point and every cluster: 
          - $dist_{x^{(i)}, \mu_k}=min_k||x^{(i)} - \mu_k||^2$
    2. Move cluster centroids:
         - for $k=1$ to $K$:
           - $\mu_k:=$ average (mean) of points assigned to cluster $k$:
             - $\mu_k=\frac{\sum_{i=1}^jx^{(i)}_k}{N_k}$ , where 
               - $x^{(i)}_k=x^{(i)}$'s example assigned to $k$'s centoid
               - $N_k=$ number of examples assigned to $k$'s centoid.

## K-means Optimization Objective

- $c^{(i)} =$ index of cluster $(1,2,...,K)$ to which example $x^{(i)}$ is currently assigned;
- $\mu_k=$ cluster centroid $k$;
- $\mu_{c^{(i)}}=$ cluster cenriod of cluster to which example $x^{(i)}$ has been assigned.

**Cost function**:

$$J(c^{(1)}, ..., c^{(m)}, \mu_1, ..., \mu_k)=\frac{1}{m}\sum^m_{i=1}||x^{(i)} - \mu_{c^{(i)}}||^2$$

This cost function is sometimes called *distortion*.

The first part of K-means where you assign points to cluster centroid. K-means is updating $c^{(1)}$ through $c^{(m)}$ to try to minimize the cost function $J$ as much as possible while holding $\mu_1$ through $\mu_k$ fixed. And the second step, in contrast where you move the cluster centroid, it is leaving $c^{(1)}$ through $c^{(m)}$ fixed, but updates $\mu_1$ through $\mu_k$ to try to minimize the cost function or the distortion as much as possible.

![image](https://user-images.githubusercontent.com/73081144/196017701-4aa883de-04af-458a-a403-404ac2edfb41.png)

*Fig. 5. Reducing cost function by assigning a point to closest centoid.*

![image](https://user-images.githubusercontent.com/73081144/196017722-096c6fb8-25ee-46b8-8a5d-2e74fa6c7648.png)

*Fig. 6. Reducing cost function by moving centoid to the center of a cluster by averaging.*

So, K-means is trying to find assignments of points of cluster centroids as well as find locations of clusters centroid that minimizes the squared distance.

## Random Cluster Initialization

Randomly pick $K$ training examples and set $\mu_1, \mu_2, ..., \mu_k$ equal to these $K$ examples. 

This technique might sometimes badly initialize first centroids, which will lead to bad clusters.

So, to avoid bad centroids, run K-means algorithm multiple times and pick one with the lowest cost function.

![image](https://user-images.githubusercontent.com/73081144/196017917-992b7d1a-1796-47f9-a79e-44b8e3fa55fc.png)

*Fig. 7. Choosing best clusters by comparing cost functions.*

![image](https://user-images.githubusercontent.com/73081144/196017950-4a2507db-6479-4ab4-b539-63234fcafe39.png)

*Fig. 8. Random initialization algorithm.*

## Choosing the Number of Clusters K

One way to try to choose the value of K is called the **elbow method**.

![image](https://user-images.githubusercontent.com/73081144/196018026-fe60431c-bdcd-48c2-bd62-43373a6dab0f.png)

*Fig. 8. Elbow method.*

However, the right 'K' is ofter ambigous. **Don't choose $K$ just to minimize cost $J$, because you will almost always just choose the largest $K$**.

Second way is to evaluate K-means based on how well it perfroms on the task you use it.

![image](https://user-images.githubusercontent.com/73081144/196018262-76a4a076-688f-4196-abcf-2b1686ca3296.png)

*Fig. 9. Choosing K.*
