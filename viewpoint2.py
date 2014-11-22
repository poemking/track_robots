#!/usr/bin/python
import cv2.cv as cv
import serial

cv.NamedWindow("Map",1)
ser=serial.Serial('/dev/ttyUSB0', 38400 ,timeout = 1)
rx = 1
ry = 1
xmax = 460
ymax = 360
xlongmin =12022.66655
xlongmax =12021.17505	
ylatmin =2299.408336
ylatmax =2300.052752

while True:
	
	image = cv.LoadImage("map2.jpg",cv.CV_LOAD_IMAGE_COLOR)
	x=ser.read(1200)
	pos1 = x.find("$GPRMC")
	pos2 = x.find("\n",pos1)
	loc = x[pos1 : pos2]
	data = loc.split(',')

	if data[2]=='v':
	  print 'no location found'
	else:
	  print "Latitude = " +data[3]+data[4]
	  print "Longtitude = "+data[5]+data[6]
	  #print "Speed = " +data[7]
	  #print "Course = " +data[8]
	  latact  = float(data[3])
	  longact = float(data[5])
	  rx = xmax-int((longact - xlongmin)/(xlongmax - xlongmin)*xmax)
	  ry = ymax-int((latact  - ylatmin)/(ylatmax - ylatmin)*ymax)
	  t1 = rx,ry
	  br = rx+5 , ry+5
	  cv.Rectangle(image,t1,br,(0,255,0),3)
	  cv.ShowImage("Map",image)
	  if cv.WaitKey(2)==27:
  	    break
