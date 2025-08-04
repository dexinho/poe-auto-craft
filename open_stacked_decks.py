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
        pyautogui.moveTo(
            x=STARTING_POSITIONS["inventory"]["first_slot"]["x"],
            y=STARTING_POSITIONS["inventory"]["first_slot"]["y"]
            + PIXEL_SIZES["inventory"]["slot"],
        )
        pyautogui.click()
        rows_occupied = 5
        cols_occupied = 5

        # if not is_inventory_empty(rows=rows_to_check, cols=cols_to_check):

        #     from_inv(rows=rows_to_check, cols=cols_to_check)

        # if not is_inventory_empty(rows=5, cols=12):
        #     exit()
        get_stacked_deck()
        random_pause(SCRIPT_SPEED["fast"], SCRIPT_SPEED["medium"])
        print(i)

        usable_cols = [1, 2, 3, 4]
        start_x = STARTING_POSITIONS["inventory"]["first_slot"]["x"]
        start_y = STARTING_POSITIONS["inventory"]["first_slot"]["y"]

        for j in range(min(stacked_deck_stack_size, 20)):  # only 4x4 slots used
            row = j // len(usable_cols)
            col_index = j % len(usable_cols)
            col = usable_cols[col_index]

            target_x = start_x + col * PIXEL_SIZES["inventory"]["slot"]
            target_y = start_y + row * PIXEL_SIZES["inventory"]["slot"]

            pull_card()

            pyautogui.moveTo(target_x, target_y, SCRIPT_SPEED["super_fast"])
            pyautogui.click()
            random_pause(SCRIPT_SPEED["super_fast"], SCRIPT_SPEED["super_fast"])

            random_pause(SCRIPT_SPEED["super_fast"], SCRIPT_SPEED["super_fast"])

        from_inv(rows=rows_occupied, cols=cols_occupied)


decks_to_open = int(input("How many decks to open: "))
for i in range(50):
    open_stacked_decks(amount=decks_to_open)
    random_pause(5, 10)
