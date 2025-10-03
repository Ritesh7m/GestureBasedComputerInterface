import cv2
import mediapipe as mp
import platform
import os
import math

# Windows-only: pycaw for volume control
if platform.system() == "Windows":
    from ctypes import cast, POINTER
    from comtypes import CLSCTX_ALL
    from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))


# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# Webcam capture
cap = cv2.VideoCapture(0)

def set_volume(increase=True):
    system = platform.system()
    if system == "Windows":
        current_volume = volume.GetMasterVolumeLevelScalar()
        step = 0.05
        new_volume = min(max(current_volume + step if increase else current_volume - step, 0.0), 1.0)
        volume.SetMasterVolumeLevelScalar(new_volume, None)
        print(f"Windows volume set to {new_volume*100:.0f}%")
    elif system == "Linux":
        step = 5  # percent
        cmd = f"amixer -D pulse sset Master {step}%+" if increase else f"amixer -D pulse sset Master {step}%-"
        os.system(cmd)
        print(f"Linux volume {'increased' if increase else 'decreased'}")
    elif system == "Darwin":
        step = 5
        cmd = f"osascript -e 'set volume output volume ((output volume of (get volume settings)) + {step})'" if increase else f"osascript -e 'set volume output volume ((output volume of (get volume settings)) - {step})'"
        os.system(cmd)
        print(f"Mac volume {'increased' if increase else 'decreased'}")

def thumb_gesture(hand_landmarks):
    # Thumb tip: 4, Thumb MCP: 2
    # Index tip: 8
    thumb_tip = hand_landmarks.landmark[4]
    thumb_mcp = hand_landmarks.landmark[2]

    # y-coordinate: smaller is up
    if thumb_tip.y < thumb_mcp.y - 0.05:
        return "up"
    elif thumb_tip.y > thumb_mcp.y + 0.05:
        return "down"
    return None

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, handLms, mp_hands.HAND_CONNECTIONS)
            gesture = thumb_gesture(handLms)
            if gesture == "up":
                set_volume(True)
            elif gesture == "down":
                set_volume(False)

    cv2.imshow("Volume Control", frame)
    if cv2.waitKey(1) & 0xFF == 27:  
        break

cap.release()
cv2.destroyAllWindows()
