import threading
import disp_thread
import time

class row_col_demo(disp_thread.dispThread):
	def __init__(self, disp):
		super(row_col_demo, self).__init__()
		self.disp = disp	

	def run(self):
		while not self._stopped():
			self.disp.clearDispBuf()
			for x in range(0, self.disp.X_MAX):
				 self.disp.clearDispBuf()
				 self.disp.drawCol(x)
				 self.disp.sendDisplay()
		
			for y in range(0, self.disp.Y_MAX):
				 self.disp.clearDispBuf()
				 self.disp.drawRow(y)
				 self.disp.sendDisplay()

class scroll_text(disp_thread.dispThread):
	def __init__(self, disp, pos, text=""):
		super(scroll_text, self).__init__()
		self.disp = disp
		self.text = text
		self.pos = pos	
		if self.text == "":
			self.getInput()

	def getInput(self):
		self.text = raw_input("Text to scroll: ")

	def run(self):
		self.disp.setCurrentString(self.text, self.pos)
		while not self._stopped():
			self.disp.scrollCurrentString()
			#time.sleep(0.1)

class bounce_text(disp_thread.dispThread):
	def __init__(self, disp, pos, text=""):
		super(bounce_text, self).__init__()
		self.disp = disp
		self.text = text
		self.pos = pos
		if self.text == "":
			self.getInput()

	def getInput(self):
		self.text = raw_input("Text to bounce: ")

	def run(self):
		self.disp.setCurrentString(self.text, self.pos)
		while not self._stopped():
			self.disp.bounceCurrentString()
			#time.sleep(0.1)

from datetime import datetime
class byte_time(disp_thread.dispThread):
	def __init__(self, disp):
		super(byte_time, self).__init__()
		self.disp = disp	
		self.dt = datetime.now()
		self.dt_string = ""

	def run(self):
		while not self._stopped():
			self.dt = datetime.now()
			dts = self.dt.strftime("%A %B %d %Y %H:%M:%S")
			if dts != self.dt_string:
				self.dt_string = dts
				pos = ( self.disp.X_MAX - len(self.dt_string)) / 2

				self.disp.clearDispBuf()
				for c in self.dt_string:
					self.disp.setColFromChar(pos, c)
					pos = pos + 1
				self.disp.sendDisplay()
			time.sleep(0.1)

class text_time(disp_thread.dispThread):
	def __init__(self, disp):
		super(text_time, self).__init__()
		self.disp = disp	
		self.dt = datetime.now()
		self.dt_string = ""
		self.last_pos = 0

	def run(self):
		first = True
		while not self._stopped():
			self.dt = datetime.now()
			dts = self.dt.strftime("%m/%d/%Y - %H:%M:%S")
			if dts != self.dt_string:
				self.dt_string = dts
				self.disp.setCurrentString(self.dt_string, self.last_pos, first)
				if first:
					first = False
				self.last_pos = self.disp.bounceCurrentString()
			else:
				self.last_pos = self.disp.bounceCurrentString()
			#time.sleep(0.1)


import urllib2
import os
class mainframe(disp_thread.dispThread):
	def __init__(self, disp):
		super(mainframe, self).__init__()
		self.disp = disp	

	def run(self):
		try:
			#rand_data = urllib2.urlopen("http://www.random.org/cgi-bin/randbyte?nbytes=12800&format=f").read()
			rand_data = os.urandom(12800)
			while not self._stopped():
				steps = range(0, len(rand_data), 128)
				shift = steps.pop(0)
				while steps and not self._stopped():
					count = 0
					for c in rand_data[shift:128+shift]:
						self.disp.setColFromChar(count, c)
						count += 1
					shift = steps.pop()
					self.disp.sendDisplay()
					time.sleep(0.3)
		except urllib2.URLError, e:
			print "Error fetching random data."
			print e
		





