import pyautogui
import os


def find_image(region, folder, image_name):
    pyautogui.PAUSE = 0.04
    image_path = os.path.join(folder, image_name)
    pyautogui.moveTo(1500, 1200)  # move away the mouse

    try:
        location = pyautogui.locateOnScreen(image_path, region=region, confidence=0.8)
        center = pyautogui.center(location)
        return {"is_found": True, "position": {"x": center.x, "y": center.y}}

    except pyautogui.ImageNotFoundException:
        return {"is_found": False, "position": None}
