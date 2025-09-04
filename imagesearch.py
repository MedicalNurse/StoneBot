# imagesearch.py
import cv2
import numpy as np
import pyautogui

def imagesearch(image_path, precision=0.8):
    screenshot = pyautogui.screenshot()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    template = cv2.imread(image_path, cv2.IMREAD_COLOR)

    if template is None:
        print(f"Görsel bulunamadı: {image_path}")
        return [-1, -1]

    result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(result)

    if max_val < precision:
        return [-1, -1]
    return max_loc
