REGIONS = {
    "stash": (15, 120, 650, 630),
    "inventory": (1270, 590, 340, 260),
    "expensive_card": (1795, 590, 110, 260),
    "horticrafting_divination_stack": (947, 427, 13, 13),
}
FOLDER_PATHS = {
    "pictures": {
        "imperial_legacy": {
            "horticrafting": r"C:\Users\jasmi\Desktop\programming_2024\python\poe\auto_craft\assets\pictures\divination_cards\imperial_legacy\horticrafting",
            "inventory": r"C:\Users\jasmi\Desktop\programming_2024\python\poe\auto_craft\assets\pictures\divination_cards\imperial_legacy\inventory",
        },
        "the_immortal": {
            "horticrafting": r"C:\Users\jasmi\Desktop\programming_2024\python\poe\auto_craft\assets\pictures\divination_cards\the_immortal\horticrafting",
            "inventory": r"C:\Users\jasmi\Desktop\programming_2024\python\poe\auto_craft\assets\pictures\divination_cards\the_immortal\inventory",
        },
        "the_apothecary": {
            "horticrafting": r"C:\Users\jasmi\Desktop\programming_2024\python\poe\auto_craft\assets\pictures\divination_cards\the_apothecary\horticrafting",
            "inventory": r"C:\Users\jasmi\Desktop\programming_2024\python\poe\auto_craft\assets\pictures\divination_cards\the_apothecary\inventory",
        },
        "stash": {
            "logo": r"C:\Users\jasmi\Desktop\programming_2024\python\poe\auto_craft\assets\pictures\stash"
        },
    },
    "logs": r"C:\Users\jasmi\Desktop\programming_2024\python\poe\auto_craft\logs",
    "pattern_history": r"C:\Users\jasmi\Desktop\programming_2024\python\poe\auto_craft\logs\pattern_history",
    "models": r"C:\Users\jasmi\Desktop\programming_2024\python\poe\auto_craft\models",
}

LOGS = {
    "cheap_craft_results": "cheap_craft_results.txt",
    "latest_expensive_crafts": "latest_expensive_crafts.txt",
    "expensive_craft_results": "expensive_craft_results.txt",
    "craft_results": "craft_results.txt",
}
STARTING_POSITIONS = {
    "inventory": {
        "first_slot": {"x": 1300, "y": 615},
    },
    "horticrafting": {
        "x": 820,
        "y": 330,
        "first_crafting_option": {"x": 560, "y": 320},
        "craft_button": {"x": 970, "y": 610},
        "crafting_slot": {"x": 970, "y": 450},
    },
    "stash": {
        "x": 1030,
        "y": 520,
        "divination_cards": {"x": 750, "y": 440, "first_card": {"x": 130, "y": 250}},
        "currency": {"x": 750, "y": 110, "stacked_deck": {"x": 550, "y": 510}},
    },
}
FILE_NAMES = {
    "expensive_card": "the_immortal_inventory_4.png",
    "ultimate_model": "ultimate_model_v7.joblib",
    "stash_logo": "stash_logo.png",
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
