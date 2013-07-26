import sys, getopt
import time
import struct
import os

from LEDFont import LEDFont

system = os.name

com = None

X_MAX = 128
Y_MAX = 8

_dispBuf = [0] * X_MAX

_font = LEDFont()

def clearDispBuf():
	global _dispBuf
	_dispBuf = [0] * X_MAX
	
def setPixel(col, row, val):
	if val:
		_dispBuf[col] = _dispBuf[col] | (1 << row)
	else:
		_dispBuf[col] = _dispBuf[col] & ~(1 << row)
		
def sendData(data):
	if com != None:
		b = com.write(bytes(data))
		res = com.read()
		if res != '#':
			print "Error writing display buffer!"
		
def sendDisplay():
	sendData('d' + ''.join(chr(c) for c in _dispBuf))
	
def drawRow(row):
	for x in range(0, X_MAX):
		setPixel(x, row, True)
			
def drawCol(col):
	_dispBuf[col] = 255;
			
def setCol(col, val):
	if col < X_MAX:
		_dispBuf[col] = val

def setColFromChar(col, char):
	setCol(col, ord(char))
	
def printChar(pos, char):
	w = _font.getCharWidth(char)
	data = _font.getCharData(char)
	for col in range(0,w):
		setCol(pos + col, data[col])
	
	return w
		
def printString(pos, string):
	w = 0
	for c in string:
		w = printChar(pos, c)
		#if c == ' ':
		#	pos += w
		#else:
		pos += (w + 1)
		
if system != 'nt':
	if os.getuid() != 0:
		print "Please re-run with sudo"
		raw_input("Press enter to continue...")
		sys.exit()

try:
	import serial.tools
except ImportError, e:
	print "Please install pyserial!"
	sys.exit()

from serial.tools import list_ports 

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
		com = serial.Serial(port, baud, timeout=1);
		print "Waiting for display to reboot..."
		time.sleep(3)
		print "Connected to " + port + " @ " + str(baud) + " baud"
		com.flushInput()
except serial.SerialException, e:
	print "Unable to connect to the given serial port!\r\nTry the --list option to list available ports."
	print e
	sys.exit()

try:

	clearDispBuf()
	printString(0, "Hello World!")
	sendDisplay()
	
	# while True:
		# clearDispBuf()
		# for x in range(0, X_MAX):
			# clearDispBuf()
			# drawCol(x)
			# sendDisplay()
		
		# for y in range(0, Y_MAX):
			# clearDispBuf()
			# drawRow(y)
			# sendDisplay()
	
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
except serial.SerialTimeoutException:
	print "Timeout sending sync data! Please check your serial connection"
	sys.exit()

