import cv2
import pyautogui
import os
import time
from datetime import datetime
import HandTrackingModule as htm

# Create folder for screenshots
if not os.path.exists("screenshots"):
    os.makedirs("screenshots")

# For webcam input
cap = cv2.VideoCapture(0)
# Initialize our hand detector from the module
detector = htm.handDetector(maxHands=1, detectionCon=0.7)
# Gesture tracking variables
prev_click_time = 0
screenshot_cooldown = 2  # seconds

while cap.isOpened():
    # --- THIS WHOLE SECTION IS NOW UPGRADED ---
    success, image = cap.read()
    if not success:
        print("Ignoring empty camera frame.")
        continue

    # Flip the image horizontally for a selfie-view display
    image = cv2.flip(image, 1)

    # 1. Find and draw the hand using our module
    image = detector.findHands(image)
    
    # 2. Get the landmark list
    lmList, bbox = detector.findPosition(image, draw=False)

    # 3. Check if a hand is detected
    if len(lmList) != 0:
        # 4. Check which fingers are up
        fingers = detector.fingersUp()
        
        # 5. Check for the "V" gesture (index and middle up) for screenshots
        # This is much cleaner than the old way! [Thumb, Index, Middle, Ring, Pinky]
        if fingers == [0, 1, 1, 0, 0]:
            current_time = time.time()
            if current_time - prev_click_time > screenshot_cooldown:
                prev_click_time = current_time

                # Human-readable timestamp (YYYY-MM-DD_HH-MM-SS)
                timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                filename = f"screenshots/screenshot_{timestamp}.png"

                pyautogui.screenshot(filename)
                print(f"📸 Screenshot saved as {filename}")

    # Display the image
    cv2.imshow('Virtual Mouse with Screenshot Gesture', image)

    if cv2.waitKey(5) & 0xFF == 27:  # ESC to exit
        break

cap.release()
cv2.destroyAllWindows()