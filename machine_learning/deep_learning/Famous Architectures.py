# VGG-19:
#   Input: 224 x 224 x 3
#   BLOCK 1:
#      Depth 64 (filters?)
#      3x3 Convolutions
#         CONV1_1 + ReLU
#         CONV1_2 + ReLU (224 x 224 x 64)
#         MAX_POOL_1 (cut size by half)
#   BLOCK 2:
#      Depth 128 (filters?)
#      3x3 Convolutions
#         CONV2_1 + ReLU
#         CONV2_2 + ReLU (112 x 112 x 128)
#         MAX_POOL_2 (cut size by half)
#   BLOCK 3:
#      Depth 256 (filters?)
#      3x3 Convolutions
#         CONV3_1 + ReLU
#         CONV3_2 + ReLU
#         CONV3_3 + ReLU
#         CONV3_4 + ReLU (56 x 56 x 256)
#         MAX_POOL_3 (cut size by half)
#   BLOCK 4:
#      Depth 512 (filters?)
#      3x3 Convolutions
#         CONV4_1 + ReLU
#         CONV4_2 + ReLU
#         CONV4_3 + ReLU
#         CONV4_4 + ReLU (28 x 28 x 512)
#         MAX_POOL_4 (cut size by half)
#   BLOCK 5:
#      Depth 512 (filters?)
#      3x3 Convolutions
#         CONV5_1 + ReLU
#         CONV5_2 + ReLU
#         CONV5_3 + ReLU
#         CONV5_4 + ReLU (14 x 14 x 512)
#         MAX_POOL_5 (cut size by half) (7 x 7 x 512)
#   FULLY CONNECTED LAYERS:
#      FC1 Dense + ReLU (1 x 1 x 4096)
#      FC2 Dense + ReLU (1 x 1 x 4096)
#      Softmax (1 x 1 x NUM_CLASSES)