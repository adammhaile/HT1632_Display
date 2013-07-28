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

menuOpts = [
["Exit", doExit],
["Clear/Stop", doClear],
["Hello World", doHelloWorld],
["Row/Col Demo", doDemo],
["Game of Life", doGameOfLife]
]

def printMenu():
	for i in range(0, len(menuOpts)):
		print str(i) + " - " + menuOpts[i][0]

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

	time.sleep(2)
	
	while True:
		disp.clearDispBuf()
		for x in range(0, disp.X_MAX):
			 disp.clearDispBuf()
			 disp.drawCol(x)
			 disp.sendDisplay()
		
		for y in range(0, disp.Y_MAX):
			 disp.clearDispBuf()
			 disp.drawRow(y)
			 disp.sendDisplay()
	
	# clearDispBuf()
	# for x in range(0, X_MAX):
		# for y in range(0, Y_MAX):
			# setPixel(x, y, (x + y) % 2)
			
	# sendDisplay()
				
	# while 1:
		# data = ''
		# for x in range(0, X_MAX):
			# for y in range(0, Y_MAX):
				
				
		# for shift in range(0, 127):
			# clearDispBuf()
			# for i in range(0 + shift, 128 + shift):
				# setCol(i - shift, i)
			
			# start_time = time.time() * 1000
			# sendDisplay()
			# end_time = time.time() * 1000
			# print("%g ms" % (end_time - start_time))
		
	#b = com.write(bytes("t" + data))
	#res = com.read()
	#if(b > 0 and res == '*'):
	#	print "Success syncing time!"
	#else:
	#	print "There was an error syncing the time! Make sure your clock is in Serial Set Mode"
	#com.close()
except ValueError, e:
	print e
	sys.exit()
