import pyautogui

from utility.config import (
    STARTING_POSITIONS,
    PIXEL_SIZES,
    REGIONS,
    FOLDER_PATHS,
    FILE_NAMES,
    SCRIPT_SPEED,
)
from utility.move_item import move_item
from utility.focus_game import focus_game
from utility.radnom_pause import random_pause
from utility.find_image import find_image
from utility.is_inventory_empty import is_inventory_empty
from utility.from_inv import from_inv


def get_stacked_deck():
    image_name = FILE_NAMES["stacked_deck"]
    image_result = find_image(
        region=REGIONS["currency_tab_extra_slots_area"],
        image_name=image_name,
        folder=FOLDER_PATHS["images"]["currency"],
    )

    if image_result["is_found"]:
        move_item(
            x=image_result["position"]["x"],
            y=image_result["position"]["y"],
        )
    else:
        print(image_name, "not found on the screen!")
        exit()


def pull_card():
    pyautogui.moveTo(
        STARTING_POSITIONS["inventory"]["first_slot"]["x"],
        STARTING_POSITIONS["inventory"]["first_slot"]["y"],
    )
    pyautogui.rightClick()


def open_stacked_decks(amount):
    focus_game()
    stash_logo_result = find_image(
        folder=FOLDER_PATHS["images"]["stash"]["logo"],
        image_name=FILE_NAMES["stash_logo"],
        region=REGIONS["stash_logo"],
    )
    if not stash_logo_result["is_found"]:
        exit()

    stacked_deck_stack_size = 20
    amount_of_stacked_deck_stacks = amount // 20
    second_inventory_slot_position = {
        "x": STARTING_POSITIONS["inventory"]["first_slot"]["x"]
        + PIXEL_SIZES["inventory"]["slot"],
        "y": STARTING_POSITIONS["inventory"]["first_slot"]["y"],
    }
    for i in range(amount_of_stacked_deck_stacks):
        rows_to_check = 2
        cols_to_check = 2
        if not is_inventory_empty(rows=rows_to_check, cols=cols_to_check):
            pyautogui.moveTo(
                x=STARTING_POSITIONS["inventory"]["first_slot"]["x"]
                + PIXEL_SIZES["inventory"]["slot"],
                y=STARTING_POSITIONS["inventory"]["first_slot"]["y"]
                + PIXEL_SIZES["inventory"]["slot"],
            )
            pyautogui.click()
            from_inv(rows=rows_to_check, cols=cols_to_check)

            # if not is_inventory_empty(rows=5, cols=12):
            #     exit()
        get_stacked_deck()
        random_pause(SCRIPT_SPEED["medium"], SCRIPT_SPEED["slow"])
        print(i)
        for j in range(stacked_deck_stack_size):
            pull_card()
            pyautogui.moveTo(
                second_inventory_slot_position["x"],
                second_inventory_slot_position["y"],
                SCRIPT_SPEED["fast"],
            )
            pyautogui.click()
            random_pause(SCRIPT_SPEED["fast"], SCRIPT_SPEED["fast"])
            move_item(
                x=second_inventory_slot_position["x"],
                y=second_inventory_slot_position["y"],
            )
            random_pause(SCRIPT_SPEED["fast"], SCRIPT_SPEED["fast"])


decks_to_open = int(input("How many decks to open: "))
for i in range(30):
    open_stacked_decks(amount=decks_to_open)
    random_pause(5, 10)
