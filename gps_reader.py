# Arquivo: gps_reader.py

import serial
import time

def read_gps_speed(port='COM3'):
    serial_port = serial.Serial(port, 9600, timeout=1)

    while True:
        gps_data = serial_port.readline().decode('utf-8')

        if 'GPRMC' in gps_data:
            data_elements = gps_data.split(',')
            speed_knots = float(data_elements[7])
            speed_kph = speed_knots * 1.852
            return speed_kph

        time.sleep(1)
