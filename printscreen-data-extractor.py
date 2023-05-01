import cv2 
import pytesseract
import pyautogui
import time

def showinfo(path):

    img = cv2.imread(path)

    # Adding custom options
    custom_config = r'--oem 1 --psm 6'
    data = pytesseract.image_to_string(img, config=custom_config)
    print(data)


def screenshot():
    time.sleep(2)
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(r'D:\screenshot.png')

    print("Screenshot Ok...\n search string data..")
    path = "D:\screenshot.png"
    showinfo(path)

screenshot()
