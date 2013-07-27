import sys, getopt
import time
import struct
import os

from LEDFont import LEDFont

class HT1632:
	def __init__(self, dev="COM4", baud=115200):
		self.dev = dev
		self.baud = baud
		self.com = None

		self.X_MAX = 128
		self.Y_MAX = 8

		self._dispBuf = [0] * self.X_MAX
		self._font = LEDFont()

		try:
			import serial.tools
		except ImportError, e:
			raise StandardError("Please install pyserial!")
		
		from serial.tools import list_ports 

		self.serial = serial

	def connect(self):
		self.com = self.serial.Serial(self.dev, self.baud, timeout=1);
		print "Waiting for display to reboot..."
		time.sleep(3)
		print "Connected to " + self.dev + " @ " + str(self.baud) + " baud"
		self.com.flushInput()

	def clearDispBuf(self):
		self._dispBuf = [0] * self.X_MAX
	
	def setPixel(self, col, row, val):
		if val:
			self._dispBuf[col] = self._dispBuf[col] | (1 << row)
		else:
			self._dispBuf[col] = self._dispBuf[col] & ~(1 << row)
		
	def sendData(self, data):
		if self.com != None:
			b = self.com.write(bytes(data))
			res = self.com.read()
			if res != '#':
				print "Error writing display buffer!"
		
	def sendDisplay(self):
		self.sendData('d' + ''.join(chr(c) for c in self._dispBuf))
	
	def drawRow(self, row):
		for x in range(0, self.X_MAX):
			self.setPixel(x, row, True)
			
	def drawCol(self, col):
		self._dispBuf[col] = 255;
			
	def setCol(self, col, val):
		if col < self.X_MAX:
			self._dispBuf[col] = val

	def setColFromChar(self, col, char):
		self.setCol(col, ord(char))
	
	def printChar(self, pos, char):
		w = self._font.getCharWidth(char)
		data = self._font.getCharData(char)
		for col in range(0,w):
			self.setCol(pos + col, data[col])
	
		return w
		
	def printString(self, pos, string):
		w = 0
		for c in string:
			w = self.printChar(pos, c)
			#if c == ' ':
			#	pos += w
			#else:
			pos += (w + 1)
	
