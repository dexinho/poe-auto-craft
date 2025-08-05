import pyautogui
import time
from utility.radnom_pause import random_pause
from utility.focus_game import focus_game
from utility.find_image import find_image
from utility.move_items import move_all, move_from_inventory
from utility.config import (
    BAD_DIVINATION_CARDS,
    STARTING_POSITIONS,
    FOLDER_PATHS,
    FILE_NAMES,
    REGIONS,
    SCRIPT_SPEED,
)


def find_npc(npc_name):
    pyautogui.moveTo(
        STARTING_POSITIONS["npc"][npc_name]["x"],
        STARTING_POSITIONS["npc"][npc_name]["y"],
    )
    pyautogui.keyDown("ctrl")
    pyautogui.click()
    pyautogui.keyUp("ctrl")


def open_stash():
    pyautogui.moveTo(
        STARTING_POSITIONS["stash"]["x"],
        STARTING_POSITIONS["stash"]["y"],
    )
    pyautogui.click()


def accept_trade():
    pyautogui.moveTo(
        STARTING_POSITIONS["npc"]["shop"]["sell"]["accept_button"]["x"],
        STARTING_POSITIONS["npc"]["shop"]["sell"]["accept_button"]["y"],
        SCRIPT_SPEED["medium"],
    )
    pyautogui.click()


def find_card(card_name):
    filtered_name = f"^{card_name}$"
    pyautogui.keyDown("ctrl")
    pyautogui.press("f")
    pyautogui.keyUp("ctrl")
    pyautogui.typewrite(filtered_name)
    time.sleep(SCRIPT_SPEED["fast"])
    card_missing = find_image(
        folder=FOLDER_PATHS["images"]["stash"]["divination_tab"][
            "divination_card_not_found"
        ],
        image_name=FILE_NAMES["stash"]["divination_tab"]["divination_card_not_found"],
        region=REGIONS["stash"]["divination_tab"]["first_card"],
    )

    if card_missing["is_found"]:
        return None

    return True


def sell_bad_divination_cards(card_names_to_sell):
    focus_game()

    for card_name in card_names_to_sell:
        while True:
            open_stash()
            time.sleep(SCRIPT_SPEED["medium"])
            move_from_inventory(rows=5, cols=1)

            is_card_found = find_card(card_name)
            if not is_card_found:
                break

            move_all(
                x=STARTING_POSITIONS["stash"]["divination_tab"]["first_card"]["x"],
                y=STARTING_POSITIONS["stash"]["divination_tab"]["first_card"]["y"],
            )

            pyautogui.press("esc")
            find_npc("lilly_roth")
            time.sleep(SCRIPT_SPEED["fast"])
            move_from_inventory()
            accept_trade()
            time.sleep(SCRIPT_SPEED["fast"])
            pyautogui.press("esc")


sell_bad_divination_cards(BAD_DIVINATION_CARDS)
