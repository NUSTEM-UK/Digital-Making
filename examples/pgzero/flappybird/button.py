"""Example button code using GPIOZero.

Run with

    python3 button.py

Interupt with ctrl+c
"""

from gpiozero import Button
from signal import pause  # Not needed when transferred to PyGameZero

button = Button(26) # Button is attached to bottom right corner pins

def button_pressed():
    """Handle 'button pressed' event."""
    print("Hello!")

# Now set up handler for button press, which calls the named function.
button.when_pressed = button_pressed

# The following lines aren't needed once in PyGameZero
print("Listening for button presses. Interup with ctrl+c")
pause()
