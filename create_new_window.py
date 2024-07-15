import datetime
import tkinter as tk
import time

from PIL import Image, ImageTk, ImageDraw
from tkcalendar import Calendar
import subprocess
import os



def launch_notepad():
    subprocess.Popen(["notepad.exe"])

def launch_calculator():
    subprocess.Popen(["calc.exe"])

def launch_chrome():
    os.system("start chrome.exe")

def launch_powerpoint():
    os.system("start POWERPNT.EXE")


def launch_recycle_bin():
    subprocess.Popen(["explorer.exe", "shell:RecycleBinFolder"])

def launch_pycharm():
    os.system("start pycharm64.exe")

def create_new_window():
    def launch_file_explorer():
        subprocess.Popen(["explorer.exe"])

    def launch_search():
        # Implement search functionality here
        pass

    def launch_weather():
        # Implement weather functionality here
        pass

        # Function to update the clock
        def update_clock():
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            clock_label.config(text=current_time)
            new_window.after(1000, update_clock)  # Update every second



    new_window = tk.Toplevel()
    new_window.title("New Interface")
    new_window.geometry("1250x685")

    # Load background image
    bg_image = Image.open("Images/BGImage.jpg")
    bg_image = ImageTk.PhotoImage(bg_image)

    new_canvas = tk.Canvas(new_window, width=1250, height=1200)
    new_canvas.pack(fill=tk.BOTH, expand=True)
    new_canvas.create_image(0, 0, anchor=tk.NW, image=bg_image)

    # Function to update the clock
    def update_clock():
        current_time = time.strftime("%H:%M:%S")
        clock_label.config(text=current_time)
        new_window.after(1000, update_clock)  # Update every second


    # Create a label widget for clock
    clock_label = tk.Label(new_window, font=("Helvetica", 14), fg="white", bg="black")
    clock_label.place(x=1150, y=10)

    # Update the clock
    update_clock()

    #WINDOW AND BUTTONS


    # Load file icon image and resize it
    recycle_bin_icon_image = Image.open("Images/recycle_bin_icon.png")
    recycle_bin_icon_image = recycle_bin_icon_image.resize((85, 85))  # Adjust size as needed

    # Make white background transparent
    recycle_bin_icon_image = make_transparent(recycle_bin_icon_image)

    # Convert the image to Tkinter-compatible format
    recycle_bin_icon_photo = ImageTk.PhotoImage(recycle_bin_icon_image)

    # Create button with file icon image
    btn_recycle_bin_icon = tk.Button(new_window, image=recycle_bin_icon_photo, command=launch_recycle_bin, bd=0)
    btn_recycle_bin_icon.image = recycle_bin_icon_photo  # Keep a reference to avoid garbage collection
    btn_recycle_bin_icon.place(x=10, y=10)  # Adjust the coordinates as needed

    # Load Chrome icon image and resize it
    file_icon_image = Image.open("Images/file_icon.png")
    file_icon_image = file_icon_image.resize((85, 85))  # Adjust size as needed

    # Make white background transparent
    file_icon_image = make_transparent(file_icon_image)

    # Convert the image to Tkinter-compatible format
    file_icon_photo = ImageTk.PhotoImage(file_icon_image)

    # Create button with Chrome icon image
    btn_file_icon = tk.Button(new_window, image=file_icon_photo, command=launch_file_explorer, bd=0)
    btn_file_icon.image = file_icon_photo  # Keep a reference to avoid garbage collection
    btn_file_icon.place(x=10, y=110)  # Adjust the coordinates as needed

    # Load Recycle Bin icon image and resize it
    chrome_icon_image = Image.open("Images/chrome_icon.png")
    chrome_icon_image = chrome_icon_image.resize((85, 85))  # Adjust size as needed

    # Make white background transparent
    chrome_icon_image = make_transparent(chrome_icon_image)

    # Convert the image to Tkinter-compatible format
    chrome_icon_photo = ImageTk.PhotoImage(chrome_icon_image)

    # Create button with Recycle Bin icon image
    btn_chrome_icon = tk.Button(new_window, image=chrome_icon_photo, command=launch_chrome, bd=0)
    btn_chrome_icon.image = chrome_icon_photo  # Keep a reference to avoid garbage collection
    btn_chrome_icon.place(x=10, y=210)  # Adjust the coordinates as needed

    # Load Notepad icon image and resize it
    notepad_icon_image = Image.open("Images/notepad_icon.png")
    notepad_icon_image = notepad_icon_image.resize((85, 85))  # Adjust size as needed

    # Make white background transparent
    notepad_icon_image = make_transparent(notepad_icon_image)

    # Convert the image to Tkinter-compatible format
    notepad_icon_photo = ImageTk.PhotoImage(notepad_icon_image)

    # Create button with Notepad icon image
    btn_notepad_icon = tk.Button(new_window, image=notepad_icon_photo, command=launch_notepad, bd=0)
    btn_notepad_icon.image = notepad_icon_photo  # Keep a reference to avoid garbage collection
    btn_notepad_icon.place(x=10, y=310)  # Adjust the coordinates as needed

    # Load Calculator icon image and resize it
    calc_icon_image = Image.open("Images/calc_icon.png")
    calc_icon_image = calc_icon_image.resize((85, 85))  # Adjust size as needed

    # Make white background transparent
    calc_icon_image = make_transparent(calc_icon_image)

    # Convert the image to Tkinter-compatible format
    calc_icon_photo = ImageTk.PhotoImage(calc_icon_image)

    # Create button with Calculator icon image
    btn_calc_icon = tk.Button(new_window, image=calc_icon_photo, command=launch_calculator, bd=0)
    btn_calc_icon.image = calc_icon_photo  # Keep a reference to avoid garbage collection
    btn_calc_icon.place(x=10, y=410)  # Adjust the coordinates as needed

    # Load PowerPoint icon image and resize it
    powerpoint_icon_image = Image.open("Images/powerpoint_icon.png")
    powerpoint_icon_image = powerpoint_icon_image.resize((85, 85))  # Adjust size as needed

    # Make white background transparent
    powerpoint_icon_image = make_transparent(powerpoint_icon_image)

    # Convert the image to Tkinter-compatible format
    powerpoint_icon_photo = ImageTk.PhotoImage(powerpoint_icon_image)

    # Create button with PowerPoint icon image
    btn_powerpoint_icon = tk.Button(new_window, image=powerpoint_icon_photo, command=launch_powerpoint, bd=0)
    btn_powerpoint_icon.image = powerpoint_icon_photo  # Keep a reference to avoid garbage collection
    btn_powerpoint_icon.place(x=10, y=510)  # Adjust the coordinates as needed

    # Load PowerPoint icon image and resize it
    pycharm_icon_image = Image.open("Images/pycharm_icon.png")
    pycharm_icon_image = pycharm_icon_image.resize((85, 85))  # Adjust size as needed

    # Make white background transparent
    pycharm_icon_image = make_transparent(pycharm_icon_image)

    # Convert the image to Tkinter-compatible format
    pycharm_icon_photo = ImageTk.PhotoImage(pycharm_icon_image)

    # Create button with PowerPoint icon image
    btn_pycharm_icon = tk.Button(new_window, image=pycharm_icon_photo, command=launch_pycharm, bd=0)
    btn_pycharm_icon.image = powerpoint_icon_photo  # Keep a reference to avoid garbage collection
    btn_pycharm_icon.place(x=120, y=10)  # Adjust the coordinates as needed

    #LABEL AND BUTTONS

    # Add a label at the bottom of the window
    bottom_label = tk.Label(new_window, bg="grey", fg="white", height=3)
    bottom_label.place(x=0, y=635, relwidth=1)

    # Load desktop app icon images and resize them
    notepad_icon_image = Image.open("Images/notepad_icon.png")
    notepad_icon_image = notepad_icon_image.resize((40, 40))  # Adjust size as needed

    calc_icon_image = Image.open("Images/calc_icon.png")
    calc_icon_image = calc_icon_image.resize((40, 40))  # Adjust size as needed

    chrome_icon_image = Image.open("Images/chrome_icon.png")
    chrome_icon_image = chrome_icon_image.resize((40, 40))  # Adjust size as needed

    powerpoint_icon_image = Image.open("Images/powerpoint_icon.png")
    powerpoint_icon_image = powerpoint_icon_image.resize((40, 40))  # Adjust size as needed

    recycle_bin_icon_image = Image.open("Images/recycle_bin_icon.png")
    recycle_bin_icon_image = recycle_bin_icon_image.resize((40, 40))  # Adjust size as needed

    # Convert the resized images to Tkinter-compatible format
    notepad_icon_photo = ImageTk.PhotoImage(notepad_icon_image)
    calc_icon_photo = ImageTk.PhotoImage(calc_icon_image)
    chrome_icon_photo = ImageTk.PhotoImage(chrome_icon_image)
    powerpoint_icon_photo = ImageTk.PhotoImage(powerpoint_icon_image)
    recycle_bin_icon_photo = ImageTk.PhotoImage(recycle_bin_icon_image)

    # Create buttons with desktop app icons and place them inside the bottom label
    btn_notepad_icon = tk.Button(bottom_label, image=notepad_icon_photo, command=launch_notepad, bd=0)
    btn_notepad_icon.image = notepad_icon_photo  # Keep a reference to avoid garbage collection
    btn_notepad_icon.place(x=10, y=5)

    btn_calc_icon = tk.Button(bottom_label, image=calc_icon_photo, command=launch_calculator, bd=0)
    btn_calc_icon.image = calc_icon_photo  # Keep a reference to avoid garbage collection
    btn_calc_icon.place(x=60, y=5)

    btn_chrome_icon = tk.Button(bottom_label, image=chrome_icon_photo, command=launch_chrome, bd=0)
    btn_chrome_icon.image = chrome_icon_photo  # Keep a reference to avoid garbage collection
    btn_chrome_icon.place(x=110, y=5)

    btn_powerpoint_icon = tk.Button(bottom_label, image=powerpoint_icon_photo, command=launch_powerpoint, bd=0)
    btn_powerpoint_icon.image = powerpoint_icon_photo  # Keep a reference to avoid garbage collection
    btn_powerpoint_icon.place(x=160, y=5)

    btn_recycle_bin_icon = tk.Button(bottom_label, image=recycle_bin_icon_photo, command=launch_recycle_bin, bd=0)
    btn_recycle_bin_icon.image = recycle_bin_icon_photo  # Keep a reference to avoid garbage collection
    btn_recycle_bin_icon.place(x=210, y=5)

    # Create a Calendar widget
    calendar = Calendar(new_window, selectmode="day", date_pattern="yyyy-mm-dd")
    calendar.place(x=1000, y=450)  # Adjust the coordinates as needed

    new_window.mainloop()

def make_transparent(image):
    # Create a mask to make white background transparent
    mask = Image.new("L", image.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.rectangle([0, 0, image.width, image.height], fill=255)

    # Apply the mask to the image
    image.putalpha(mask)

    return image

