#include <Boards.h>
#include <Firmata.h>

#include <SPI.h>
#include <Ethernet.h>

byte mac[] = {0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED};
byte ip[] = {10, 10, 0, 177};
//byte dns[] = {10, 10, 0, 1};
byte gateway[] = {10, 10, 0, 1};
byte subnet[] = {255, 255, 255, 0};

byte server[] = {174, 120, 97, 7}; //ambrosedigiorgio.com

EthernetClient client;

int value;
void setup() {
  Ethernet.begin(mac, ip, dns, gateway, subnet);
  Serial.begin(9600);
  
  
  Serial.print("Arduino at ");
  Serial.println(Ethernet.localIP());
}



void loop() {
  
  value= analogRead(A0);
  Serial.println(value);
  
       
       updateServer(1);
     
  
}

void updateServer(int value)
{
  char buffer[256];
  
  if (client.connect('localhost', 5000)) {
    Serial.println("Connected");
    sprintf(buffer, "HEAD /arduino.php?GarageDoorStatus=%d HTTP/1.1", value);
    client.println(buffer);
    client.println("Host: ambrosedigiorgio.com");
    client.println("Connection: close");
    client.println();
    client.stop();
  } else {
    Serial.println("Connection failed");
  }
}

