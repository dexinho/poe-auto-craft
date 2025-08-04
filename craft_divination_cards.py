import pyautogui
import os
import math
from utility.config import (
    DIVINATION_CARDS,
    FOLDER_PATHS,
    LOGS,
    PIXEL_SIZES,
    STARTING_POSITIONS,
    CARDS_USED,
    PATTERN_RULES,
)
from utility.get_divination_craft_result import get_divination_craft_result
from utility.manage_file import update_file, read_file, clear_file
from utility.move_item import move_item
from utility.horticraft import horticraft
from utility.expensive_craft import expensive_craft
from utility.radnom_pause import random_pause
from utility.find_pattern import find_pattern

pyautogui.PAUSE = 0.05


def craftDivinationCards():
    rows, cols = 5, 10
    total_slots = rows * cols
    starting_pos = input("Start at which position: ")
    pos = int(starting_pos) - 1
    cheap_card_name = CARDS_USED["cheap_card"]
    expensive_card_name = CARDS_USED["expensive_card"]

    pyautogui.click(1000, 1200)  # focus the game

    for current_pos in range(pos, total_slots):
        is_pattern_found = find_pattern()

        if is_pattern_found:
            expensive_craft_result = expensive_craft()
            card_stack_difference = math.ceil(
                (
                    DIVINATION_CARDS[cheap_card_name]["stack_size"]
                    - DIVINATION_CARDS[expensive_card_name]["stack_size"]
                )
                // 2
            )

            update_file(
                file_path=os.path.join(
                    FOLDER_PATHS["logs"], LOGS["expensive_craft_results"]
                ),
                value=expensive_craft_result
                - DIVINATION_CARDS[expensive_card_name]["stack_size"] // 2,
            )

            update_file(
                file_path=os.path.join(FOLDER_PATHS["logs"], LOGS["craft_results"]),
                value=expensive_craft_result + card_stack_difference,
            )

            update_file(
                file_path=os.path.join(
                    FOLDER_PATHS["logs"], LOGS["latest_expensive_crafts"]
                ),
                value=expensive_craft_result,
            )

            expensive_craft_data = read_file(
                file_path=os.path.join(
                    FOLDER_PATHS["logs"], LOGS["expensive_craft_results"]
                )
            )

            expensive_crafts_data = list(map(int, expensive_craft_data.strip().split()))
            expensive_crafts_sum = 0
            if len(expensive_crafts_data) > 0:
                expensive_crafts_sum = sum(
                    list(map(int, expensive_craft_data.strip().split()))
                )

            if (
                expensive_crafts_sum >= PATTERN_RULES["positive_net_limit"]
            ) or expensive_crafts_sum <= PATTERN_RULES["negative_net_limit"]:
                clear_file(
                    file_path=os.path.join(
                        FOLDER_PATHS["logs"], LOGS["cheap_craft_results"]
                    )
                )

                clear_file(
                    file_path=os.path.join(
                        FOLDER_PATHS["logs"], LOGS["expensive_craft_results"]
                    )
                )
            else:
                current_pos -= 1
                continue

        row = current_pos // cols
        col = current_pos % cols

        move_item(
            x=STARTING_POSITIONS["inventory"]["first_slot"]["x"]
            + col * PIXEL_SIZES["inventory"]["slot"],
            y=STARTING_POSITIONS["inventory"]["first_slot"]["y"]
            + row * PIXEL_SIZES["inventory"]["slot"],
        )

        horticraft()

        random_pause(0.3, 0.4)

        cheap_divination_craft_result = get_divination_craft_result(
            folder=FOLDER_PATHS["images"][cheap_card_name]["horticrafting"],
            stack_size=DIVINATION_CARDS[cheap_card_name]["stack_size"],
        )

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

        if (
            cheap_divination_craft_result
            == DIVINATION_CARDS[cheap_card_name]["stack_size"] // 2
        ):
            continue

        update_file(
            file_path=os.path.join(FOLDER_PATHS["logs"], LOGS["craft_results"]),
            value=cheap_divination_craft_result,
        )

        update_file(
            file_path=os.path.join(FOLDER_PATHS["logs"], LOGS["cheap_craft_results"]),
            value=cheap_divination_craft_result
            - DIVINATION_CARDS[cheap_card_name]["stack_size"] // 2,
        )


craftDivinationCards()
