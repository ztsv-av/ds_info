# Image Segmentation architecture:
#   The architecture usually consists of Convolutional Encoder-Decoder.
#   -Encoder:
#       CNN without fully connected layers;
#       Aggregates low level features to high level features (to decoder)
#   -Decoder:
#       Replaces fully connected layers in a CNN;
#       Up samples image to original size to generate a pixel mask.
#   The input in Image Segmentation models are images with specific shape, e.x. 224x224x3
#   The output in those models are images with original shape, where channel dimension equals number of classes, 
#       e.x. 224x224xN, where N - number of classes

# Fully Convolutional Neural Network Architecture (most of the Image Segmentation models are based on this):
#   Encoder:
#      -Popular encoder architectures:
#          VGG-16;
#          Resnet-50;
#          MobileNet.
#      -Reuse convolutional layers for feature extraction (do not reuse fully connected layers)
#   Decoder:
#       FCN-32s;
#       FCN-16s;
#       FCN-8s.
#   Architecture:
#       FCN-32:
#           Encoder (Down Sampling):
#               Image (32x32) -> Pool 1 -> Pool 2 -> Pool 3 -> Pool 4 -> Pool 5
#           Decoder (Up Sampling):
#               32 x Upsampled Prediction (stride size 32), which is the output - pixel vise prediction of classes
#       FCN-16:
#           Encoder (Down Sampling):
#               Image (32x32) -> Pool 1 -> Pool 2 -> Pool 3 -> Pool 4 -> Pool 5
#           Decoder (Up Sampling):
#               From Pool 5 -> 2x Upsampled Prediction (1x1 -> 4x4)
#               From Pool 4 -> 1x1 Conv Layer to Pool 4 Prediction (4x4 -> 4x4)
#                   Summation of two prediction layers
#                       16 x Upsampled Prediction (stride size 16), which is the output - pixel vise prediction of classes
#       FCN-8:
#           Encoder (Down Sampling):
#               Image (32x32) -> Pool 1 -> Pool 2 -> Pool 3 -> Pool 4 -> Pool 5
#           Decoder (Up Sampling):
#               From Pool 5 -> 2x Upsampled Prediction (1x1 -> 4x4)
#               From Pool 4 -> 1x1 Conv Layer to Pool 4 Prediction (4x4 -> 4x4)
#                   Summation of two prediction layers                  
#                   From Pool 3 -> 1x1 Conv Layer to Pool 3 Prediction (8x8 -> 8x8)
#                       Summation of summated prediction with Pool 3 Prediction
#                           8 x Upsampled Prediction (stride size 16), which is the output - pixel vise prediction of classes


# Famous Image Segmentation architectures:
# Predict segmentation masks for each instance of a class in the image
#   -SegNet:
#       Input - RGB Image
#       Convolutional Encoder-Decoder:
#           2 x (Conv + Batch Normalization + RELU) + 1 x Pooling (decrease shape)
#           2 x (Conv + Batch Normalization + RELU) + 1 x Pooling (decrease shape)
#           3 x (Conv + Batch Normalization + RELU) + 1 x Pooling (decrease shape)
#           3 x (Conv + Batch Normalization + RELU) + 1 x Pooling (decrease shape)
#           3 x (Conv + Batch Normalization + RELU) + 1 x Pooling
#           1 x Upsampling + 3 x (Conv + Batch Normalization + RELU) (increase shape)
#           1 x Upsampling + 3 x (Conv + Batch Normalization + RELU) (increase shape)
#           1 x Upsampling + 3 x (Conv + Batch Normalization + RELU) (increase shape)
#           1 x Upsampling + 2 x (Conv + Batch Normalization + RELU) (increase shape)
#           1 x Upsampling + 2 x (Conv + Batch Normalization + RELU) + 1 x Softmax Dense Layer
#       Output - Segmented Image
#   -UNet (look at architecture somewhere else, but the principle or encoder-decoder remains the same)
#   -Mask R-CNN (instance segmentation):
#       architecture that predicts class, boxes (builds of Faster R-CNN w/ ResNet (Object Detection)) and adds aditional layers for a segmentation of an image)

# Instance Segmentation
# This means that aside from the bounding boxes, the model is also able to predict segmentation masks for each instance of a class in the image
#   -Mask R-CNN (expensive to train)
#   Has 2 stage pipeline:
#       1) generate region proposals for objects in the image using technique called
#           RoIAlign (region of interest align)
#       2) predict class of the object within the bounding boxes as well as pixel level mask
#           based on this class.
#           There are 2 CONV layers here: first, for feature extraction (ResNet of Inception) (also predicts bounding box?), 
#           and second one final feature map used for classifiying pixels for segmentation