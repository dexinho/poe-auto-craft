import pyautogui
pyautogui.PAUSE = 0.03

def move_item(x, y):
    pyautogui.keyDown("ctrl")
    pyautogui.moveTo(x, y)
    pyautogui.click()
    pyautogui.keyUp("ctrl")
