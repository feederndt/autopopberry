import pyautogui
from time import sleep

broswerPos = [(710, 1060), (770, 1060), (830, 1060),
              (890, 1060), (950, 1060), (1010, 1060)]
soilPos = [(965, 315), (1045, 315), (885, 400),
           (965, 400), (1045, 400), (1125, 400), (805, 480), (885, 480), (965, 480), (1045, 480), (1125, 480), (1205, 480), (805, 555), (885, 555), (965, 555), (1045, 555), (1125, 555), (1205, 555), (805, 635), (885, 635), (965, 635), (1045, 635), (1125, 635), (1205, 635), (885, 720), (965, 720), (1045, 720), (1125, 720), (1205, 720), (965, 800), (1045, 800)]

# broswerPos = [(710, 1060), (770, 1060), (830, 1060),
#               (890, 1060), (950, 1060), (1010, 1060)]

# (965, 315), (1045, 315),
# (885, 400), (965, 400),(1045, 400),(1125, 400),
# (805, 480), (885, 480), (965, 480),(1045, 480),(1125, 480),(1205,480),
# (805, 555), (885, 555), (965, 555),(1045, 555),(1125, 555),(1205,555),
# (805, 635), (885, 635), (965, 635),(1045, 635),(1125, 635),(1205,635),
#  (885, 720), (965, 720),(1045, 720),(1125, 720),(1205,720),
# (965, 800), (1045, 800)


def plant():
    pyautogui.press("1")
    for pos in soilPos:
        pyautogui.click(x=pos[0], y=pos[1], clicks=2, interval=0.07)
    pyautogui.press("esc")


def water():
    pyautogui.press("2")
    for pos in soilPos:
        pyautogui.click(x=pos[0], y=pos[1], clicks=2, interval=0.07)
    pyautogui.press("esc")


def harvest():
    pyautogui.press("3")
    for pos in soilPos:
        pyautogui.click(x=pos[0], y=pos[1], clicks=2, interval=0.07)
    pyautogui.press("esc")


def autoPop(turn, numofBros, shearFirst):
    numberofBros = broswerPos[:numofBros]
    t = turn

    while t > 0:

        for bros in numberofBros:
            pyautogui.click(x=bros[0], y=bros[1])
            if t != turn or shearFirst:
                harvest()
                sleep(1)
            else:
                pass
            plant()
            sleep(1)
            water()

        if t == 1:
            for bros in numberofBros:
                pyautogui.click(x=bros[0], y=bros[1])
                harvest()
                sleep(2)

        t -= 1


autoPop(turn=5, numofBros=6, shearFirst=False)

# if __name__ == "__main__":
#     turn = 4
#     while turn > 0:
#         turn -= 1
#         for bros in broswerPos:
#             pyautogui.click(x=bros[0], y=bros[1])
#             plant()
#             water()

#         sleep(35)

#         for bros in broswerPos:
#             pyautogui.click(x=bros[0], y=bros[1])
#             harvest()
