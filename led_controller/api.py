import requests
from config import ip, port

def fetch_printer():
    printer_response = requests.get("http://%s:%s/api/printer" % (ip, port))
    data = printer_response.json()

    return {
        # Temperature values
        "extruder_temp": int(data["temperature"]["tool0"]["actual"]),
        "extruder_temp_target": int(data["temperature"]["tool0"]["target"]),
        "heater_bed_temp": int(data["temperature"]["bed"]["actual"]),
        "heater_bed_temp_target": int(data["temperature"]["bed"]["target"]),

        # Printer state values (boolean)
        "operational": int(data["state"]["flags"]["operational"]),
        "paused": int(data["state"]["flags"]["paused"]),
        "printing": int(data["state"]["flags"]["printing"]),
        "cancelling": int(data["state"]["flags"]["cancelling"]),
        "pausing": int(data["state"]["flags"]["pausing"]),
        "error": int(data["state"]["flags"]["error"]),
        "ready": int(data["state"]["flags"]["ready"]),
        "closedOrError": int(data["state"]["flags"]["closedOrError"])
    }
