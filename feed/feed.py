#!/usr/bin/python
#! -*- coding:utf-8 -*-

import RPi.GPIO as GPIO
import time
import sys,os

def rotate(clockwise = 1, circle=2):
	#11/12/15/16 to step motor 1/2/3/4
	GPIO.setmode(GPIO.BOARD)
	#pins = [17,18,22,23]
	pins = [16,15,12,11]	
	GPIO.setup(pins,GPIO.OUT)
	interval = 0.002

	
	if clockwise == 1:
		pins = [11,12,15,16]

	#圈数，测试发现循环500次为一圈
	for a in range(250 * int(circle)):
		for i in range(len(pins)):
			GPIO.output(pins[i],0)
			if i+1 >= len(pins):
				i = -1
			GPIO.output(pins[i+1],1)
			time.sleep(interval)
	GPIO.cleanup()

def openIt():
	path = getCurPath()
	f = open(path + "/feed.txt","r+")
	num = f.read()
	if num == "":
		num = "0"
	num = int(num) + 1
	if num > 2:
		return
	f.seek(0)
	f.write(str(num))
	f.close()
	rotate(1)
	
def closeIt():
	path = getCurPath()
	f = open(path + "/feed.txt","r+")
	num = f.read()
	if num == "":
		num = "0"	
	num = int(num)
	while (num > 0):
		rotate(0)
		num = num - 1
	f.seek(0)
	f.write(str(num))
	f.close()

def getCurPath():
	path = sys.path[0]
	if os.path.isdir(path):
		return path
	elif os.path.isfile(path):
		return os.path.dirname(path)

if sys.argv[1] == 'open':
	openIt()
elif sys.argv[1] == 'close':
	closeIt()
elif sys.argv[1] == 'feed':
	openIt()
	closeIt()
else:
	rotate(sys.argv[2],sys.argv[3])
