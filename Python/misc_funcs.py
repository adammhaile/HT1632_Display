import threading
import stop_thread
import time

class row_col_demo(stop_thread.dispThread):
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

class scroll_text(stop_thread.dispThread):
	def __init__(self, disp, pos, text=""):
		super(scroll_text, self).__init__()
		self.disp = disp
		self.text = text
		self.pos = pos	
		if self.text == "":
			self.requiresInput = self.text != ""

	def getInput():
		self.text = raw_input("Text to scroll: ")

	def run(self):
		w = self.disp.getStringWidth(self.text)
		while not self._stopped():
			self.disp.clearDispBuf()
			self.disp.printString(self.pos, self.text)

			self.pos = self.pos - 1
			if self.pos + w <= 0:
				self.pos = self.disp.X_MAX - 1

			self.disp.sendDisplay()
			#time.sleep(0.1)

import urllib2
import os
class mainframe(stop_thread.dispThread):
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
		





