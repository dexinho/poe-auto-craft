import pyautogui

from utility.radnom_pause import random_pause


def focus_game():
    pyautogui.PAUSE = 0.028
    pyautogui.moveTo(22, 22, 0.1)  # focus the game
    pyautogui.rightClick()
    random_pause(0.5, 1)
