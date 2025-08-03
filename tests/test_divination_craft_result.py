import pyautogui

REGIONS = {
    "stash": (15, 120, 650, 630),
    "inventory": (1270, 590, 340, 260),
    "horticrafting_divination_stack": (947, 427, 13, 13),
    "expensive_card": (1795, 590, 110, 260),
}
FOLDER_PATHS = {
    "pictures": {
        "imperial_legacy": {
            "horticrafting": r"C:\Users\jasmi\Desktop\programming_2024\python\poe\auto_craft\assets\pictures\divination_cards\imperial_legacy\horticrafting",
        },
        "the_immortal": {
            "horticrafting": r"C:\Users\jasmi\Desktop\programming_2024\python\poe\auto_craft\assets\pictures\divination_cards\the_immortal\horticrafting",
            "inventory": r"C:\Users\jasmi\Desktop\programming_2024\python\poe\auto_craft\assets\pictures\divination_cards\the_immortal\inventory",
        },
    },
    "logs": r"C:\Users\jasmi\Desktop\programming_2024\python\poe\auto_craft\logs",
    "pattern_history": r"C:\Users\jasmi\Desktop\programming_2024\python\poe\auto_craft\logs\pattern_history",
}
LOGS = {"crafts": "crafts.txt", "current_craft_result": "current_craft_result.txt"}

STARTING_POSITIONS = {
    "inventory": {
        "first_slot": {"x": 1300, "y": 615},
    },
    "horticrafting": {
        "craft_button": {"x": 970, "y": 610},
        "crafting_slot": {"x": 970, "y": 450},
    },
}
FILE_NAMES = {
    "craft_results": "craft_results.txt",
    "expensive_card": "the_immortal_5.png",
}
PIXEL_SIZES = {"inventory": {"slot": 53}}

DIVINATION_CARDS = {
    "imperial_legacy": {"stack_size": 22},
    "the_immortal": {"stack_size": 10},
}


PATTERNS = [
    [-1, -1, -1, 1, 1, -1],
    [1, -1, -1, -1, 1, 1],
    [1, -1, 1, -1, -1, 1],
    [1, 1, -1, 1, 1, 1],
    [1, -1, 1, 1, 1, 1],
]

import sys
import os

# Step back to parent folder
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(parent_dir)

from utility.get_divination_craft_result import get_divination_craft_result

divination_craft_result = get_divination_craft_result(
    folder=FOLDER_PATHS["pictures"]["imperial_legacy"]['horticrafting'],
    stack_size=DIVINATION_CARDS["imperial_legacy"]["stack_size"],
)

pyautogui.moveTo(1795, 590)