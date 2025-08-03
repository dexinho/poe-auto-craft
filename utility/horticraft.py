import pyautogui
from utility.config import STARTING_POSITIONS


def horticraft():
    pyautogui.moveTo(
        x=STARTING_POSITIONS["horticrafting"]["craft_button"]["x"],
        y=STARTING_POSITIONS["horticrafting"]["craft_button"]["y"],
    )
    pyautogui.click()
