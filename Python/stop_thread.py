import threading

class dispThread(threading.Thread):
	def __init__(self):
		super(dispThread, self).__init__()
		self._stop = threading.Event()
		self.requiresInput = False
		self.input = ""

	def stop(self):
		self._stop.set()

	def _stopped(self):
		return self._stop.isSet()	

	def getInput():
		self.input = ""



