import pyautogui
import os

currency_size = 12
region = (1280, 600, currency_size, currency_size)
horticrafting_path = r"C:\Users\jasmi\Desktop\programming_2024\python\poe\auto_craft\assets\images\inventory"
image_name = "empty_slot.png"
full_path = os.path.join(horticrafting_path, image_name)
screenshot = pyautogui.screenshot(region=region)
screenshot.save(full_path)