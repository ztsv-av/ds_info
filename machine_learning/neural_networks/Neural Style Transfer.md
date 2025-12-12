# **Neural Style Transfer**
Neural style transfer is an algorithm that takes a pair of images - style image and content image, combines them and creates a stylized image. There are *3* approaches to Style Transfer:
### 1. **Supervised learning**:
&nbsp;&nbsp;&nbsp;&nbsp; - Pairs: original & stylized (manually created) images;  
&nbsp;&nbsp;&nbsp;&nbsp; - It needs lots of pairs!  
&nbsp;&nbsp;&nbsp;&nbsp; - So, you teach a model how to stylize an image.
### 2. **Neural Style Transfer**:
&nbsp;&nbsp;&nbsp;&nbsp; - Uses pre-trained model;  
&nbsp;&nbsp;&nbsp;&nbsp; - Inputs: a single pair of images:  
&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; - Extract style from image 1;  
&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; - Extract content from image 2.  
&nbsp;&nbsp;&nbsp;&nbsp; - Generate image to match style and content;  
&nbsp;&nbsp;&nbsp;&nbsp; - In a loop: minimize loss of generated image with respect to the style of image 1 and content of image 2;  
&nbsp;&nbsp;&nbsp;&nbsp; - You use loss minimization to merge the style and the content into the generated image;
### 3. **Fast Neural Style Transfer**:
&nbsp;&nbsp;&nbsp;&nbsp; - Faster version of Neural Style Transfer.

&nbsp;  

## **Neural Style Transfer Process Explained**
We start with the image that we want to transform and we call this the content image. 
Then there's the image that gives us the style that we want to convert our image into - style image. 
From these, we'll create a new image that we'll call the generated image. 
It would be created over many iterations initially looking very much like the content image but over time it will take on the attributes of the style image.  
Using a pre-trained CNN, for example, VGG-19, we can extract the content features from the content image. 
We'll represent these features as the last block in the network (last COVN2D block I think - features), and the style is also extracted by using a pre-trained CNN. 
Style information can be extracted from every layer in the network, and this is represented by the arrows coming out of each block in the network diagram. 
We'll then initialize our generated image from the content image.   
The model can compare the generated image with the content image by calculating what's called a content loss. 
On every iteration, it checks how much of the original content is present in the generated image. 
As you can imagine on the first iteration, the content loss will be close or equal to zero depending on the initialization of the pre-trained CNN. 
Over several iterations the content loss may increase as the generated image is modified to incorporate the style information. 
Now, this might seem counterintuitive, but increasing the content loss is actually a good thing 
because that would indicate that there are differences between the generated image and the original content image. 
The loss would be zero if they were identical. 
But of course, you don't want the loss to get too high or you'd lose the features and attributes of the original image.   
Similarly, you want to reduce the style loss because we'd like some of its attributes to be in the generated image. 
It's ultimately a BALANCING game. 
The algorithm also compares the generated image with the style image using a metric called the style loss. 
The style loss is calculated by comparing each layer of the CNNs for both the generated image and the style image. 
The style loss ends up being an average loss across the multiple layers that are being compared. 
In early iterations, as the images are very different, the style loss will be very high, 
but the goal is to reduce it over time as the generated image incorporates more of the style information. 
You can imagine that you'd want a generated image to keep the overall loss low.   
You can combine the style loss with the content loss to get a total loss. 
Given this information, we can use an optimizer to update the generated image to get a new generated image whose total loss is lower. 
If you recall how you can use gradients in an optimizer to update each layer of a neural network, you can apply a very similar concept here to updating the input image. 
Which should make the generated image into something closer to a merged image between the two input images. 
We'll repeat the process comparing the generated image against the style image to get a style loss and also comparing the generated image against the content image to get a content loss. 
Adding the two losses into a total loss, and then optimizing to reduce the overall total loss.   
Now notice that WE ARE NOT TRAINING this network. 
It's being used to extract the content and style information from the images. 
But the process is quite similar to network training in that you iteratively calculate and minimize a loss through a loss function and then apply what you've learned using an optimizer to get new data.   
Note that while I'm showing three networks here, there's really only one network. 
I'm just splitting into three like this to make it easier to illustrate.

### *Remember that lower layer features define style of the image, higher layer features (complex) define content of the image.*

&nbsp;  

### **VGG-19 for Style Extraction:**
&nbsp;&nbsp;&nbsp;&nbsp; - VGG-19 has 16 CONV + MAX_POOL blocks.  
&nbsp;&nbsp;&nbsp;&nbsp; - To effectively extract style, use 1st CONV layer in each CONV block
(CONV1_1, CONV2_1, CONV3_1, CONV4_1, CONV5_1)
### **VGG-19 for Contect Extraction:**
&nbsp;&nbsp;&nbsp;&nbsp; - VGG-19 has 16 CONV + MAX_POOL blocks.  
&nbsp;&nbsp;&nbsp;&nbsp; - To effectively extract content, use only last CONV layer - CONV5_4  
&nbsp;&nbsp;&nbsp;&nbsp; - BUT it last layer isn't always the best one to use, because filters
reduces image to very small images containing extracted feautures.
Choosing a layer positioned a little before the last layer will work well.
For example, choose CONV5_2 or experiment.

&nbsp;

## **Total Loss**
$$L_{total}(\vec{p}, \vec{a}, \vec{x}) = \alpha * L_{content}(\vec{p}, \vec{x}) + \beta * L_{style}(\vec{a}, \vec{x})$$
&nbsp;&nbsp;&nbsp;&nbsp; $L_{total}$ - total loss,    
&nbsp;&nbsp;&nbsp;&nbsp; $L_{content}$ - content loss,  
&nbsp;&nbsp;&nbsp;&nbsp; $L_{style}$ - style loss,  
&nbsp;&nbsp;&nbsp;&nbsp; $\alpha$ - content weight,  
&nbsp;&nbsp;&nbsp;&nbsp; $\beta$ - style weight,  
&nbsp;&nbsp;&nbsp;&nbsp; $\vec{p}$ - content image (original photograph),  
&nbsp;&nbsp;&nbsp;&nbsp; $\vec{x}$ - generated image initialized to input image,  
&nbsp;&nbsp;&nbsp;&nbsp; $\vec{a}$ - style image.

&nbsp;  

### **Content Loss**
&nbsp;&nbsp;&nbsp;&nbsp; - generated image - content image = element-wise subtraction;  
&nbsp;&nbsp;&nbsp;&nbsp; - then do element-wise square;  
&nbsp;&nbsp;&nbsp;&nbsp; - then do reduce sum to get a scalar value;  
&nbsp;&nbsp;&nbsp;&nbsp; - then apply weight.  
$$L_{content}(\vec{p}, \vec{x}, l) = \frac{1}{2} \cdot \sum_{i, j}(F_{i,j}^{l} - P_{i,j}^{l})^2$$
&nbsp;&nbsp;&nbsp;&nbsp; - $L_{content}$ - content loss,  
&nbsp;&nbsp;&nbsp;&nbsp; - $F_{i,j}^{l}$ - content representation of generated image x in layer l (activation of ith feature map at position j in layer l of generated image),  
&nbsp;&nbsp;&nbsp;&nbsp; - $P_{i,j}^{l}$ - content representation of content image p in layer l
(activation of ith feature map at position j in layer l of content image).  

&nbsp;  

### **Style Loss**
&nbsp;&nbsp;&nbsp;&nbsp; Concept is the same as in content loss.
$$E_{l} = \frac{1}{(4 \cdot N_{l}^2 \cdot M_{l}^2)} * \sum_{i,j}(G_{i,j}^{l} - A_{i,j}^{l})^2$$
&nbsp;&nbsp;&nbsp;&nbsp; - $E_{l}$ - loss at layer l,  
&nbsp;&nbsp;&nbsp;&nbsp; - l - layer,  
&nbsp;&nbsp;&nbsp;&nbsp; - $A_{i,j}^{l}$ - style representation (*gram matrix*) of features for a single layer of style image a,  
&nbsp;&nbsp;&nbsp;&nbsp; - $G_{i,j}^{l}$ - style representation (*gram matrix*) of features for a single layer of generated image x,  
&nbsp;&nbsp;&nbsp;&nbsp; - $\frac{1}{(4 \cdot N_{l}^2 \cdot M_{l}^2)}$ = $\frac{1}{(2 \cdot h \cdot w \cdot f)^2}$ - weight,  
&nbsp;&nbsp;&nbsp;&nbsp; - $N_{l}$ - number of filters,  
&nbsp;&nbsp;&nbsp;&nbsp; - $M_{l}$ - filter size (h $\cdot$ w)
       
&nbsp;  

## **Total Variation Loss**
&nbsp;&nbsp;&nbsp;&nbsp; - Decreases high frequence artifacts;  
&nbsp;&nbsp;&nbsp;&nbsp; - Explicit regularization term on high frequency components.  
&nbsp;  
Basically, it removes noise that was presented by styling the image, i.e. smoothes out the image.  
&nbsp;  
To use it in code:
```
def calculate_gradients(image, content_targets, style_targets_style_weight, content_weight, with_regularization=False):

   total_variation_weight = 30

   with tf.GradientTape as tape:
      if with_regularization:
         loss += total_variation_weight * tf.image.total_variation(image)

   gradients = tape.gradient(loss, image)

   return gradients
```

&nbsp; 

## **Steps to Develop Neural Style Transfer:**
   1. Preprocess content & style images;
   2. Load pre-trained model, define loss functions;
   3. Loop:  
&nbsp;&nbsp;&nbsp;&nbsp;        - Optimize and generate new image;  
&nbsp;&nbsp;&nbsp;&nbsp;        - Visualize outputs.