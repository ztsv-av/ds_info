# Convolutional Neural Networks (CNNs)

Convolutional Neural Networks (CNNs) are a type of deep learning architecture widely used for tasks like image recognition, object detection, and video analysis. CNNs are particularly powerful because they automatically learn spatial hierarchies of features from input images through convolution operations. Unlike traditional fully connected neural networks, CNNs use convolutional layers to capture local patterns in data, allowing for more efficient and accurate analysis of visual information.

## Key Components of CNNs

- **Convolution Layer**: Applies filters (also called kernels) across the input image to extract features like edges, textures, or more complex patterns. The filter slides over the image with a specified stride.
- **Pooling Layer**: Reduces the dimensionality of the feature maps, retaining only the most important information. This helps reduce computational complexity and control overfitting.
- **Activation Function**: Introduces non-linearity into the network, commonly using ReLU (Rectified Linear Unit) to speed up learning and improve model performance.
- **Fully Connected Layers**: After feature extraction, these layers map the high-level features to the final output (e.g., class labels in classification tasks).

---

## Stride and Pooling in CNNs

The **stride** controls how much the filter shifts as it slides over the input image. A smaller stride means more detailed processing since the filter moves by smaller increments. Conversely, a larger stride means faster, less detailed processing.

**Pooling** reduces the size of the feature map by selecting the maximum (Max Pooling) or average (Average Pooling) value within a specific window, such as 2x2, over the feature map. Pooling helps retain important information while lowering the spatial dimensions, which reduces computational load and helps avoid overfitting.

For example, with a 2x2 pooling window and a 2x2 stride window, the height and width of the feature map will be halved.

Given the following matrix:

$$
\begin{bmatrix}
1 & 2 \\
2 & 1 \\
0 & 1 \\
0 & 1 \\
\end{bmatrix}
$$

Applying 2x2 pooling with a stride of 2x2, we take the maximum value from each 2x2 block. The pooled output will be:

$$
\begin{bmatrix}
\max(1, 2, 2, 1) \\
\max(0, 1, 0, 1) \\
\end{bmatrix}
=
\begin{bmatrix}
2 \\
1 \\
\end{bmatrix}
$$

The result is a smaller matrix, halving both the height and width.

---

# Upsampling in CNNs

**Upsampling** is used to increase the spatial dimensions of a feature map, commonly in tasks like image generation or segmentation.

### In TensorFlow:

- **Simple Scaling (`UpSampling2D`)**: Upscales an image by duplicating pixel values.
    - **Nearest**: Copies the value from the nearest pixel.
    - **Bilinear**: Uses a weighted average of nearby pixels for smoother scaling.
    - Example: `size = (2, 2)` turns each pixel into a 2x2 block.

- **Transposed Convolution (Deconvolution)**: Reverses the convolution operation to upsample the image. It uses learned filters to create a refined version of the upscaled image, but some information loss can occur due to previous downsampling layers.

For instance, consider an input feature map:

$$
\begin{bmatrix}
0 & 64 & 128 \\
48 & 192 & 144 \\
142 & 226 & 168 \\
\end{bmatrix}
$$

After applying a transposed convolution, the output might approximate the original values with some adjustments:

$$
\begin{bmatrix}
-1 & 0 & -2 \\
0.5 & 4.5 & -1.5 \\
1.5 & 2 & -3 \\
\end{bmatrix}
$$

If you use a 1x1 filter with a stride of 2x2, this filter does not alter the original values but helps in upsampling the image size by increasing its resolution.
