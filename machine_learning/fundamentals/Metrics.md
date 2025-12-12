# Metrics

Metrics are used to evaluate your algorithm's perfomance.

### Unbalanced, Skewed Datasets

One of the most common evaluation metrics used in unbalanced classification is ROC AUC. However, some people claim that when the data set is highly imbalanced, ROC AUC is not a suitable metric and a good alternative would be the area under the precision-recall curve (PR AUC), especially when dealing with high dimensional data in which the positive class, i.e, anomalies, is more important than the negative class, i.e., normal points. Nonetheless, no single evaluation metric dominates others; therefore, both ROC AUC and PR AUC can be used for evaluation

By raising prediction threshold in skewed datasets, you end up with higher precision, but lower recall.

When lowering prediction threshold, you end up with lower precision, but higher recall.

### Precision

Precision is the fraction of *true positives* to *all positives*, where *all positives* $=$ *true positives* $+$ *false positives*.

```
def precision(y_true, y_pred):

    """Precision metric.

    Only computes a batch-wise average of precision.

    Computes the precision, a metric for multi-label classification of
    how many selected items are relevant.
    """

    true_positives = K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))
    predicted_positives = K.sum(K.round(K.clip(y_pred, 0, 1)))
    precision = true_positives / (predicted_positives + K.epsilon())

    return precision
```

### Recall

Recall is the fraction of *true positives* to *actual positives*, where *actual positives* $=$ *true positives* $+$ *false negatives*.

![image](https://user-images.githubusercontent.com/73081144/193480110-b8f3c4c0-86b3-4539-9f83-6042703b2028.png)

*Fig. 1. Precision and recall.*

![image](https://user-images.githubusercontent.com/73081144/193480656-cf0eaf63-3cf2-4e8e-8982-b3dbeeaa3bd4.png)


*Fig. 2. Precision recall tradeoff.*

```
def recall(y_true, y_pred):

    """Recall metric.

    Only computes a batch-wise average of recall.

    Computes the recall, a metric for multi-label classification of
    how many relevant items are selected.
    """

    true_positives = K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))
    possible_positives = K.sum(K.round(K.clip(y_true, 0, 1)))
    recall = true_positives / (possible_positives + K.epsilon())

    return recall
```

### F1 Score

The F1 score can be interpreted as a harmonic mean of the precision and recall, where an F1 score reaches its best value at 1 and worst score at 0. It is useful to combine precision and recall into one metric to help choose the best algorithm. F1 score gives us a way to tradeoff precision and recall.

![image](https://user-images.githubusercontent.com/73081144/193480943-ba56972f-5f78-45e8-afe8-e04e3d901b38.png)

*Fig. 3. F1 score.*

```
def f1(y_true, y_pred, activation):

    if activation==None:
    
        y_pred = sigmoid(y_pred) # use if dense has no activation function

    precisionScore = precision(y_true, y_pred)
    recallScore = recall(y_true, y_pred)

    f1 = 2 * ((precisionScore * recallScore) / (precisionScore + recallScore + K.epsilon()))
    
    return f1
```

## Segmentation Metrics

### IoU and Dice Score

- *Area of Overlap = sum(True Positives - pixel correctly classified)* (intersection) 
- *Combined area - total pixels in predicted segmentation mask + total pixels in true segmentation mask* 
- *Area of union - total pixels in predicted segmentation mask + total pixels in true segmentation mask* - area of overlap 
- *Intersection Over Union (IoU) - area of overlap / area of union (evaluates worst case perfomance)* 
- *Dice Score - 2 x (area of overlap / combined area)* (evaluates average perfomance).

```
def segmentation_IoU_DiceScore(y_true, y_pred):
  '''
  Computes IOU and Dice Score.

  Args:
    y_true (tensor) - ground truth label map
    y_pred (tensor) - predicted label map
  '''
  
  class_wise_iou = []
  class_wise_dice_score = []

  smoothening_factor = 0.00001

  for i in range(12):
      
    intersection = np.sum((y_pred == i) * (y_true == i))
    y_true_area = np.sum((y_true == i))
    y_pred_area = np.sum((y_pred == i))
    combined_area = y_true_area + y_pred_area
    
    iou = (intersection + smoothening_factor) / (combined_area - intersection + smoothening_factor)
    class_wise_iou.append(iou)
    
    dice_score =  2 * ((intersection + smoothening_factor) / (combined_area + smoothening_factor))
    class_wise_dice_score.append(dice_score)

  return class_wise_iou, class_wise_dice_score
```
