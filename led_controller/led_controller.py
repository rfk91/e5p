import time
import threading
import sys
from rpi_ws281x import Color
from api import fetch_printer
from led_strips import strip_1, strip_2
from effects import set_color, turn_off, startup, spotlight

printer = None

def error(*strips):
    print("\nKeyboardInterrupt exception")
    for strip in strips:
        strip.setBrightness(0)
        turn_off(strip)


if __name__ == '__main__':

    def fetch_api(stop_event):
        global printer
        while not stop_event.is_set():
            printer = fetch_printer()
            print("Extruder  " + str(printer["extruder_temp"])   + " / " + str(printer["extruder_temp_target"]))
            print("Bed       " + str(printer["heater_bed_temp"]) + " / " + str(printer["heater_bed_temp_target"]))
            time.sleep(1) # Fetch each second

    def led_1():
        startup(strip_1, Color(255,0,0), 100, [0,39])
        time.sleep(5)
        spotlight(strip_1, Color(255,255,255), 5, [0,39])

    def led_2():
        startup(strip_2, Color(255,0,0), 26, [0,139])
        time.sleep(5)
        spotlight(strip_2, Color(0,0,255), 10, [0,139])

    # Event on keyboard interrupt
    stop_event: threading.Event = threading.Event()

    try:
        turn_off(strip_1)
        turn_off(strip_2)
        time.sleep(1)

        api_thread = threading.Thread(target=fetch_api, args=(stop_event,))
        l1_thread  = threading.Thread(target=led_1)
        l2_thread  = threading.Thread(target=led_2)

        api_thread.start()
        l1_thread.start()
        l2_thread.start()

        api_thread.join()
        l1_thread.join()
        l2_thread.join()

    except KeyboardInterrupt:
        stop_event.set()
        error(strip_1, strip_2)
        sys.exit() # Exit threads?
