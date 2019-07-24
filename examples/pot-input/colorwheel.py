"""Colour wheel calculations.

Use for NeoPixels, etc. Only works for RGB or GRB neopixels
"""

def wheel(pos):
    # Input a value 0 to 255 to get a colour value.
    # The colours are a transition r - g - b - r.
    # Input is effectively hue angle.

    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos*3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos*3)
        g = 0
        b = int(pos*3)
    else:
        pos -= 170
        r = 0
        g = int(pos*3)
        b = int(255 - pos*3)
    return (r, g, b)