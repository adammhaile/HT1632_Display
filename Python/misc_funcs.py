import threading
import stop_thread

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




