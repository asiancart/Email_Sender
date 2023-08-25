import pyautogui
import time

time.sleep(3)

print(pyautogui.size())
print(pyautogui.position())

pyautogui.moveTo(100,100,1)
pyautogui.moveRel(100,100)


time.sleep(1)
distance=400
a=distance

while distance>50:
    pyautogui.dragRel(distance,0,1,button="left")
    distance -= 50
    pyautogui.dragRel(0,distance,1,button="left")
    pyautogui.dragRel(-distance,0,1,button="left")
    distance -= 50
    pyautogui.dragRel(0,-distance,1,button="left")

