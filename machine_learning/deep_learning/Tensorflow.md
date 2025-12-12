# Tensorflow

## tf.Variable

*tf.Variable()* is used to store values of parameters we want to optimize. Remember that they require special functions to modify their contents. *tf.Variable()* example:

```
w = tf.Variable(3.0)
x = 1.0
alpha = 0.01

w.assign_add(-alpha * x)
```

## Updating Gradients / tf.GradientTape

To compute gradients in Tensorflow, use *.GradientTape()* method. By writing forward propagation steps inside *.GradientTape()* method, Tensorflow will automatically compute backward propagation steps using *.gradient()* method, i.e. correct sequence of operations to compute the cost. After computing derivatives, you can update parameters. *.GradientTape()* example:

```
w = tf.Variable(3.0)
x = 1.0
y = 1.0
alpha = 0.01

iterations = 30
for iter in range(iterations):  # run gradient descent for *iterations* iterations
    # use .GradientTape() to record steps
    #   used to compute the cost J to enable autodifferentiation
    with tf.GradientTape() as tape:
        fwb = w*x
        costJ = (fwb - y)**2
    
    # use .GradientTape().gradient to calculate gradients
    #   of the cost with respect to parameter w
    [dJdw] = tape.gradient(costJ, [w])

    # run gradient descent step
    #   by updating w to reduce the cost
    w.assign_add(-alpha * dJdw)
```
