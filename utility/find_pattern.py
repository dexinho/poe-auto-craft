import os
from utility.config import (
    LOGS,
    FOLDER_PATHS,
    PATTERN_RULES,
)
from utility.manage_file import read_file, clear_file


def find_pattern():
    cheap_craft_results_file_path = os.path.join(
        FOLDER_PATHS["logs"], LOGS["cheap_craft_results"]
    )

    cheap_crafts_data = read_file(file_path=cheap_craft_results_file_path)
    cheap_crafts = list(map(int, cheap_crafts_data.strip().split()))

    if len(cheap_crafts) < 1:
        return False

    cheap_crafts_sum = sum(cheap_crafts)

    if cheap_crafts_sum >= PATTERN_RULES["threshold"]:
        return True
    elif cheap_crafts_sum < PATTERN_RULES["stop_loss"]:
        clear_file(file_path=cheap_craft_results_file_path)

    return False
