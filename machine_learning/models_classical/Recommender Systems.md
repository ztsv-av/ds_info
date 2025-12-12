# Recommender Systems

A recommender system, or a recommendation system (sometimes replacing 'system' with a synonym such as platform or engine), is a subclass of information filtering system that provide suggestions for items that are most pertinent to a particular user. In a very general way, recommender systems are algorithms aimed at suggesting relevant items to users (items being movies to watch, text to read, products to buy or anything else depending on industries).

In the typical recommender system, you have some number of users as well as some number of items (e.g. movies). You might as well have features related to those items (e.g. how much a movie related to romance, action, etc. genres)

![image](https://user-images.githubusercontent.com/73081144/197675433-0c333adc-a344-4bb8-a285-75db5301df5b.png)

*Fig. 1. Recommendation task: movies.*

To predict user's $j$ rating, use **linear regression** model:

$$\hat{y}^{(j)} = w^{(j)} * x^{(i)} + b^{(j)}$$

## Cost function

Notation:

- $r(i, j) = 1$ if user $j$ has rated movie $i$ (0 otherwise);
- $y^{(i, j)} =$ rating given by user $j$ on movie $i$ (if defined);
- $w^{(j)}, b^{(j)} =$ parameters for user $j$;
- $x^{(i)} =$ feature vector for movie $i$;
- $m^{(j)} =$ number of movies rated by user $j$;
- $n =$ number of features.

For user $j$ and movie $i$, predict rating: $w^{(j)} * x^{(i)} + b^{(j)}$

To learn $w^{j}, b^{j}$ for a single user use **Mean Squared Error**:

$min_{w^{(j)}b^{(j)}}J(w^{(j)}, b^{(j)}) = \frac{1}{2m^{(j)}}\sum_{i:r(i,j)=1}(w^{(j)} * x^{(i)} + b^{(j)}-y^{(i, j)})^2  + \frac{\lambda}{2m^{(j)}}\sum_{k=1}^n(w_k^{(j)})^2$

You might remove $m^{(j)}$ term. It a constant and it does not affect cost function much.

So, overall cost function for all users looks like this:

$$J(w^{(1)}, ..., w^{(n_u)}, b^{(1)}, ..., b^{(n_u)}) = \frac{1}{2}\sum_{j=1}^{n_u}\sum_{i:r(i,j)=1}(w^{(j)} * x^{(i)} + b^{(j)}-y^{(i, j)})^2  + \frac{\lambda}{2}\sum_{j=1}^{n_u}\sum_{k=1}^n(w_k^{(j)})^2$$

The difference between simple linear regression model is that now we train different linear regression unit for each user.

## Collaborative Filtering Algorithm

Collaboratiove filtering algorithm is used to  **learn** **parameters** as well as **features**.

Given $w^{(1)}, ..., w^{(n_u)}, b^{(1)}, ..., b^{(n_u)}$, **cost function** to learn $x^{(1)}, ..., x^{(n_m)}$:

$J(x^{(1)}, ..., x^{(n_m)}) = \frac{1}{2}\sum_{i=1}^{n_m}\sum_{j:r(i,j)=1}(w^{(j)} * x^{(i)} + b^{(j)}-y^{(i, j)})^2  + \frac{\lambda}{2}\sum_{i=1}^{n_m}\sum_{k=1}^n(x_k^{(i)})^2$

Putting parameters and features cost functions together, we have a new cost function that we want to minimize, based on parameter values $w, b$ and features values $x$ for each user:

$$J(w, b, x) = \frac{1}{2}\sum_{(i, j):r(i,j)=1}(w^{(j)} * x^{(i)} + b^{(j)}-y^{(i, j)})^2  + \frac{\lambda}{2}\sum_{j=1}^{n_u}\sum_{k=1}^n(w_k^{(j)})^2 + \frac{\lambda}{2}\sum_{i=1}^{n_m}\sum_{k=1}^n(x_k^{(i)})^2$$

To minimize cost function, use **Gradient Descent**:

$repeat \space\{$

- $w_i^{(j)}=w_i^{(j)}-\alpha \frac{\partial}{\partial w_i^{(j)}}J(w,b,x)$

- $b^{(j)}=b^{(j)}-\alpha \frac{\partial}{\partial b^{(j)}}J(w,b,x)$
  
- $x_k^{(i)} = x_k^{(i)} - \alpha \frac{\partial}{\partial x_k^{(i)}}J(w,b,x)$

$\}$

### Limitations of Collaborative Filtering

- Not very good for cold start problems:
  - rank new items that few users have rated;
  - show something reasonable to new users who have rated few items.
- Difficult to use side information about items or users:
  - item: genre, movie stars, studio, etc.;
  - user: demographics (age, gender, location), expressed preferences, etc.

### Binary Labels

Possible recommender binary labels are: favorited, liked, clicked, engaged, etc.

Possible meaning of ratings:
- 1 - engaged after being shown;
- 0 - did not engage after being shown;
- ? - item not yet shown.

Example applications:
- did user $j$ purchase an item after being shown?
- did user $j$ fav/like an item?
- did user $j$ spend at least 30sec with an item?
- did user $j$ click on an item?

To generalize collaborative filtering algorithm from regression to binary classification we will predict a probability of $y^{(i, j)} = 1$ given by $g(w^{(j)} * x^{(i)} + b^{(j)}$, where $g(z) = \frac{1}{1+e^{-z}}$

**Binary cost function**:

$$J(w,b,x) = \sum_{(i, j):r(i,j)=1}L(f_{(w,b,x)}(x), y^{(i,j)}$$

, where

- $g(z) = \frac{1}{1+e^{-z}}$;
- $f_{w,b,x}(x) = g(w^{(j)} * x^{(i)} + b^{(j)})$;
- $L(f_{w,b,x}(x), y^{(i,j)}) = (-y^{(i,j)} \log(f_{w,b,x}( x ) ) - ( 1 - y^{(i,j)}) \log ( 1 - f_{w,b,x}( x ) )$

## Mean Normalization

In the case of building a recommended system with numbers $y$ such as movie ratings from one to five or zero to five stars, it turns out your algorithm will run more efficiently. And also perform a bit better if you first carry out mean normalization, that is if you normalize the movie ratings to have a consistent average value.

That way, when you dont have a user rating for a movie, you will not get weights ($w, b$) with 0 values and will not predict 0 user rating for a movie:

![image](https://user-images.githubusercontent.com/73081144/198196072-eccc33e6-26cc-4684-a506-f2a215356942.png)

*Fig. 2. Weights with 0 values and users with no ratings.*

In other words, mean normalization will cause no ratings to be equal to mean of ratings for a movie on a first iteration.

In order to carry out mean normalization, you subtract mean of one movie with every rating. The result becomes $y^{(i, j)}$:

![image](https://user-images.githubusercontent.com/73081144/198196179-46b4a04a-e1ed-40e7-a764-20c970073d31.png)

*Fig. 3. Mean normalization.*

In order not to predict negative values (e.g. movie ratings), add mean back to the linear function.

## Finding Related Items

To find an item $k$ related to an item $i$, just compare their features. In other words, find an item $x^{(k)}$ with features similar to $x^{(i)}$. To compare features, use **squared distance** between them:

$\sum^n_{l=1}(x_l^{(k)} - x_l^{(i)})^2$

or

$||x^{(k)} - x^{(i)}||^2$

## Content-based Filtering

Collaborative filtering recommends items based on ratings of users who gave similar ratings as you.

Content-based filtering **recommends** items **based on features of user and item** to find a good match.

Possible features:

1) user features $x_u^{(j)}$ for user $j$:
     - age;
     - gender;
     - country;
     - movies watched (e.g. 1000 most popular movies user watched);
     - average rating per genre;
     - ...
2) movie features $x_m^{(i)}$ for movie $i$:
     - year;
     - genre/genres;
     - reviews;
     - average rating;
     - ...

Feature vector sizes for user and movie can differ.

Predict rating of user $j$ on movie $i$ as:

$v^{(j)}_u * v^{(i)}_m$ , where:
- $v^{(j)}_u$ = user preferences - computed from $x^{(j)}_u$;
- $v^{(i)}_m$ = movie features - computed from $x^{(i)}_m$;

Notice we remoed $b^{(j)}$. Turns out bias just worsens the perfomance of an algorithm.

The challenge here is given $x^{(j)}_u$ and $x^{(i)}_m$ how we can compute $v^{(j)}_u$ and $v^{(i)}_m$ respectevely.

$v^{(j)}_u$ and $v^{(i)}_m$ are of the same size, because there is a dot-product between them.

With content-based filtering it is worth spending more time on **feature engineering**.

### Cost Function

Cost function for content-based filtering is as follows:

$$J = \sum_{(i, j):r(i,j)=1}(v_u^{(j)} \cdot v_m^{(i)} - y^{(i,j)})^2 + NN \space regularization$$

### Algorithm

To develop content-based filtering, we will use combined prediction of two neural networks: user and movie networks.

![image](https://user-images.githubusercontent.com/73081144/199142303-f58a32da-a0ed-4ad5-b9ba-1100e7a07471.png)

*Fig. 4. Content-based filtering neural networks.*

We can apply sigmoid function to the dot-product to predict the probability that $y^{(i,j)}$ is 1.

![image](https://user-images.githubusercontent.com/73081144/199143453-fa109850-63b4-4e89-9185-d5d45bf458c6.png)

*Fig. 5. Content-based filtering prediction process.*

Notice that both neural networks train at the same time. We're going to judge the two networks according to how well $v_u$ and $v_m$ predict $y^{(i,j)}$, and with this cost function, we're going to use gradient descent or some other optimization algorithm to tune the parameters of the neural network to cause the cost function J to be as small as possible. If you want to regularize this model, we can also add the usual neural network regularization term to encourage the neural networks to keep the values of their parameters small.

### Finding Similar Items

- $v^{(j)}_u$ - vector of length $m$ describing user $j$ with features $x^{(j)}_u$
- $v^{(i)}_m$ - vector of length $m$ describing movie $i$ with features $x^{(i)}_m$

Thereby, to find movies similar to movie $i$ take squared distance between movie vector and all other movie vectors: 

$min||v^{(k)}_m - v^{(i)}_m||^2$

*Note: this can be pre-computed ahead of time. You can run a compute server overnight to go through the list of all your movies and for every movie, find similar movies to it, so that tomorrow, if a user comes to the website and they're browsing a specific movie, you can already have pre-computed to 10 or 20 most similar movies to show to the user at that time.*

### Efficient Recommendations / Retrieval & Ranking

Recommender systems will sometimes need to pick a handful of items to recommend, from a catalog of thousands or millions or 10s of millions or even more items. How do you do this efficiently computationally?

If you feed 10s of millions movie/ads/songs/products feature vectors through neural network, it will take a lot of time to find the most relatable items to user preference.

For that, there is are two steps called **retrieval & ranking**.

![image](https://user-images.githubusercontent.com/73081144/199144223-e32fce54-397c-4345-aa0b-3ac0622d747c.png)

*Fig. 6. Retrieval step.*

The goal of retrieval step is to find a broad coverage of plausible item candidates related to user preference.

*For retrieval step 1) - find similar movies through precomputed lookup table.*

![image](https://user-images.githubusercontent.com/73081144/199144431-38077818-6710-457d-a68b-ca625fa53961.png)

*Fig. 7. Ranking step.*

In ranking step, take generated list through retrieval step and feed it into neural network to generate possible user ratings for this list of movies. Then, pick top $n$ movies and recommend them to user.

*If you computed $v_m$ for all the movies in advance, then all you need to do is to do inference on $x_u => v_u$ part of the neural network a single time to compute $v_u$. And then take that just computed $v_u$ for the user on your website right now. And take the inner product between $v_u$ and $v_m$ for the movies that you have retrieved during the retrieval step. So this computation can be done relatively quickly.*

- Retrieving more items results in better perfomance, but slower recommendations.
- To analyze/optimize the trade-off, carry out offline experiments to see if retrieving additional items results in more relevant recommendations (i.e. $p(y^{(i,j)}=1$ of items displayed to user are higher).
