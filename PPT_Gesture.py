import win32com.client
from cvzone.HandTrackingModule import HandDetector
import cv2

try:
    # Initialize PowerPoint application and open presentation
    Application = win32com.client.Dispatch("PowerPoint.Application")
    Presentation = Application.Presentations.Open("C:\\Users\shubham\Documents\gesture2.pptx")
    Presentation.SlideShowSettings.Run()

except Exception as e:
    print("Error", e)
    exit()




# Parameters
width, height = 900, 720
gestureThreshold = 300

# Camera Setup
cap = cv2.VideoCapture(0)
cap.set(3, width)
cap.set(4, height)

# Hand Detector
detectorHand = HandDetector(detectionCon=0.8, maxHands=2)

# Variables
buttonPressed = False
delay = 30

while True:
    # Get image frame
    success, img = cap.read()

    # Find the hands and their landmarks
    hands, img = detectorHand.findHands(img)

    if hands and not buttonPressed:
        for hand in hands:
            cx, cy = hand["center"]
            fingers = detectorHand.fingersUp(hand)

            # If hand is at the height of the face
            if cy <= gestureThreshold:
                # If thumb is up, go to next slide
                if fingers == [1, 0, 0, 0, 0] and hand["type"] == "Right":
                    if Presentation.SlideShowWindow.View.State == 1:  # Check if in slideshow mode
                        print("Next Slide")
                        buttonPressed = True
                        Presentation.SlideShowWindow.View.Next()
                    else:
                        print("Not in slideshow mode.")

                # If thumb is up , go to previous slide
                elif fingers == [1, 0, 0, 0, 0] and hand["type"] == "Left":
                    if Presentation.SlideShowWindow.View.State == 1:  # Check if in slideshow mode
                        print("Previous Slide")
                        buttonPressed = True
                        Presentation.SlideShowWindow.View.Previous()
                    else:
                        print("Not in slideshow mode.")

    # Reset buttonPressed after delay
    if buttonPressed:
        delay -= 1
        if delay == 0:
            delay = 30
            buttonPressed = False

    cv2.imshow("Image", img)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break
