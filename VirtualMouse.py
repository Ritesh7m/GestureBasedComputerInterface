import cv2
import mediapipe as mp
import pyautogui
import os
import time
from datetime import datetime   # ✅ Import for human-readable timestamps

# Mediapipe hands initialization
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

# Create folder for screenshots
if not os.path.exists("screenshots"):
    os.makedirs("screenshots")

# For webcam input
cap = cv2.VideoCapture(0)

# Gesture tracking variables
prev_click_time = 0
screenshot_cooldown = 2  # seconds

with mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
) as hands:

    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("Ignoring empty camera frame.")
            continue

        # Flip the image horizontally for a later selfie-view display
        image = cv2.flip(image, 1)
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Process the image and find hands
        results = hands.process(image_rgb)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:

                # Drawing landmarks
                mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                # Get landmark positions
                h, w, _ = image.shape
                landmarks = []
                for lm in hand_landmarks.landmark:
                    landmarks.append((int(lm.x * w), int(lm.y * h)))

                # Example gesture: Index & middle finger up (V gesture)
                index_tip = landmarks[8][1] < landmarks[6][1]
                middle_tip = landmarks[12][1] < landmarks[10][1]
                ring_tip = landmarks[16][1] > landmarks[14][1]  # ring finger down
                pinky_tip = landmarks[20][1] > landmarks[18][1]  # pinky finger down

                if index_tip and middle_tip and ring_tip and pinky_tip:
                    current_time = time.time()
                    if current_time - prev_click_time > screenshot_cooldown:
                        prev_click_time = current_time
                        
                        # ✅ Human-readable timestamp (YYYY-MM-DD_HH-MM-SS)
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

