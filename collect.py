import serial
import csv
import time
PORT = 'COM3'
DEVICE = '1n5404'
with serial.Serial(PORT, 115200, timeout=2) as ser:
    time.sleep(2)
    with open(f'data/{DEVICE}.csv', 'w', newline='') as f: 
        writer = csv.writer(f)
        writer.writerow(["voltage", "current"])
        for _ in range(256):
            line = ser.readline().decode().strip()
            if ',' in line:
                writer.writerow(line.split(','))
                
print(f'Saved {DEVICE}.csv')