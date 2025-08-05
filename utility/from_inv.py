import sys
import pyautogui
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from utility.config import STARTING_POSITIONS, PIXEL_SIZES


def from_inv(rows=5, cols=12):
    pyautogui.PAUSE = 0.02
    pyautogui.keyDown("ctrl")
    print('moving from inventory')

    slot_size = PIXEL_SIZES["inventory"]["slot"]
    start_x = STARTING_POSITIONS["inventory"]["first_slot"]["x"]
    start_y = STARTING_POSITIONS["inventory"]["first_slot"]["y"]

    for j in range(cols):
        for i in range(rows):
            x = start_x + j * slot_size
            y = start_y + i * slot_size
            pyautogui.moveTo(x, y)
            pyautogui.click()

    pyautogui.keyUp("ctrl")

from_inv()