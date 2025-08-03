import pyautogui
import os

region = (1850, 590, 18, 18)
horticrafting_path = r"C:\Users\jasmi\Desktop\programming_2024\python\poe\auto_craft\assets\pictures\divination_cards\the_apothecary\inventory"
image_name = "the_apothecary_inventory_3.png"
full_path = os.path.join(horticrafting_path, image_name)
screenshot = pyautogui.screenshot(region=region)
screenshot.save(full_path)
