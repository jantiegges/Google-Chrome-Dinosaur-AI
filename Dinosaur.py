"""
Dino(action)
    performs action decided in DecisionMaker.py and saved in action array
    check outcome (dead or not)
    restarts the game if dead
    return reward depending on dead or not
"""

import pyautogui


def jump():
    """
    Jump over the obstacle
    :return: None
    """
    pyautogui.press('up')


def duck():
    """
    Get on the ground /!\ the dino stays down with this function
    :return: None
    """
    pyautogui.keyDown('down')


def unduck():
    """
    Get the dino up
    :return: None
    """
    pyautogui.keyUp('down')


def check_state(arr) :
    """
    Check if the dino is still running
    :parameter: arr, the 16x4 array of the last image
    :return: True if it does, False otherwise
    """
    alive = True
    if arr[1][7] < 200 and arr[2][7] < 200:
        alive = False
    return alive
