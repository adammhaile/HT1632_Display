#include <stdlib.h>
#include "MatrixDisplay.h"
#include "DisplayToolbox.h"
//#include "font.h"

//Ethernet Setup
#include <SPI.h>
#include <Ethernet.h>

#include <EEPROM.h>
#include "Config.h"

//DEFINES
#define MAXMSG 129
#define MAXCHAR MAXMSG - 1

// Macro to make it the initDisplay function a little easier to understand
#define setMaster(dispNum, CSPin) initDisplay(dispNum,CSPin,true)
#define setSlave(dispNum, CSPin) initDisplay(dispNum,CSPin,false)
//****************

//GLOBALS
byte mac[] = { 0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED };

unsigned long _updateRef = 0;

bool _updateAvailable = false;

unsigned long _dispStartTime = 0;

uint8_t _dispBuf[MAXCHAR];

// Prepare boundaries
uint8_t X_MAX = 0;
uint8_t Y_MAX = 0;

//****************

//GLOBAL OBJECTS
EthernetServer server(23); //Ethernet Server Instance
MatrixDisplay disp(4,6,7, false); //Matrix controller
DisplayToolbox toolbox(&disp); //Display tools

//****************

inline uint8_t getMsgLen(char msgtype)
{
	static uint8_t msgLen = 0;
		switch (msgtype)
		{
			case 'd':
				return  MAXCHAR;
			default:
				return MAXCHAR;
		}
}

void GetInput()
{
	static char msgtype = 0;
	int i=0;
	static uint8_t cbuf[MAXCHAR];
	memset(cbuf, 0, MAXCHAR);

	if(Serial.available()){
		msgtype = Serial.read();
		static uint8_t msgLen = 0;
		msgLen = getMsgLen(msgtype);
		while(i<msgLen) {
			if(Serial.available())
				cbuf[i++] = Serial.read();
			//else
			//	_nop();

		}
		Serial.flush();
	}

	/*
	EthernetClient client = server.available();

	if(i==0)
	{
	char c;
	i = 0;
	if(client)
	{
	msgtype = client.read();

	c = client.read();
	while(c != -1 && i<MAXCHAR)
	{
	cbuf[i++] = (byte)c;
	c = client.read();
	} 
	client.flush();
	client.stop(); 

	cbuf[i] = 0;
	}
	}
	*/

	if(i>0)
	{
		if(msgtype == 'd' && i<=MAXCHAR) //display buffer
		{
			//memset(_dispBuf, 0, MAXCHAR);
			memcpy(_dispBuf, cbuf, i);
			_updateAvailable = true;
		}
		/*
		else if(msgtype == 'i')
		{
			memcpy(&IP, &cbuf, 4);
			SaveIP();
		}
		else if(msgtype == 'c') //config
		{
			if(i == sizeof(config_t))
			{
				memcpy(&config, &cbuf, sizeof(config_t));
			}

			SaveConfig();
		}
		*/
	}
}

boolean TimeElapsed(unsigned long ref, unsigned long wait)
{
	unsigned long now = millis();

	if(now < ref || ref == 0) //for the 50 day rollover or first boot
		return true;  

	if((now - ref) > wait)
		return true;
	else
		return false;
}

/*
* Copy a character glyph from the myfont data structure to
* display memory, with its upper left at the given coordinate
* This is unoptimized and simply uses setPixel() to draw each dot.
*/
//void drawChar(uint8_t x, uint8_t y, char c)
//{
//  static uint8_t dots;
//  static uint8_t index;
//  index = pgm_read_byte_near(&index_list[c]);
//  static uint8_t cw;
//  cw = CharWidth(c);
//  static char col;
//  static char row;
//  for (col=0; col< cw; col++) {
//    if((x+col) >= (X_MAX) && (x+col)<(256-cw+1))
//    {
//      break;
//    }
//    dots = pgm_read_byte_near(&font[index][col]);
//    for (row=0; row < 8; row++) {
//      if (dots & (128>>row))   	     // only 8 rows.
//        toolbox.setPixel(x+col, y+row, 1);
//      else 
//        toolbox.setPixel(x+col, y+row, 0);
//    }
//  }
//}

void setup() 
{
	memset(_dispBuf, 170, MAXCHAR);
	_updateAvailable = true;

	Serial.begin(115200);
	Serial.flush();

	//Read the config

	ReadConfig();

	if(config.CheckVal != 7476)
	{
		//RESET SETTINGS
		config.CheckVal = 7476;
		/*
		config.MAC[0] = 0xDE;
		config.MAC[1] = 0xAD;
		config.MAC[2] = 0xBE;
		config.MAC[3] = 0xEF;
		config.MAC[4] = 0xFE;
		config.MAC[5] = 0xED;
		config.IP[0] = 10;
		config.IP[1] = 0;
		config.IP[2] = 1;
		config.IP[3] = 127;
		config.Port = 23;
		*/
		config.ScrollDelay = 45;
		config.DisplayTime = 2000;
		config.Mbrightness = 10;
		config.Pbrightness = 2;
		config.OffTime = 23;
		config.OnTime = 6;
		config.UseMilTime = false;
		config.ShowDate = true;

		//SaveConfig();
	}

	/*IP[0] = 192;
	IP[1] = 168;
	IP[2] = 0;
	IP[3] = 111;
	SaveIP();*/
	ReadIP();

	Ethernet.begin(mac, IP);
	server.begin();

	// Fetch bounds (dynamically work out how large this display is)
	X_MAX = disp.getTotalWidth();
	Y_MAX = disp.getTotalHeight();

	// Prepare displays  
	disp.setMaster(0,5);
	disp.setSlave(1,4);
	disp.setSlave(2,3);
	disp.setSlave(3,2);

	disp.clear();
	disp.syncDisplays();
	toolbox.setBrightness(1);  
}

void UpdateDisplay()
{
	if(_updateAvailable)
	{
		_updateAvailable = false;

		//disp.clear();

		static uint8_t col;
		static uint8_t row;
		static uint8_t dots;
		for (col=0; col< X_MAX; col++) 
		{
			dots = _dispBuf[col];
			for (row=0; row < Y_MAX; row++) {
				if (dots & (128>>row))   	     // only 8 rows.
					toolbox.setPixel(col, row, 1);
				else 
					toolbox.setPixel(col, row, 0);
			}
		}

		disp.syncDisplays();
		
		Serial.print("#"); //So we know the display has been updated
	}
}

void loop() 
{
	//_dispStartTime = millis();
	
	GetInput();

	UpdateDisplay();
	
	//Serial.println(millis() - _dispStartTime, DEC);
}

