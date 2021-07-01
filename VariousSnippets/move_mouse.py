import pyautogui
from datetime import datetime

#print(pyautogui.size())

now = datetime.now()
#print(now)
current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)

while current_time < '09:43:00':   #set this to your stop time.
    pyautogui.moveTo(100, 100, duration = 1)
    pyautogui.moveTo(100, 200, duration = 1)
    pyautogui.moveTo(200, 200, duration = 1)
    pyautogui.moveTo(200, 100, duration = 1)
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    #print("Current Time =", current_time)

print("Program Done!")

