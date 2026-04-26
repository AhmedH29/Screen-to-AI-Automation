from xml.dom import minidom

import keyboard
import mss
import cv2
import numpy as np
import pytesseract
import pyperclip
import pyautogui
import time
import webbrowser

def capture():
    print('\nCapturing your image text, please hold...')

    with mss.mss() as sct:
        monitor = {"top": 0, "left": 0, "width": 1920, "height": 1080}
        screenshot = sct.grab(monitor)

        img = np.array(screenshot)
        img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)[1]

        text = pytesseract.image_to_string(thresh, config='--psm 6')

    print("RAW OCR:\n")
    print(text)


    pyperclip.copy(text)
    print('copied!')

    webbrowser.open("https://copilot.microsoft.com/")
    time.sleep(5)

    pyautogui.moveRel(-200, -50, duration=0.5)
    pyautogui.hotkey("ctrl", "v")
    time.sleep(0.5)
    pyautogui.press("enter")

keyboard.add_hotkey('ctrl+shift+c', capture)

print("Press CTRL+SHIFT+C to capture and send to Copilot.")
keyboard.wait()

