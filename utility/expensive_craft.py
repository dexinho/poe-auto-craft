import pyautogui
import math

from utility.find_expensive_card import find_expensive_card
from utility.move_item import move_item
from utility.horticraft import horticraft
from utility.get_divination_craft_result import get_divination_craft_result
from utility.config import (
    FOLDER_PATHS,
    DIVINATION_CARDS,
    STARTING_POSITIONS,
    CARDS_USED,
    REGIONS,
    FILE_NAMES,
)
from utility.radnom_pause import random_pause

def expensive_craft():
    expensive_card_name = CARDS_USED["expensive_card"]
    max_retries = 10

    pyautogui.moveTo(100, 1000) # so it doesn't cover the inventory card
    
    found_expensive_card = find_expensive_card(
        region=REGIONS["expensive_card"],
        folder=FOLDER_PATHS["pictures"][expensive_card_name]["inventory"],
        image_name=FILE_NAMES["expensive_card"],
    )

    if not found_expensive_card["is_found"]:
        print("Expensive card not found on screen.")
        exit()

    move_item(
        x=found_expensive_card["position"]["x"], y=found_expensive_card["position"]["y"]
    )

    default_result = int(DIVINATION_CARDS[expensive_card_name]["stack_size"] / 2)
    attempts = 0

    while True:
        if attempts >= max_retries:
            print(f"Reached max retries ({max_retries}). Exiting.")
            exit()

        horticraft()
        random_pause(0.3, 0.5)

        result = int(
            get_divination_craft_result(
                folder=FOLDER_PATHS["pictures"][expensive_card_name]["horticrafting"],
                stack_size=DIVINATION_CARDS[expensive_card_name]["stack_size"],
            )
        )

        print(f"Attempt {attempts + 1}: Result = {result}")
        attempts += 1

        if result != default_result:
            break

    pyautogui.moveTo(
        STARTING_POSITIONS["horticrafting"]["crafting_slot"]["x"],
        STARTING_POSITIONS["horticrafting"]["crafting_slot"]["y"],
    )
    pyautogui.click()

    pyautogui.moveTo(
        found_expensive_card["position"]["x"], found_expensive_card["position"]["y"]
    )
    pyautogui.click()

    return result
