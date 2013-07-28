import threading

class stopThread(threading.Thread):
	def __init__(self):
		super(stopThread, self).__init__()
		self._stop = threading.Event()

	def stop(self):
		self._stop.set()

	def _stopped(self):
		return self._stop.isSet()	




