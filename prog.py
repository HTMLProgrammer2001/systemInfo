import psutil as u
import serial
import json
import time

com = "COM5"

while(1):
    if not com:
        com = input("Enter COM port ")
    
    try:
        s = serial.Serial(com, 9600)
        s.close()
        break;
    except (OSError, serial.SerialException):
        com = ''
    
s = serial.Serial(com, 9600)

while(1):
    battery = u.sensors_battery()
    disk = u.disk_usage

    response = {
        'CPU': str(round(u.cpu_percent())),
        'memory': str(round(u.virtual_memory().percent)),
        'battery': str(battery.percent) + ('+' if battery.power_plugged else '-'),
        'disks': str(round(disk('c:').percent)) + '/' + str(round(disk('d:').percent))
    }
    
    s.write(bytes(json.dumps(response), "ASCII"))
    print(bytes(json.dumps(response), "ASCII"))

    time.sleep(5)
