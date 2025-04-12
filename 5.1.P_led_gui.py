import RPi.GPIO as GPIO
import tkinter as tk
from tkinter import Radiobutton

# GPIO setup
GPIO.setmode(GPIO.BCM)

# Define LED pins
LED_PINS = {
    'Red': 17,     # GPIO 17
    'Green': 27,   # GPIO 27
    'Blue': 22     # GPIO 22
}

# Set pins as output
for pin in LED_PINS.values():
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

# Function to turn on selected LED
def turn_on_led():
    selected_color = led_var.get()
    for color, pin in LED_PINS.items():
        if color == selected_color:
            GPIO.output(pin, GPIO.HIGH)
        else:
            GPIO.output(pin, GPIO.LOW)

# Function to exit the app safely
def exit_app():
    GPIO.cleanup()
    window.destroy()

# Create main window
window = tk.Tk()
window.title("LED Control GUI")
window.geometry("300x200")
window.configure(bg='lightblue')

# Radio buttons variable
led_var = tk.StringVar()

# Label
label = tk.Label(window, text="Select LED to Turn On", font=("Arial", 14), bg='lightblue')
label.pack(pady=10)

# Create radio buttons for Red, Green, Blue LEDs
for color in LED_PINS.keys():
    Radiobutton(window, text=color, variable=led_var, value=color,
                command=turn_on_led, font=("Arial", 12), bg='lightblue').pack()

# Exit button
exit_button = tk.Button(window, text="Exit", command=exit_app, font=("Arial", 12), bg='red', fg='white')
exit_button.pack(pady=20)

# Run the GUI loop
window.mainloop()
