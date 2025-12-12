# IMAGE SEGMENTATION
# Area of Overlap = sum(True Positives - pixel correctly classified) (intersection)
# Combined area - total pixels in predicted segmentation mask +
#   total pixels in true segmentation mask
# Area of union - total pixels in predicted segmentation mask + 
#   total pixels in true segmentation mask - area of overlap
# Intersection Over Union (IoU) - area of overlap / area of union (evaluates worst case perfomance)
# Dice Score - 2 x (area of overlap / combined area) (evaluates average perfomance)

# Unbalanced Classification
# One of the most common evaluation metrics used
# in unbalanced classification is ROC AUC; however, some people
# claim that when the data set is highly imbalanced, ROC
# AUC is not a suitable metric and a good alternative
# would be the area under the precision-recall curve (PR
# AUC), especially when dealing with high dimensional
# data in which the positive class, i.e, anomalies, is more
# important than the negative class, i.e., normal points.
# Nonetheless, no single evaluation metric dominates others;
# therefore, both ROC AUC and PR AUC can be used for evaluation

import tensorflow.keras.backend as K
from tensorflow.keras.activations import sigmoid

import numpy as np


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

def f1(y_true, y_pred):
    
    y_pred = sigmoid(y_pred) # use if dense has no activation function

    precisionScore = precision(y_true, y_pred)
    recallScore = recall(y_true, y_pred)
    
    return 2 * ((precisionScore * recallScore) / (precisionScore + recallScore + K.epsilon()))