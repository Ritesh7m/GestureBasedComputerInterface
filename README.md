# 👋 Gesture-Controlled Application Suite 🖐️

This project provides a suite of applications leveraging hand gesture recognition for various functionalities, including a PowerPoint controller, a virtual mouse, and a GUI application launcher. It aims to provide intuitive and innovative ways to interact with your computer using hand gestures.

🚀 **Key Features**

*   **PowerPoint Control:** Navigate through PowerPoint presentations using simple thumb-up gestures. 👍
*   **Virtual Mouse:** Control your mouse cursor and perform clicks using hand movements. 🖱️
*   **Application Launcher:** Launch frequently used applications like Notepad, Calculator, and Chrome with a click of a button on a custom GUI. 🚀
*   **Tutorial Window:** Provides a visual guide on how to use the gesture control features. 📖
*   **Loading Animation:** A visually appealing loading animation during the sign-in process. ⏳
*   **Screenshot Capture:** Capture screenshots with a specific hand gesture. 📸

🛠️ **Tech Stack**

*   **Programming Language:** Python
*   **GUI:** Tkinter
*   **Image Processing:** OpenCV (cv2), Pillow (PIL)
*   **Hand Tracking:** MediaPipe, cvzone
*   **Automation:** PyAutoGUI
*   **PowerPoint Control:** `win32com`
*   **Threading:** `threading`
*   **OS Interaction:** `os`, `subprocess`
*   **Date and Time:** `datetime`, `time`

📦 **Getting Started**

### Prerequisites

*   Python 3.x installed
*   pip package installer

### Installation

1.  Clone the repository:

    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2.  Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

    Create a `requirements.txt` file with the following content:

    ```
    opencv-python
    mediapipe
    pyautogui
    pillow
    cvzone
    pywin32
    tkcalendar
    ```

### Running Locally

1.  **Run the main GUI:**

    ```bash
    python simplegui.py
    ```

2.  **Run the Virtual Mouse:**

    ```bash
    python VirtualMouse.py
    ```

3.  **Run the PowerPoint Gesture Controller:**

    ```bash
    python PPT_Gesture.py <path_to_your_powerpoint_file>
    ```
    Replace `<path_to_your_powerpoint_file>` with the actual path to your PowerPoint presentation.

📂 **Project Structure**

```
├── Images/
│   ├── ... (Images for GUI and Manual)
├── HandTrackingModule.py  # Module for hand tracking using MediaPipe
├── Manual.py              # Script for the tutorial window
├── PPT_Gesture.py         # Script for PowerPoint gesture control
├── VirtualMouse.py        # Script for virtual mouse functionality
├── create_new_window.py   # Script for creating the application launcher window
├── simplegui.py           # Script for the main GUI window
├── Tutorial_Window.py     # (Currently Empty) Intended for tutorial features
└── README.md              # This file
```

📸 **Screenshots**

(Space for screenshots of the GUI, virtual mouse in action, and PowerPoint control)

🤝 **Contributing**

Contributions are welcome! Please follow these steps:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Make your changes and commit them with descriptive messages.
4.  Push your changes to your fork.
5.  Submit a pull request.



.
