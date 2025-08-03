import pyautogui

from utility.config import STARTING_POSITIONS, PIXEL_SIZES
from utility.move_item import move_item
from utility.focus_game import focus_game
from utility.radnom_pause import random_pause


def get_stacked_deck():
    move_item(
        x=STARTING_POSITIONS["stash"]["currency"]["stacked_deck"]["x"],
        y=STARTING_POSITIONS["stash"]["currency"]["stacked_deck"]["y"],
    )


def pull_card():
    pyautogui.PAUSE = 0.04
    pyautogui.moveTo(
        STARTING_POSITIONS["inventory"]["first_slot"]["x"],
        STARTING_POSITIONS["inventory"]["first_slot"]["y"],
    )
    pyautogui.rightClick()


def open_stacked_decks(amount):
    focus_game()
    pyautogui.PAUSE = 0.01
    stacked_deck_stack_size = 20
    amount_of_stacked_deck_stacks = amount // 20
    print(amount_of_stacked_deck_stacks)
    second_inventory_slot_position = {
        "x": STARTING_POSITIONS["inventory"]["first_slot"]["x"]
        + PIXEL_SIZES["inventory"]["slot"],
        "y": STARTING_POSITIONS["inventory"]["first_slot"]["y"],
    }
    for _ in range(amount_of_stacked_deck_stacks):
        get_stacked_deck()
        random_pause(0.1, 0.2)
        for _ in range(stacked_deck_stack_size):
            pull_card()
            pyautogui.moveTo(
                second_inventory_slot_position["x"], second_inventory_slot_position["y"]
            )
            pyautogui.click()
            move_item(
                x=second_inventory_slot_position["x"],
                y=second_inventory_slot_position["y"],
            )


open_stacked_decks(amount=5000)
