"""
DecisionMaker
    get Image Frame and resize it
        Image should be 16x4x4
    add image to image_array (consists of 4 images) and delete the oldest one
    give image_array to QTable --> get out highest value
    send action to Dinosaur(action) dependent on highest QValue --> get reward back
    compute the new q-value: new_value = (1 - alpha) * old_value + alpha * (reward + gamma * next_max)
        ### alpha = Learning_rate, gamma = Discount
    store image_array and neq q_value in batch_array
"""

from PIL import ImageGrab, ImageOps, Image
import numpy as np

IMG_COL = 16    # number of columns of the input image
IMG_ROW = 4     # number of rows of the input image

playing_area = (190, 420, 850, 510)


def getImage():
    """
    Checks the area to have obstacles
    :return: np array of the image
    """
    image = ImageGrab.grab(playing_area)
    gray_img = ImageOps.grayscale(image)
    img_block = gray_img.resize((IMG_COL, IMG_ROW), Image.LANCZOS)
    arr = np.array(img_block)
    return arr


def takeDecision(model, array):
    """
    return the prediction as a 3x1 vector with each value for going, jumping or ducking
    :parameter: model used, 16x4x4 array with the screen pixels values.
    :return: float 3x1 vector
    """
    return model.predict(array)
