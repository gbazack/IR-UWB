import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import numpy as np



#Create a sequential model with four (04) convolution layers
# To extract important features from the IR-UWB radar data
model= keras.Sequential([
    keras.Input(shape=(200, 1280, 1)), # 200x1280: size of radar image, 1: gray color
    layers.Conv2D(32, 5, activation="relu"),
    layers.Conv2D(32, 3, activation="relu"),
    layers.Conv2D(32, 3, activation="relu")
    layers.Conv2D(32, 3, activation="relu", name="last_layer")])
    
#Extraction of features from Convolution layers  
#extractor= keras.Model(inputs=model.inputs, outputs=[layer.output for layer in initial_model.layers])
extractor= keras.Model(inputs=model.inputs, outputs=model.get_layer(name='last_layer').output)

# Call feature extractor on test input.
x = tf.ones((1, 250, 250, 3))
features = feature_extractor(x)
