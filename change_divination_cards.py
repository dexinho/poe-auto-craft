import pyautogui
import os

from utility.config import STARTING_POSITIONS, PIXEL_SIZES, FOLDER_PATHS, FILE_NAMES
from utility.move_item import move_item
from utility.horticraft import horticraft
from utility.radnom_pause import random_pause
from utility.focus_game import focus_game

MIN_RANDOM = 0.2
MAX_RANDOM = 0.3


def change_divination_cards(card_name, stack_size):
    focus_game()
    image_path = os.path.join(
        FOLDER_PATHS["pictures"]["stash"]["logo"], FILE_NAMES["stash_logo"]
    )
    pyautogui.locateOnScreen(image=image_path, confidence=0.8)

    pyautogui.keyDown("ctrl")
    pyautogui.press("f")
    pyautogui.keyUp("ctrl")

    pyautogui.typewrite(card_name)
    random_pause(MIN_RANDOM, MAX_RANDOM)
    rows, cols = 5, 12
    total_slots = rows * cols

    slot_size = PIXEL_SIZES["inventory"]["slot"]
    start_x = STARTING_POSITIONS["inventory"]["first_slot"]["x"]
    start_y = STARTING_POSITIONS["inventory"]["first_slot"]["y"]

    for i in range(0, total_slots, stack_size):  # Go in steps of 6 slots
        # Click on the divination card
        pyautogui.moveTo(
            STARTING_POSITIONS["stash"]["divination_cards"]["first_card"]["x"],
            STARTING_POSITIONS["stash"]["divination_cards"]["first_card"]["y"],
        )
        pyautogui.click()

        # Place into 6 slots
        for j in range(stack_size):
            slot_index = i + j
            if slot_index >= total_slots:
                break  # avoid overflow

            row = slot_index // cols
            col = slot_index % cols
            pyautogui.keyDown("shift")
            pyautogui.moveTo(
                x=start_x + col * slot_size,
                y=start_y + row * slot_size,
            )
            pyautogui.click()
            pyautogui.keyUp("shift")

    pyautogui.press("esc")

    random_pause(MIN_RANDOM, MAX_RANDOM)

    pyautogui.moveTo(
        STARTING_POSITIONS["horticrafting"]["x"],
        STARTING_POSITIONS["horticrafting"]["y"],
        MIN_RANDOM,
    )
    pyautogui.click()
    random_pause(MIN_RANDOM, MAX_RANDOM)

    pyautogui.keyDown("ctrl")
    pyautogui.press("f")
    pyautogui.keyUp("ctrl")
    pyautogui.typewrite("change a divination")
    random_pause(MIN_RANDOM, MAX_RANDOM)
    pyautogui.moveTo(
        STARTING_POSITIONS["horticrafting"]["first_crafting_option"]["x"],
        STARTING_POSITIONS["horticrafting"]["first_crafting_option"]["y"],
    )
    pyautogui.click()
    pyautogui.PAUSE = 0.045

    rows, cols = 5, 12
    total_slots = rows * cols
    for current_pos in range(0, total_slots):
        row = current_pos // cols
        col = current_pos % cols

        move_item(
            x=STARTING_POSITIONS["inventory"]["first_slot"]["x"]
            + col * PIXEL_SIZES["inventory"]["slot"],
            y=STARTING_POSITIONS["inventory"]["first_slot"]["y"]
            + row * PIXEL_SIZES["inventory"]["slot"],
        )

        horticraft()
        random_pause(0.01, 0.01)
        pyautogui.moveTo(
            STARTING_POSITIONS["horticrafting"]["crafting_slot"]["x"],
            STARTING_POSITIONS["horticrafting"]["crafting_slot"]["y"],
        )
        pyautogui.click()

        pyautogui.moveTo(
            STARTING_POSITIONS["inventory"]["first_slot"]["x"]
            + col * PIXEL_SIZES["inventory"]["slot"],
            STARTING_POSITIONS["inventory"]["first_slot"]["y"]
            + row * PIXEL_SIZES["inventory"]["slot"],
        )
        pyautogui.click()

        pyautogui.keyUp("ctrl")

    pyautogui.press("esc")
    random_pause(MIN_RANDOM, MAX_RANDOM)

    pyautogui.moveTo(
        STARTING_POSITIONS["stash"]["x"], STARTING_POSITIONS["stash"]["y"], MIN_RANDOM
    )
    pyautogui.click()

    random_pause(MIN_RANDOM, MAX_RANDOM)
    pyautogui.PAUSE = 0.018

    rows, cols = 5, 12
    total_slots = rows * cols
    for current_pos in range(0, total_slots):
        row = current_pos // cols
        col = current_pos % cols

        move_item(
            x=STARTING_POSITIONS["inventory"]["first_slot"]["x"]
            + col * PIXEL_SIZES["inventory"]["slot"],
            y=STARTING_POSITIONS["inventory"]["first_slot"]["y"]
            + row * PIXEL_SIZES["inventory"]["slot"],
        )


# for i in range(0, 31):
#     change_divination_cards(card_name='metals', stack_size=6)

for i in range(0, 22):
    change_divination_cards(card_name="the lover", stack_size=2)
