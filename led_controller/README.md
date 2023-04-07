# led_controller

Copy the service to the correct location:

`sudo cp /home/pi/e5p/led_controller/led_controller.service.example /etc/systemd/system/led_controller.service`

Enable the service to start at boot:

`sudo systemctl enable led_controller`

To see the status or start/stop/restart the service manually:

`sudo systemctl status|start|stop|restart led_controller`
