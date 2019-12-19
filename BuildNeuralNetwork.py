"""
BuildNeuralNetwork
    Image_array is 16x4x4
    2-3 Dense Layers
    Flatten it to 256 Neurons
    at the end 3x1 or 2x1 Q-Table depending if duck is included or not
"""

import keras.layers as Layers
import keras.optimizers as Optimizers
from keras import Sequential

IMG_COL = 16
IMG_ROW = 4
IMG_FLOW = 4


def createNewSeqModel():
    """
    create the neural network model (input layer, 2x hidden dense layer with 64 neurones each and output layer)
    :return: model
    """
    model = Sequential()
    weights = 'random_uniform'
    model.add(Layers.Flatten(input_shape=(IMG_FLOW, IMG_ROW, IMG_COL)))
    model.add(Layers.Dense(64, activation='relu', kernel_initializer=weights))
    model.add(Layers.Dense(64, activation='relu', kernel_initializer=weights))
    model.add(Layers.Dense(3, activation='linear', kernel_initializer=weights))
    model.compile(Optimizers.adam(), loss='mse')
    return model
