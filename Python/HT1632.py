import sys, getopt
import time
import struct
import os
import threading

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

		self._curString = ""
		self._curStringW = 0
		self._curStringPos = 0
		self._curStringDir = -1

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

		#self.dispUpdater.start()

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
		if pos + w < 0:
			return w
		data = self._font.getCharData(char)
		for col in range(0,w):
			if pos + col >= 0 and pos + col < self.X_MAX:
				self.setCol(pos + col, data[col])
	
		return w
		
	def printString(self, pos, string):
		w = 0
		for c in string:
			w = self.printChar(pos, c)
			pos += (w + 1)

	def getStringWidth(self, string):
		return self._font.getStringWidth(string)

	def setCurrentString(self, string, pos, center=False):
		self._curString = string
		self._curStringW = self.getStringWidth(self._curString)
		self._curStringPos = pos
		if center and self._curStringW < self.X_MAX:
			self._curStringPos = (self.X_MAX - self._curStringW) / 2
	
	def scrollCurrentString(self):
		self.clearDispBuf()
		self.printString(self._curStringPos, self._curString)
		self.sendDisplay()

		self._curStringPos = self._curStringPos - 1
		if self._curStringPos + self._curStringW <= 0:
			self._curStringPos = self.X_MAX - 1

		return self._curStringPos

	def bounceCurrentString(self):
		self.clearDispBuf()
		self.printString(self._curStringPos, self._curString)
		self.sendDisplay()
		self._curStringPos = self._curStringPos + self._curStringDir
		if self._curStringW > self.X_MAX:
			if self._curStringDir == -1 and self._curStringPos + self._curStringW < self.X_MAX:
				self._curStringDir = 1
			elif self._curStringDir == 1 and self._curStringPos >= 1:
				self._curStringDir = -1
		else:
			if self._curStringPos <= 0:
				self._curStringDir = 1
			elif self._curStringPos + self._curStringW > self.X_MAX:
				self._curStringDir = -1

		return self._curStringPos