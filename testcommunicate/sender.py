import serial
import time
import struct
import random
import numpy as np
from datetime import datetime

ser = serial.Serial(port='COM4',
                    baudrate = 9600,
                    parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_TWO,
                    bytesize=serial.EIGHTBITS,
                    timeout=0.2)

# data type
# header1, header2, hour, minute, second, millisecond, roll, pitch, yaw, rollSpeed, pitchSpeed, yawSpeed, Xaccel, Yaccel, Zaccel, 위도, 경도, 고도 , checksum

while True:
    header_list = [1, 2]
    now = datetime.now()
    time_string = now.strftime("%H:%M:%S.%f")[:-4]
    strt_list = [now.strftime("%H"), now.strftime("%M"), now.strftime("%S"), now.strftime("%f")[:-4]]
    time_list = list(map(float, strt_list))
    float_list = [10.11, 20.22, 30.33, 100.11, 200.11, 300.11, 1.02, 0.92, 4.22, 37.3840, 126.6571, 90.85]
    for i in range(len(float_list)-3):
        float_list[i] += random.uniform(-1, 1)
    for i in range(len(float_list)-9):
        float_list[i+9] += random.uniform(-0.01, 0.01)
    data_list = header_list+time_list+float_list
    checksum = sum(float_list)
    data_list.append(checksum)

    byte_list=[]
    for f in data_list:
    int_value = int(f * (10 ** 6))
    byte = int_value.to_bytes(4, byteorder='big')
    byte_list.append(byte)

    packed_bytes = struct.pack('>{}f'.format(len(data_list)), *data_list)
    ser.write(packed_bytes) 
    print(packed_bytes)
    time.sleep(0.01)