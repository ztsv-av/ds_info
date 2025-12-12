# **Autoencoders**

What are *autoencoders*?  
&nbsp;&nbsp;&nbsp;&nbsp; - neural networks capable of learning dense representations of input data without supervision (training data not labeled);  
&nbsp;&nbsp;&nbsp;&nbsp; - useful for dimensionality reduction and for visualization;  
&nbsp;&nbsp;&nbsp;&nbsp; - can be used to generate new data that resembels input data;  
&nbsp;&nbsp;&nbsp;&nbsp; - in practice they:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; a. copy input to output;  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; b. learn efficient ways to represent data. 

&nbsp;  

## **Basic Autoencoder Architecture**
In autoencoders, the number of inputs and output neurons should match. For example, if we have x1, x2 and x3, then then we should have 3 neurons, where each produces y1, y2 and y3 respectively. However, the number of neurons in encoder and decoders cannot match! Otherwise, there will be a straith path from inputs to outputs and no pattern to represent data will be learned. This network representation is called *under complete*. Also, when training the network, you feed it the same data as x_train and y_train.  

&nbsp;

### **Basic architecture:**   
&nbsp;&nbsp;&nbsp;&nbsp; - *Inputs*: X1, X2, X3;  

&nbsp;&nbsp;&nbsp;&nbsp; - Layer that takes inputs and encodes the latent representation of the input data - 2 neurons (turn 3D input data into 2D encoded data) - *Encoder*;  

&nbsp;&nbsp;&nbsp;&nbsp; - Layer that takes latent representation of input data, decodes it and turns it into an output - 3 neurons (turn 2D encoded data into 3D decoded, approximated representation of input data) - *Decoder*;  

&nbsp;&nbsp;&nbsp;&nbsp; - *Outputs*: Y1, Y2, Y3.

&nbsp;  

# **Deep autoencoders**
## **Stacked Autoencoders**
Stacked autoencoder architecture can be used to achieve encoding and decoding for more complex images. They are usually more accurate than shallow autoencoders. A bottleneck layer - the shallowest layer in the network - is used to get more features but without further reducing the dimension afterwards.  

&nbsp;  

### **Stacked Autoencoder Architecture:**  
&nbsp;&nbsp;&nbsp;&nbsp; - *Inputs*: X1, X2, X3, X4, X5;  

&nbsp;&nbsp;&nbsp;&nbsp; - *Encoder:*  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - 4 neurons;  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - 3 neurons.  

&nbsp;&nbsp;&nbsp;&nbsp; - *Bottleneck* - 2 neurons;  

&nbsp;&nbsp;&nbsp;&nbsp; - *Decoder:*  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - 3 neurons;  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - 4 neurons.  

&nbsp;&nbsp;&nbsp;&nbsp; - *Output* - reconstructed input.

&nbsp;  

## **Convolutional Autoencoders**
It is known that convolutional neural networks are better for computer vision. Thereby, convolutional autoencoders work better than just DNN autoencoders. Notice we don't flatten the images. This is because CNNs can deal with 2D arrays. 

&nbsp;

### **Convolutional Autoencoder Architecture:**  
&nbsp;&nbsp;&nbsp;&nbsp; - *Input* (28x28x1);  

&nbsp;&nbsp;&nbsp;&nbsp; - *Encoder:*  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - CONV2D(filters=64) + POOLING(2x2) (28x28x64);  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - CONV2D(filters=128) + POOLING(2x2) (14x14x128).  

&nbsp;&nbsp;&nbsp;&nbsp; - *Bottleneck:*  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - CONV2D(filters=256) (7x7x256); 

&nbsp;&nbsp;&nbsp;&nbsp; - *Decoder:*  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - CONV2D(filters=128) + UPSAMPLING(2x2) (14x14x128);  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - CONV2D(filters=64) + UPSAMPLING(2x2) (28x28x64);  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - CONV2D(filters=1) (28x28x1) (1x1 convolution?).  

&nbsp;&nbsp;&nbsp;&nbsp; - *Output* - reconstructed input.

&nbsp;

# **Variational Autoencoders**
Variational autoencoders are a type of autoencoders, but instead of generating reconstructed input, they create completely new data. This is achievied by adding noise to the output of the encoder in the bottleneck layer. In other words, VAE changes the latent space to be a combination of the learned values of the encoder with a *Gaussian distribution*, so that future values could be predicted from the same distribution (*Gaussian distribution* is used to sample latent encoding pseudo randomly OR gives a level of random noise in probability instead of just a learned feature from the encoder). This would require some architectural changes. The encoder should output standart deviation $\sigma$ and a mean $\mu$ that would be used to build a latent representation of the data (this would be learned by a network, not calculated manually).

&nbsp;

### **Variational Autoencoder Architecture:**  
&nbsp;&nbsp;&nbsp;&nbsp; - *Input* (28x28x1);  

&nbsp;&nbsp;&nbsp;&nbsp; - *Encoder:*  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - CONV2D(filters=32, strides=2) + BATCH_NORM (14x14x32);  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - CONV2D(filters=64, strides=2) + BATCH_NORM (7x7x64)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  - *Output* - BATCH_2_SHAPE (7x7x64).  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - FLATTEN;  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - DENSE + BATCH_NORM;  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - *Output:*  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  - Dense $\mu$ (mean);  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  - Dense $\sigma$ (standart deviation).  
&nbsp;&nbsp;&nbsp;&nbsp; - *Sampling Layer (can be viewed as a part of the encoder):*  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Calculate *epsilon* $\epsilon$ - random normal Gaussian distribution in the desired shape (batch, dim);  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - *Output $z$* - 
$$z = \mu + \exp(0.5 \cdot \sigma) \cdot \epsilon$$
&nbsp;&nbsp;&nbsp;&nbsp; - *Full Encoder Output:*  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - BATCH_2_SHAPE;  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - $\mu$;  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - $\sigma$;  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - *z*.  

&nbsp;&nbsp;&nbsp;&nbsp; - *Decoder:*  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Calculate number of neurons from BATCH_2_SHAPE:      
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; UNITS = BATCH_2_SHAPE[1] $\cdot$ BATCH_2_SHAPE[2] $\cdot$ BATCH_2_SHAPE[3] = 7 $\cdot$ 7 $\cdot$ 64  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - DENSE(UNITS) + BATCH_NORM;  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - RESHAPE(BATCH_2_SHAPE[1], BATCH_2_SHAPE[2], BATCH_2_SHAPE[3]) (7x7x64);  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - CONV2D_TRANSPOSE(filters=64, strides=2) + BATCH_NORM (14x14x64);  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - CONV2D_TRANSPOSE(filters=32, strides=2) + BATCH_NORM (28x28x32);  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - CONV2D_TRANSPOSE(filters=1, strides=1) (28x28x1);    

&nbsp;&nbsp;&nbsp;&nbsp; - *Output* - randomly reconstructed input.

&nbsp;

### **Variational Autoencoder Loss Function**
With variational autoencoders *Kullback-Leibler* cost function is normally used.
```
def kl_reconstruction_loss(inputs, outputs, mu, sigma):

    kl_loss = 1 + sigma - tf.square(mu) - tf.math.exp(sigma)

    return tf.reduce_mean(kl_loss) * -0.5
```

Still, in gradients calculation we use binary cross entropy loss + KL loss to get total loss. The binary cross entropy loss function still works for training the MNIST VAE because it gives the minimum value when the prediction is equal to the ground truth. In this case, that would be when outputs == inputs. Unlike binary classification problems though where the ground truth is only either 0 or 1, this minimum value won't necessarily be equal to 0 because the normalized MNIST pixel values are in the range [0, 1].

&nbsp;

### **VAE Model Definition in Code**
```
def vae_model(encoder, decoder, input_shape):

    inputs = tf.keras.layers.Input
    (shape=input_shape)

    mu, sigma, z = encoder(inputs)

    reconstructed = decoder(z)

    model = tf.keras.Model(inputs=inputs, outputs=reconstructed)

    loss = kl_reconstruction_loss(inputs, z, mu, sigma)
    model.add_loss(loss)

    return model

```

### Vector-Quantized Variational Auto-Encoders

State of the art. TODO