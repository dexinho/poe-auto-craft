import pyautogui
import os

currency_size = 10
logo_size = 20
region = (100, 200, currency_size, currency_size)
horticrafting_path = r"C:\Users\jasmi\Desktop\programming_2024\python\poe\auto_craft\assets\images\stash\divination_tab"
image_name = "divination_card_not_found.png"
full_path = os.path.join(horticrafting_path, image_name)
screenshot = pyautogui.screenshot(region=region)
screenshot.save(full_path)

# pyautogui.moveTo(100, 100, 0.2)
