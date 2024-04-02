import pyautogui
from time import sleep

broswerPos = []
soilPos = []
seedPos = ()
canPos = ()
shearsPos = ()

turn = 1


def plant():
    pyautogui.click(x=seedPos[0], y=seedPos[1])
    for pos in soilPos:
        pyautogui.click(x=pos[0], y=pos[1], duration=0.2)
    pyautogui.press("esc")


def water():
    pyautogui.click(x=canPos[0], y=canPos[1])
    for pos in soilPos:
        pyautogui.click(x=pos[0], y=pos[1], duration=0.2)
    pyautogui.press("esc")


def harvest():
    pyautogui.click(x=shearsPos[0], y=shearsPos[1])
    for pos in soilPos:
        pyautogui.click(x=pos[0], y=pos[1], duration=0.2)
    pyautogui.press("esc")


while turn > 0:
    turn -= 1
    for bros in broswerPos:
        plant()
        water()

    sleep(60)

    for bros in broswerPos:
        harvest()
