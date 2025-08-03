import pyautogui

pyautogui.PAUSE = 0.05

REGIONS = {"stash": (15, 120, 650, 630), "inventory": (1270, 590, 340, 260)}
IMAGE_PATHS = {
    "currency": {
        "divination_card": "./assets/pictures/divination_card.png",
    }
}
STARTING_POSITIONS = {
    "inventory": {
        "first_slot": {"x": 1300, "y": 615},
    },
}
PIXEL_SIZES = {"inventory": {"slot": 53}}


def splitDivinationCards():
    # focus the game
    pyautogui.click(1800, 1000)
    
    for i in range(5):
        for j in range(5):
            pyautogui.moveTo(
                STARTING_POSITIONS["inventory"]["first_slot"]["x"]
                + j * PIXEL_SIZES["inventory"]["slot"],
                STARTING_POSITIONS["inventory"]["first_slot"]["y"]
                + i * PIXEL_SIZES["inventory"]["slot"],
            )

            pyautogui.keyDown("shift")
            pyautogui.click()
            pyautogui.press("1")
            pyautogui.press("1")
            pyautogui.press("enter")
            pyautogui.keyUp("shift")

            pyautogui.moveTo(
                STARTING_POSITIONS["inventory"]["first_slot"]["x"]
                + (j + 5) * PIXEL_SIZES["inventory"]["slot"],
                STARTING_POSITIONS["inventory"]["first_slot"]["y"]
                + i * PIXEL_SIZES["inventory"]["slot"],
            )

            pyautogui.click()


splitDivinationCards()
