import sys, getopt
import time
import struct
import os

from HT1632 import HT1632

from misc_funcs import *

from GameOfLife import GameOfLife

disp = None

curThread = None

def doExit():
	sys.exit()

def doClear():
	disp.clearDispBuf()
	disp.sendDisplay()

def doHelloWorld():
	disp.clearDispBuf()
	disp.printString(0, "Hello!!!! World!!!!")
	disp.sendDisplay()

def doDemo():
	global curThread
	curThread = row_col_demo(disp)
	curThread.start()

def doGameOfLife():
	global curThread
	curThread = GameOfLife(disp)
	curThread.start()

def doMainframe():
	global curThread
	curThread = mainframe(disp)
	curThread.start()

def doHelloWorldScroll():
	global curThread
	curThread = scroll_text(disp, "Hello World!!!!!! 1 2 3", disp.X_MAX / 2)
	curThread.start()

menuOpts = [
["Exit", doExit],
["Clear/Stop", doClear],
["Hello World", doHelloWorld],
["Hello World Scroll", doHelloWorldScroll],
["Row/Col Demo", doDemo],
["Game of Life", doGameOfLife],
["90s Mainframe", doMainframe]
]

def printMenu():
	for i in range(0, len(menuOpts)):
		print str(i) + " - " + menuOpts[i][0]

#def fireOption(opt):

def handleMenu(choice):
	try:
		i = int(choice)
		if i < len(menuOpts):
			global curThread
			if curThread != None:
				curThread.stop()
				curThread.join()
				curThread = None
			menuOpts[i][1]()
		else:
			raise ValueError()
	except ValueError:
		print "Invalid Option!"

system = os.name

try:
	import serial.tools
except ImportError, e:
	print("Please install pyserial!")
	sys.exit()

from serial.tools import list_ports 

if system != 'nt':
	if os.getuid() != 0:
		print "Please re-run with sudo"
		raw_input("Press enter to continue...")
		sys.exit()

port = ''
baud = 115200
try:
	opts, args = getopt.getopt(sys.argv[1:], "p:b:", ["list",])
except getopt.GetoptError:
	print "sync_time.py -p <COMX> -b <baud_rate>"
	sys.exit()
for opt, arg in opts:
	if opt == '-p':
		print "Port specified: " + arg
		port = arg
	elif opt == '-b':
		try:
			baud = int(arg)
		except ValueError:
			print "Invalid baud rate specified. Must be a integer."
			sys.exit()
	elif opt == '--list':
		ports = [port[0] for port in list_ports.comports()]
		if len(ports) == 0:
			print "No available serial ports found!"
			sys.exit()
		print "Available serial ports:"
		for p in ports:
			print p
		sys.exit()
		

if port == '':
	ports = [port for port in list_ports.comports()]
	if len(ports) > 0:
		if system == 'posix':
			p = ports[len(ports) - 1]
			port = p[0]
		elif system == 'nt':
			p = ports[0]
			port = p[0]
		elif system == 'mac':
			p = ports[len(ports) - 1]
			port = p[0]
		else:
			print "What system are you running?!"
			sys.exit()
		print "No port specified, using best guess serial port:\r\n" + p[1] + ", " + p[2] + "\r\n"
	else:
		print "Cannot find default port and no port given!"
		sys.exit()

try:
		disp = HT1632(port, baud)
		disp.connect()
except serial.SerialException, e:
	print "Unable to connect to the given serial port!\r\nTry the --list option to list available ports."
	print e
	sys.exit()
except StandardError, e:
	print e
	sys.exit()

try:
	while True:
		printMenu()
		i = raw_input("Choice: ")
		handleMenu(i)

except ValueError, e:
	print e
	sys.exit()
