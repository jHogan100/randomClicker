
import pyautogui #use pip to unstall these libraries
import random
import time



def randomClick():
    interval = random.uniform(1.5, 1.6) #adjust for selected interval
    time.sleep(interval)  # Wait for the random interval
    pyautogui.click()


try:
    while True:
        randomClick()

except KeyboardInterrupt:

    print("CTRL + C detected. Exiting script.")

    exit(0)