import pyautogui

def move_item(x, y):
    pyautogui.keyDown("ctrl")
    pyautogui.moveTo(x, y)
    pyautogui.click()
    pyautogui.keyUp("ctrl")
