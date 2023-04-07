from rpi_ws281x import Color
from led_strips import strip_1, strip_2
from effects import set_color

# Turn on the LED strips manually
# $ sudo python3 /home/pi/e5p/led_controller/turn_on.py

set_color(strip_1, Color(255,255,255))
set_color(strip_2, Color(255,255,255))
