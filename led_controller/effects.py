import time
from rpi_ws281x import Color
from config import primary_color

def set_color(strip, color=primary_color):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
    strip.show()

def turn_off(strip):
    set_color(strip, Color(0,0,0))

def startup(strip, color=primary_color, ms=50, pixels_range=[]):
    pxs = pixels_range[1] - pixels_range[0]
    if pxs % 2 == 0: # Even number of pixels
        centerPx1 = pxs // 2 - 1
        centerPx2 = pxs // 2
    else: # Odd number of pixels
        centerPx1 = centerPx2 = pxs // 2
    for i in range(pxs // 2 + 1):
        strip.setPixelColor(centerPx1 + i, color)
        strip.setPixelColor(centerPx2 - i, color)
        strip.show()
        time.sleep(ms / 1000.0)

def spotlight(strip, color=primary_color, width=1, pixels_range=[]):
    pxs, centerPx1, centerPx2 = calc_pixels_range(pixels_range)
    for i in range(pxs):
        distance_from_center = min(abs(centerPx1 - i), abs(centerPx2 - i))
        brightness = max(0, 255 - (distance_from_center * 255 // width))
        r = (color >> 16) & 0xFF
        g = (color >> 8) & 0xFF
        b = color & 0xFF
        r = r * brightness // 255
        g = g * brightness // 255
        b = b * brightness // 255
        strip.setPixelColor(i, Color(r,g,b))
    strip.show()

def calc_pixels_range(pixels_range=[]):
    pxs = pixels_range[1] - pixels_range[0] + 1
    if pxs % 2 == 0: # Even number of pixels
        centerPx1 = pxs // 2 - 1
        centerPx2 = pxs // 2
    else: # Odd number of pixels
        centerPx1 = centerPx2 = pxs // 2
    return pxs, centerPx1, centerPx2


# TODOOOOOOOOOOOOOOOOOOOOO
