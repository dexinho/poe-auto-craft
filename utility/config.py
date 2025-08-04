import pyautogui
from pathlib import Path
from utility.scale_resolution import scale_coordinates, scale_region

display_width, display_height = pyautogui.size()
DISPLAY_SETTINGS = {
    "reference_width": 1920,
    "reference_height": 1080,
    "display_width": display_width,
    "display_height": display_height,
}

BASE_PATH = Path(__file__).resolve().parent.parent
FOLDER_PATHS = {
    "images": {
        "imperial_legacy": {
            "horticrafting": BASE_PATH
            / "assets"
            / "images"
            / "divination_cards"
            / "imperial_legacy"
            / "horticrafting",
            "inventory": BASE_PATH
            / "assets"
            / "images"
            / "divination_cards"
            / "imperial_legacy"
            / "inventory",
        },
        "the_immortal": {
            "horticrafting": BASE_PATH
            / "assets"
            / "images"
            / "divination_cards"
            / "the_immortal"
            / "horticrafting",
            "inventory": BASE_PATH
            / "assets"
            / "images"
            / "divination_cards"
            / "the_immortal"
            / "inventory",
        },
        "the_apothecary": {
            "horticrafting": BASE_PATH
            / "assets"
            / "images"
            / "divination_cards"
            / "the_apothecary"
            / "horticrafting",
            "inventory": BASE_PATH
            / "assets"
            / "images"
            / "divination_cards"
            / "the_apothecary"
            / "inventory",
        },
        "stash": {"logo": BASE_PATH / "assets" / "images" / "stash"},
        "currency": BASE_PATH / "assets" / "images" / "currency",
        "inventory": BASE_PATH / "assets" / "images" / "inventory",
    },
    "logs": BASE_PATH / "logs",
    "pattern_history": BASE_PATH / "logs" / "pattern_history",
    "models": BASE_PATH / "models",
}

LOGS = {
    "cheap_craft_results": "cheap_craft_results.txt",
    "latest_expensive_crafts": "latest_expensive_crafts.txt",
    "expensive_craft_results": "expensive_craft_results.txt",
    "craft_results": "craft_results.txt",
}


REGIONS = {
    "stash": scale_region(15, 120, 650, 630, display_settings=DISPLAY_SETTINGS),
    "stash_logo": scale_region(310, 20, 40, 40, display_settings=DISPLAY_SETTINGS),
    "inventory": scale_region(1270, 590, 640, 260, display_settings=DISPLAY_SETTINGS),
    "expensive_card": scale_region(
        1795, 590, 110, 260, display_settings=DISPLAY_SETTINGS
    ),
    "horticrafting_divination_stack": scale_region(
        947, 427, 13, 13, display_settings=DISPLAY_SETTINGS
    ),
    "currency_tab_extra_slots_area": scale_region(
        140, 590, 390, 100, display_settings=DISPLAY_SETTINGS
    ),
}

STARTING_POSITIONS = {
    "inventory": {
        "first_slot": dict(
            zip(
                ["x", "y"],
                scale_coordinates(1300, 615, display_settings=DISPLAY_SETTINGS),
            )
        ),
    },
    "horticrafting": {
        "x": scale_coordinates(820, 330, display_settings=DISPLAY_SETTINGS)[0],
        "y": scale_coordinates(820, 330, display_settings=DISPLAY_SETTINGS)[1],
        "first_crafting_option": dict(
            zip(
                ["x", "y"],
                scale_coordinates(560, 320, display_settings=DISPLAY_SETTINGS),
            )
        ),
        "craft_button": dict(
            zip(
                ["x", "y"],
                scale_coordinates(970, 610, display_settings=DISPLAY_SETTINGS),
            )
        ),
        "crafting_slot": dict(
            zip(
                ["x", "y"],
                scale_coordinates(970, 450, display_settings=DISPLAY_SETTINGS),
            )
        ),
    },
    "stash": {
        "x": scale_coordinates(1030, 520, display_settings=DISPLAY_SETTINGS)[0],
        "y": scale_coordinates(1030, 520, display_settings=DISPLAY_SETTINGS)[1],
        "divination_cards": {
            "x": scale_coordinates(750, 440, display_settings=DISPLAY_SETTINGS)[0],
            "y": scale_coordinates(750, 440, display_settings=DISPLAY_SETTINGS)[1],
            "first_card": dict(
                zip(
                    ["x", "y"],
                    scale_coordinates(130, 250, display_settings=DISPLAY_SETTINGS),
                )
            ),
        },
        "currency": {
            "x": scale_coordinates(750, 110, display_settings=DISPLAY_SETTINGS)[0],
            "y": scale_coordinates(750, 110, display_settings=DISPLAY_SETTINGS)[1],
            "stacked_deck": dict(
                zip(
                    ["x", "y"],
                    scale_coordinates(550, 510, display_settings=DISPLAY_SETTINGS),
                )
            ),
        },
    },
}

FILE_NAMES = {
    "expensive_card": "the_immortal_inventory_4.png",
    "ultimate_model": "ultimate_model_v7.joblib",
    "stash_logo": "stash_logo.png",
    "stacked_deck": "stacked_deck.png",
    "empty_inventory_slot": "empty_inventory_slot.png",
}


PIXEL_SIZES = {"inventory": {"slot": 53}}

DIVINATION_CARDS = {
    "imperial_legacy": {"stack_size": 22},
    "the_immortal": {"stack_size": 8},
    "the_apothecary": {"stack_size": 2},
}

PATTERN_RULES = {
    "threshold": 1,
    "positive_net_limit": 3,
    "negative_net_limit": -3,
    "stop_loss": -22,
}


MODELS = {"ultimate_model": {"threshold": 0.53, "max_lag": 40}}

CARDS_USED = {"cheap_card": "imperial_legacy", "expensive_card": "the_immortal"}
MODEL_USED = "ultimate_model"

SCRIPT_SPEED = {
    "super_slow": 1,
    "slow": 0.5,
    "medium": 0.25,
    "fast": 0.1,
    "super_fast": 0.05,
}
