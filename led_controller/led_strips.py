from rpi_ws281x import ws, Adafruit_NeoPixel

# Primary LED strip under the X axis extrusion
# / PWM0 / index 0-39
LED_1_COUNT      = 40      # Number of LED pixels
LED_1_PIN        = 18      # GPIO pin (must support PWM)
LED_1_FREQ_HZ    = 800000  # LED signal frequency in Hz (usually 800kHz)
LED_1_DMA        = 10      # DMA channel to use for generating signal (careful)
                           # DMA channels 10 and 11 should be safe for the Raspberry Pi 3 Model B
LED_1_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_1_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_1_CHANNEL    = 0       # Set to 1 for GPIOs 13, 19, 41, 45 or 53

# Secondary LED strip at the printer's base
# / PWM1 / index 0-139 or 0-175 if grid enabled
# BASE_R=[0,42] BASE_F=[43,97] BASE_L=[98,139] LED_GRID=[140,175]
LED_2_COUNT      = 140 # With LED grid disabled
LED_2_COUNT      = 176 # With LED grid enabled
LED_2_PIN        = 13
LED_2_FREQ_HZ    = 800000
LED_2_DMA        = 10
LED_2_BRIGHTNESS = 255
LED_2_INVERT     = False
LED_2_CHANNEL    = 1

strip_1 = Adafruit_NeoPixel(LED_1_COUNT, LED_1_PIN, LED_1_FREQ_HZ, LED_1_DMA, LED_1_INVERT, LED_1_BRIGHTNESS, LED_1_CHANNEL, ws.WS2811_STRIP_GRB)
strip_2 = Adafruit_NeoPixel(LED_2_COUNT, LED_2_PIN, LED_2_FREQ_HZ, LED_2_DMA, LED_2_INVERT, LED_2_BRIGHTNESS, LED_2_CHANNEL, ws.WS2811_STRIP_GRB)

# Initialize LED strips before anything else
strip_1.begin()
strip_2.begin()
