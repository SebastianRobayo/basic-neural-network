import tensorflow as tf
import numpy as np

celsius = np.array([-40, -10, 0, 8, 15, 22, 38], dtype=float)
fahrenheit = np.array([-40, 14, 32, 46, 59, 72, 100], dtype=float)

# neural network setup
layer = tf.keras.layers.Dense(units=1, input_shape=[1])
model = tf.keras.Sequential([layer])

# compiling the model
model.compile(
    optimizer=tf.keras.optimizers.Adam(0.1),
    loss='mean_squared_error'
)

# model training
print('training begins...')
record = model.fit(celsius, fahrenheit, epochs=600, verbose=False)
print('trained model')

# graph
import matplotlib.pyplot as plt
plt.xlabel('#Epoch')
plt.ylabel("Magnitude of loss")
plt.plot(record.history["loss"])

# prediction result
print("Let's make a prediction!")
result = model.predict([290.0])
print("The result is " + str(result) + " fahrenheit")

# internal variables of the model
print("Internal variables of the model")
print(layer.get_weights())