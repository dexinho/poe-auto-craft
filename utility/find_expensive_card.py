import pyautogui
import os

# from config import REGIONS, FOLDER_PATHS, FILE_NAMES


def find_expensive_card(region, folder, image_name):
    image_path = os.path.join(folder, image_name)
    pyautogui.moveTo(1800, 1000)  # move away the mouse

    location = pyautogui.locateOnScreen(image_path, region=region, confidence=0.9)

    if location:
        center = pyautogui.center(location)
        pyautogui.moveTo(center.x, center.y)
        print(f"Mouse moved to image at {center}")
        return {"is_found": True, "position": {"x": center.x, "y": center.y}}
    else:
        print("Image not found on screen.")
        return {"is_found": False, "position": None}


# find_expensive_card(
#     region=REGIONS["expensive_card"],
#     folder=FOLDER_PATHS["pictures"]["the_immortal"]["inventory"],
#     image_name=FILE_NAMES["expensive_card"],
# )
