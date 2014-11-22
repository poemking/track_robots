#!/usr/bin/python
import serial

f=open('data.txt','w')
ser=serial.Serial('/dev/ttyUSB0', 38400 ,timeout = 1)
x=ser.read(1200)
pos1 = x.find("$GPRMC")
pos2 = x.find("\n",pos1)
loc = x[pos1 : pos2]
f.write(loc)
data = loc.split(',')

if data[2]=='v':
	print 'no location found'
else:
	print "Latitude = " +data[3]+data[4]
	print "Longtitude = "+data[5]+data[6]
	print "Speed = " +data[7]
	print "Course = " +data[8]

