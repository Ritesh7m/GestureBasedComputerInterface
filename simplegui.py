import tkinter as tk
from PIL import Image, ImageTk, ImageDraw
import threading
import time
from create_new_window import create_new_window




def display_message():
    label.config(text="Welcome to Entity", font=("Helvetica", 16), fg="white", bg="black")
    sign_in_button.pack_forget()
    sign_in_button.config(state="disabled", font=("Helvetica", 16), fg="white", bg="black")
    loading_thread = threading.Thread(target=start_loading)
    loading_thread.start()


def start_loading():
    loading_image = Image.open("Images/Loading.png").resize((120, 120))  # Replace "Loading.png" with your image file

    # Make the white background of the image transparent
    loading_image = make_transparent(loading_image)

    loading_icon = ImageTk.PhotoImage(loading_image)

    loading_label = tk.Label(window, image=loading_icon, bd=0, highlightthickness=0, bg="black")
    loading_label.image = loading_icon
    loading_label.place(x=560, y=140)

    pulse_effect(loading_label, iterations=10, delay=90)

    # Simulate a sign-in process (you can replace this with your actual sign-in logic)
    time.sleep(5)

    # Hide the current window
    window.iconify()

    # Create a new window with the same background (in the main thread)
    window.after(100, create_new_window)

def pulse_effect(widget, iterations=20, delay=90):
    for _ in range(iterations):
        widget.place_forget()
        widget.update_idletasks()
        time.sleep(delay / 1000)
        widget.place(x=560, y=130)
        widget.update_idletasks()
        time.sleep(delay / 1000)


def make_transparent(image):
    # Create a mask to make white background transparent
    mask = Image.new("L", image.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.rectangle([0, 0, image.width, image.height], fill=255)

    # Apply the mask to the image
    image.putalpha(mask)

    return image

# Function to update the clock
def update_clock():
    current_time = time.strftime("%H:%M:%S")
    clock_label.config(text=current_time)
    window.after(1000, update_clock)  # Update every second

# Create the main window
window = tk.Tk()
window.title("The Entity")
window.geometry("1250x1200")

# Load background image
bg_image = Image.open("Images/BGImage.jpg")
bg_image = ImageTk.PhotoImage(bg_image)

canvas = tk.Canvas(window, width=1250, height=1200)
canvas.grid(row=0, column=0)
canvas.create_image(0, 0, anchor=tk.NW, image=bg_image)

# Create a label widget for clock
clock_label = tk.Label(window, font=("Helvetica", 14), fg="white", bg="black")
clock_label.place(x=1150, y=10)

# Update the clock
update_clock()

# Create a label widget
label = tk.Label(window, text="Click the 'Sign In' button to start loading", font=("YourGlitchyFont", 16), fg="white",
                 bg="black")
label.grid(row=0, column=0, pady=(0, 65))

# Create a "Sign In" button
sign_in_button = tk.Button(window, text="Sign In", command=display_message, font=("YourGlitchyFont", 16), fg="white",
                           bg="black")
sign_in_button.grid(row=0, column=0, pady=10)

# Configure row and column weights for centering
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)



# Start the GUI event loop
window.mainloop()


