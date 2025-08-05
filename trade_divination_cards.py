import sys
import pyautogui
import time
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from utility.config import (
    STARTING_POSITIONS,
    PIXEL_SIZES,
    FOLDER_PATHS,
    FILE_NAMES,
    REGIONS,
    SCRIPT_SPEED,
)
from utility.move_item import move_item
from utility.find_image import find_image
from utility.radnom_pause import random_pause

pyautogui.PAUSE = 0.02


def trade_card():
    trade_button_x = STARTING_POSITIONS["divination_card_trade"]["trade_button"]["x"]
    trade_button_y = STARTING_POSITIONS["divination_card_trade"]["trade_button"]["y"]
    pyautogui.moveTo(trade_button_x, trade_button_y)
    pyautogui.click()


def get_traded_result():
    card_slot_x = STARTING_POSITIONS["divination_card_trade"]["card_slot"]["x"]
    card_slot_y = STARTING_POSITIONS["divination_card_trade"]["card_slot"]["y"]
    move_item(card_slot_x, card_slot_y)


def trade_divination_cards(rows, cols):
    print("moving from inventory")
    script_speed = SCRIPT_SPEED["super_fast"]
    slot_size = PIXEL_SIZES["inventory"]["slot"]
    start_x = STARTING_POSITIONS["inventory"]["first_slot"]["x"]
    start_y = STARTING_POSITIONS["inventory"]["first_slot"]["y"]

    divination_card_trade_logo = find_image(
        region=REGIONS["divination_card_trade"]["logo"],
        folder=FOLDER_PATHS['images']["divination_card_trade"],
        image_name=FILE_NAMES["divination_card_trade"]["logo"],
    )

    if not divination_card_trade_logo["is_found"]:
        exit()

    for j in range(cols):
        for i in range(rows):
            x = start_x + j * slot_size
            y = start_y + i * slot_size
            move_item(x, y)
            time.sleep(script_speed)
            trade_card()
            time.sleep(script_speed)
            get_traded_result()
            time.sleep(script_speed)


rows = int(input("Rows: "))
cols = int(input("Cols: "))
trade_divination_cards(rows=rows, cols=cols)
