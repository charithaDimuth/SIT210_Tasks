import RPi.GPIO as GPIO
import tkinter as tk

# GPIO Pin Setup
GPIO.setmode(GPIO.BCM)

LED_PINS = {'Red': 17, 'Green': 27, 'Blue': 22}

for pin in LED_PINS.values():
    GPIO.setup(pin, GPIO.OUT)

# Create PWM instance for each LED
pwm_leds = {}
for color, pin in LED_PINS.items():
    pwm_leds[color] = GPIO.PWM(pin, 1000)  # Frequency 1000Hz
    pwm_leds[color].start(0)

# Function to change brightness of selected LED using PWM
def change_brightness(color, val):
    pwm_leds[color].ChangeDutyCycle(float(val))

# Function to safely exit GUI and clean GPIO settings
def exit_app():
    for pwm in pwm_leds.values():
        pwm.stop()
    GPIO.cleanup()
    window.destroy()

# GUI Window Setup
window = tk.Tk()
window.title("LED Brightness Control GUI")
window.geometry("300x300")
window.configure(bg='lightblue')

label = tk.Label(window, text="Adjust LED Brightness", font=("Arial", 14), bg='lightblue')
label.pack(pady=10)

# Create Sliders for Red, Green, Blue LEDs
for color in LED_PINS.keys():
    slider = tk.Scale(window, from_=0, to=100, orient=tk.HORIZONTAL, label=color,
                     command=lambda val, c=color: change_brightness(c, val))
    slider.pack()

# Exit Button
tk.Button(window, text="Exit", command=exit_app, font=("Arial", 12), bg='red', fg='white').pack(pady=20)

# Run the GUI loop
window.mainloop()
