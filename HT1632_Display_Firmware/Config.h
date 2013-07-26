#include <Arduino.h>
#include <EEPROM.h>

//STRUCTS
struct config_t
{
  uint16_t CheckVal; 	//2
  //byte MAC[6];       	//6
  //byte IP[4];			//4
  //uint8_t Port;			//1
  uint8_t ScrollDelay;	//1	
  uint16_t DisplayTime; //2
  uint8_t Mbrightness;	//1	
  uint8_t Pbrightness;	//1	
  uint8_t OffTime;		//1	
  uint8_t OnTime;		//1	
  boolean UseMilTime;	//1	
  boolean ShowDate;		//1	
  
} config;

byte IP[4];
//****************

//Config Functions
template <class T> int EEPROM_writeAnything(int ee, const T& value)
{
    const byte* p = (const byte*)(const void*)&value;
    int i;
    for (i = 0; i < sizeof(value); i++)
	  EEPROM.write(ee++, *p++);
    return i;
}

template <class T> int EEPROM_readAnything(int ee, T& value)
{
    byte* p = (byte*)(void*)&value;
    int i;
    for (i = 0; i < sizeof(value); i++)
	  *p++ = EEPROM.read(ee++);
    return i;
}


void PrintBool(boolean val)
{
 val ? Serial.print("True") : Serial.print("False"); 
}

void PrintConfig()
{
  Serial.println("Current Configuration");
  Serial.println(sizeof(config_t), DEC);
  Serial.println("*********************************");
  /*Serial.print("IP: ");Serial.print(config.IP[0], DEC);Serial.print(".");
                       Serial.print(config.IP[1], DEC);Serial.print(".");
                       Serial.print(config.IP[2], DEC);Serial.print(".");
                       Serial.println(config.IP[3], DEC);*/
  
  //Serial.print("Port: ");Serial.println(config.Port, DEC);
  Serial.print("Scroll Delay: ");Serial.println(config.ScrollDelay, DEC);
  Serial.print("Display Interval: ");Serial.println(config.DisplayTime, DEC);
  Serial.print("M Bright: ");Serial.println(config.Mbrightness + 1, DEC);
  Serial.print("P Bright: ");Serial.println(config.Pbrightness + 1, DEC);
  Serial.print("Off Time: ");Serial.println(config.OffTime, DEC);
  Serial.print("On Time: ");Serial.println(config.OnTime, DEC);
  Serial.print("Use Mil Time: "); PrintBool(config.UseMilTime); Serial.println("");
  Serial.print("Show Date: "); PrintBool(config.ShowDate); Serial.println("");
  Serial.println("*********************************");
  Serial.println("");
}

void SaveConfig()
{
  PrintConfig();
  EEPROM_writeAnything(0, config);
}

void ReadConfig()
{
  EEPROM_readAnything(0, config);
  PrintConfig();
}

void SaveIP()
{
  EEPROM_writeAnything(sizeof(config_t), IP);
}

void ReadIP()
{
  EEPROM_readAnything(sizeof(config_t), IP);
}
//****************

