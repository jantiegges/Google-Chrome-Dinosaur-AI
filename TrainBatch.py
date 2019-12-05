"""
TrainBatch(batch_array)

"""
import numpy as np

def trainBatch(model, samples, labels):
    """
    Train the model on the training data samples with the result labels
    :return: None
    """
    epochs = 100        # epochs and bathcSize can be defined later
    batchSize = 50      # they should be defined to optimize learning speed
    model.fit(np.array(samples), np.array(labels),  epochs=epochs, batch_size=batchSize)
