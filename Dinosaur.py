"""
Dino(action)
    performs action decided in DecisionMaker.py and saved in action array
    check outcome (dead or not)
    restarts the game if dead
    return reward depending on dead or not
"""

import pyautogui
import time


def jump():
    """
    Jump over the obstacle
    :return: None
    """
    pyautogui.keyDown('up')


def unJump():
    """
    Stop pressing the jump key
    :return: None
    """
    pyautogui.keyUp('up')


def duck():
    """
    Get on the ground /!\ the dino stays down with this function
    :return: None
    """
    pyautogui.keyDown('down')


def unDuck():
    """
    Get the dino up
    :return: None
    """
    pyautogui.keyUp('down')


def restart():
    """
    restart the game when the dino is dead
    :return: None
    """
    restart_coords = (490, 465)
    pyautogui.click(restart_coords)


def checkState(arr):
    """
    Check if the dino is still running
    :parameter: arr, the 16x4 array of the last image
    :return: True if it does, False otherwise
    """
    alive = True
    if arr[1][7] < 200 and arr[2][7] < 200:
        alive = False
    return alive


def resetWebPage():
    """
    Refreshes the webpage
    :return: None
    """
    refresh_button_coords = (110, 75)
    pyautogui.click(refresh_button_coords)
    time.sleep(10)
    pyautogui.keyDown('up')
    pyautogui.keyUp('up')
    time.sleep(10)
