import os
import subprocess
import time

subprocess.Popen(["python", "Manual.py"])


# Function to check if PowerPoint is open
def is_powerpoint_open():
    os.system('TASKLIST > temp.txt')
    with open('temp.txt', 'r') as file:
        tasklist = file.read()
    return 'POWERPNT.EXE' in tasklist.upper()

# Function to execute VirtualMouse.py
def execute_virtual_mouse():
    subprocess.Popen(["python", "VirtualMouse.py"])

# Function to execute Code.py
def execute_code():
    subprocess.Popen(["python", "Code.py"])

# Main function to control execution flow based on PowerPoint
def main():
    if is_powerpoint_open():
        execute_code()

    else:
        execute_virtual_mouse()

import cv2
import numpy as np
import pyautogui
import HandTrackingModule as htm
import requests
import HandTrackingModule as htm

# Initialize plocX and plocY
plocX, plocY = 0, 0


##########################
wCam, hCam = 640, 480
frameR = 150  # Increase frame reduction
smoothening = 5 # Decrease smoothening factor
#########################
#########################s

pTime = 0
plocX, plocY = 0, 0
clocX, clocY = 0, 0

cap = cv2.VideoCapture(0)  # Open the default camera (usually the built-in webcam)
cap.set(3, wCam)
cap.set(4, hCam)
detector = htm.handDetector(maxHands=1)
wScr, hScr = pyautogui.size()

def detect_slide_advancement(detector, plocX, plocY):
    fingers = detector.fingersUp()
    if fingers[1] == 1 and fingers[2] == 0:
        x3 = np.interp(x1, (frameR, wCam - frameR), (0, wScr))
        y3 = np.interp(y1, (frameR, hCam - frameR), (0, hScr))

        clocX = plocX + (x3 - plocX) / smoothening
        clocY = plocY + (y3 - plocY) / smoothening

        pyautogui.moveTo(clocX, clocY)
        cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
        plocX, plocY = clocX, clocY


while True:
    # Capture frame-by-frame from the webcam
    ret, img = cap.read()
    if not ret:
        break

    img = cv2.flip(img, 1)
    img = cv2.resize(img, (wCam, hCam))

    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img)

    if lmList:
        x1, y1 = lmList[8][1:]
        x2, y2 = lmList[12][1:]

        fingers = detector.fingersUp()

        cv2.rectangle(img, (frameR, frameR), (wCam - frameR, hCam - frameR), (255, 0, 255), 2)

        if fingers[1] == 1 and fingers[2] == 0:
            x3 = np.interp(x1, (frameR, wCam - frameR), (0, wScr))
            y3 = np.interp(y1, (frameR, hCam - frameR), (0, hScr))

            clocX = plocX + (x3 - plocX) / smoothening
            clocY = plocY + (y3 - plocY) / smoothening

            pyautogui.moveTo(clocX, clocY)
            cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
            plocX, plocY = clocX, clocY

        if fingers[1] == 1 and fingers[2] == 1:
            length, img, lineInfo = detector.findDistance(8, 12, img)

            if length < 40:
                cv2.circle(img, (lineInfo[4], lineInfo[5]), 15, (0, 255, 0), cv2.FILLED)
                pyautogui.click()

        if fingers[1] == 1 and fingers[2] == 1:
            # Check if handgun gesture is detected
            if detector.isHandGesture():
                length, img, lineInfo = detector.findDistance(8, 12, img)

                if length > 40:
                    cv2.circle(img, (lineInfo[4], lineInfo[5]), 15, (0, 255, 0), cv2.FILLED)
                    pyautogui.click()

                    # Call the function to detect slide advancement gesture
                detect_slide_advancement(detector, plocX, plocY)

                # Update plocX and plocY
                plocX, plocY = clocX, clocY

            # Call the function to detect slide advancement gesture
            detect_slide_advancement(detector, plocX, plocY)




    cv2.imshow("Image", img)

    if cv2.waitKey(1) == 27:
        break

# Release the capture
cap.release()
cv2.destroyAllWindows()

if __name__ == "__main__":
    main()



