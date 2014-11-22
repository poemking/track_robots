

import serial

ser=serial.Serial('/dev/ttyUSB0',38400,timeout=2)
x=ser.read(1200)
print x
