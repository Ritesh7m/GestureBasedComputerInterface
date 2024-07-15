import os
import tkinter as tk
from PIL import Image, ImageTk



def manual_window():
    # Create the Tkinter window
    window = tk.Tk()
    window.title("Gesture Control Tutorial")
    window.geometry("950x600")
    window.configure(bg="white")

    text_label_3 = tk.Label(window, text="Welcome To The Gesture Tutorial", font=("Helvetica", 16), bg="white")
    text_label_3.place(x=320, y=20)

    # Load the image of the index finger
    hover_control_image = Image.open("Images/hover_control.png")
    hover_control_image = hover_control_image.resize((150, 150))  # Resize the image as needed
    hover_control_image_photo = ImageTk.PhotoImage(hover_control_image)

    # Create a label to display the index finger image
    hover_control_label = tk.Label(window, image=hover_control_image_photo, bg="white")
    hover_control_label.place(x=90, y=150)  # Adjust the position as needed

    # Add a text label below the image label
    text_label = tk.Label(window, text="Extend Your Index Finger", font=("Helvetica", 16), bg="white")
    text_label.place(x=50, y=300)  # Adjust the position as needed

    # Add the second part of the text label
    text_label_2 = tk.Label(window, text="To Hover The Mouse", font=("Helvetica", 16), bg="white")
    text_label_2.place(x=65, y=330)  # Adjust the position as needed

    # Load the image of the index finger
    green_tick_image = Image.open("Images/green_tick.png")
    green_tick_image = green_tick_image.resize((100, 100))  # Resize the image as needed
    green_tick_image_photo = ImageTk.PhotoImage(green_tick_image)

    # Create a label to display the index finger image
    green_tick_label = tk.Label(window, image=green_tick_image_photo, bg="white")
    green_tick_label.place(x=100, y=390)  # Adjust the position as needed

    # Load the image of the index finger
    click_control_image = Image.open("Images/click_control.png")
    click_control_image = click_control_image.resize((150, 150))  # Resize the image as needed
    click_control_image_photo = ImageTk.PhotoImage(click_control_image)

    # Create a label to display the index finger image
    click_control_label = tk.Label(window, image=click_control_image_photo, bg="white")
    click_control_label.place(x=380, y=150)  # Adjust the position as needed

    # Add a text label below the image label
    text_label = tk.Label(window, text="Extend Your Two Fingers", font=("Helvetica", 16), bg="white")
    text_label.place(x=360, y=300)  # Adjust the position as needed

    # Add the second part of the text label
    text_label_2 = tk.Label(window, text="To Perform A Click", font=("Helvetica", 16,), bg="white")
    text_label_2.place(x=390, y=330)  # Adjust the position as needed

    # Load the image of the index finger
    green_tick_1_image = Image.open("Images/green_tick.png")
    green_tick_1_image = green_tick_1_image.resize((100, 100))  # Resize the image as needed
    green_tick_1_image_photo = ImageTk.PhotoImage(green_tick_1_image)

    # Create a label to display the index finger image
    green_tick_1_label = tk.Label(window, image=green_tick_1_image_photo, bg="white")
    green_tick_1_label.place(x=420, y=390)  # Adjust the position as needed

    # Load the image of the index finger
    wrong_control_image = Image.open("Images/wrong_gesture.png")
    wrong_control_image = wrong_control_image.resize((150, 150))  # Resize the image as needed
    wrong_control_image_photo = ImageTk.PhotoImage(wrong_control_image)

    # Create a label to display the index finger image
    wrong_control_label = tk.Label(window, image=wrong_control_image_photo, bg="white")
    wrong_control_label.place(x=700, y=150)  # Adjust the position as needed

    # Add a text label below the image label
    text_label = tk.Label(window, text="Do Not Perform The Above", font=("Helvetica", 16), bg="white")
    text_label.place(x=660, y=300)  # Adjust the position as needed

    # Add the second part of the text label
    text_label_3 = tk.Label(window, text="Given Gesture", font=("Helvetica", 16,), bg="white")
    text_label_3.place(x=710, y=330)  # Adjust the position as needed

    # Load the image of the index finger
    red_cross_image = Image.open("Images/red_cross.png")
    red_cross_image = red_cross_image.resize((150, 150))  # Resize the image as needed
    red_cross_image_photo = ImageTk.PhotoImage(red_cross_image)

    # Create a label to display the index finger image
    red_cross_label = tk.Label(window, image=red_cross_image_photo, bg="white")
    red_cross_label.place(x=700, y=370)  # Adjust the position as needed

    OK_button = tk.Button(window, text="OK", command=lambda: open_simplegui(window))
    OK_button.place(x=450, y=550)

    # Run the Tkinter event loop
    window.mainloop()

def open_simplegui(window):
    os.system("python simplegui.py")
    window.destroy()

# Call the manual_window function to start the program
manual_window()

