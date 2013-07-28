import threading
import stop_thread
import time

class row_col_demo(stop_thread.stopThread):
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

import urllib2
class mainframe(stop_thread.stopThread):
	def __init__(self, disp, step=128):
		super(mainframe, self).__init__()
		self.disp = disp
		self.step = step	

	def run(self):
		try:
			rand_data = urllib2.urlopen("http://www.random.org/cgi-bin/randbyte?nbytes=12800&format=f").read()
			while not self._stopped():
				steps = range(0, len(rand_data), self.step)
				shift = steps.pop()
				while steps and not self._stopped():
					count = 0
					for c in rand_data[shift:128+shift]:
						self.disp.setColFromChar(count, c)
						count += 1
					shift = steps.pop()
					self.disp.sendDisplay()
					time.sleep(0.5)
		except urllib2.URLError, e:
			print "Error fetching random data."
			print e
		





