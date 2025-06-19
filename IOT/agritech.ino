#include <ESP8266WiFi.h>
//#include "DHT.h"

//#define DHTPIN D1
//#define DHTTYPE DHT11
 
int waterpin = A0;
int soilpin = D1;
int raindroppin = D2;
int smokepin = D3;
int firepin = D4;
int irpin = D5;

const char* ssid     = "vivo_1609";
const char* password = "krish.2009";
const char* host = "agriitech.000webhostapp.com";
//DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(115200);
  delay(100);
//  dht.begin();
  Serial.println();
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);
  
  pinMode(waterpin,INPUT);
  pinMode(soilpin,INPUT);
  pinMode(raindroppin,INPUT);
  pinMode(firepin,INPUT);
  pinMode(irpin,INPUT);
  pinMode(smokepin, INPUT);


  WiFi.begin(ssid, password); 
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
 
  Serial.println("");
  Serial.println("WiFi connected");  
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
  Serial.print("Netmask: ");
  Serial.println(WiFi.subnetMask());
  Serial.print("Gateway: ");
  Serial.println(WiFi.gatewayIP());
}
void loop() {
 
  int watervalue = analogRead(waterpin);
  int soilvalue = digitalRead(soilpin);
  int raindropvalue = digitalRead(raindroppin);
  int firevalue = digitalRead(firepin);
  int irvalue = digitalRead(irpin);
  int smokevalue = digitalRead(smokepin);
  int device_id;
  
 

  delay(5000);
  const int httpPort = 80;

//-----------------------------------------------------------------------------------------------------------------
//water level start
  WiFiClient client1;
  
  if (!client1.connect(host, httpPort)) {
    Serial.println("connection failed");
    return;
  }
  
  String url1 = "/API/waterlevelapi.php?wl_value=" + String(watervalue);
  Serial.print("Requesting URL: ");
  Serial.println(url1);
  
  client1.print(String("GET ") + url1 + " HTTP/1.1\r\n" +
               "Host: " + host + "\r\n" + 
               "Connection: close\r\n\r\n");
  delay(500);
  
  while(client1.available()){
    String line = client1.readStringUntil('\r');
    Serial.print(line);
  }
  if(watervalue>=300){

    WiFiClient client11;
  
    if (!client11.connect(host, httpPort)) {
      Serial.println("connection failed");
      return;
    }

    String watersmsurl ="https://agriitech.000webhostapp.com/API/WaterSMS.php";
    Serial.print("SMS URL:");
    Serial.println(watersmsurl);

  
  
  client11.print(String("GET ") + watersmsurl + " HTTP/1.1\r\n" +
               "Host: " + host + "\r\n" + 
               "Connection: close\r\n\r\n");
  delay(500);
  
  while(client11.available()){
    String line11 = client11.readStringUntil('\r');
    Serial.print(line11);
  }


  }
 //water level ends
 //---------------------------------------------------------------------------------------------------------------------------
 //soil start
WiFiClient client2;
  
  if (!client2.connect(host, httpPort)) {
    Serial.println("connection failed");
    return;
  }
  
  String url2 = "/API/soilapi.php?soil_value=" + String(soilvalue);
  Serial.print("Requesting URL: ");
  Serial.println(url1);
  
  client2.print(String("GET ") + url2 + " HTTP/1.1\r\n" +
               "Host: " + host + "\r\n" + 
               "Connection: close\r\n\r\n");
  delay(500);
  
  while(client2.available()){
    String line = client2.readStringUntil('\r');
    Serial.print(line);
  }

    if(soilvalue==0){

    WiFiClient client12;
  
    if (!client12.connect(host, httpPort)) {
      Serial.println("connection failed");
      return;
    }

    String soilrsmsurl ="https://agriitech.000webhostapp.com/API/SoilSMS.php";
    Serial.print("SMS URL:");
    Serial.println(soilrsmsurl);

  
  
  client12.print(String("GET ") + soilrsmsurl + " HTTP/1.1\r\n" +
               "Host: " + host + "\r\n" + 
               "Connection: close\r\n\r\n");
  delay(500);
  
  while(client12.available()){
    String line12 = client12.readStringUntil('\r');
    Serial.print(line12);
  }
}

 //soil end----------------------------------------------------------------------------------------------------
//rain drop start
WiFiClient client3;
  
  if (!client3.connect(host, httpPort)) {
    Serial.println("connection failed");
    return;
  }
  
  String url3 = "/API/rainapi.php?rain_value=" + String(raindropvalue);
  Serial.print("Requesting URL: ");
  Serial.println(url1);
  
  client3.print(String("GET ") + url3 + " HTTP/1.1\r\n" +
               "Host: " + host + "\r\n" + 
               "Connection: close\r\n\r\n");
  delay(500);
  
  while(client3.available()){
    String line = client3.readStringUntil('\r');
    Serial.print(line);
  }

    if(raindropvalue==0){

    WiFiClient client13;
  
    if (!client13.connect(host, httpPort)) {
      Serial.println("connection failed");
      return;
    }

    String rainsmsurl ="https://agriitech.000webhostapp.com/API/RainSMS.php";
    Serial.print("SMS URL:");
    Serial.println(rainsmsurl);

  
  
  client13.print(String("GET ") + rainsmsurl + " HTTP/1.1\r\n" +
               "Host: " + host + "\r\n" + 
               "Connection: close\r\n\r\n");
  delay(500);
  
  while(client13.available()){
    String line13 = client13.readStringUntil('\r');
    Serial.print(line13);
  }
}


//rain drop end
//-----------------------------------------------------------------------------------------------------
// flame start
WiFiClient client4;
  
  if (!client4.connect(host, httpPort)) {
    Serial.println("connection failed");
    return;
  }
  
  String url4 = "/API/fireapi.php?fire_value=" + String(firevalue)+"device_id=" + String(device_id);
  Serial.print("Requesting URL: ");
  Serial.println(url4);
  
  client4.print(String("GET ") + url4 + " HTTP/1.1\r\n" +
               "Host: " + host + "\r\n" + 
               "Connection: close\r\n\r\n");
  delay(500);
  
  while(client4.available()){
    String line = client4.readStringUntil('\r');
    Serial.print(line);
  }

    if(firevalue==0){

    WiFiClient client14;
  
    if (!client14.connect(host, httpPort)) {
      Serial.println("connection failed");
      return;
    }

    String firesmsurl ="https://agriitech.000webhostapp.com/API/FlameSMS.php";
    Serial.print("SMS URL:");
    Serial.println(firesmsurl);

  
  
  client14.print(String("GET ") + firesmsurl + " HTTP/1.1\r\n" +
               "Host: " + host + "\r\n" + 
               "Connection: close\r\n\r\n");
  delay(500);
  
  while(client14.available()){
    String line14 = client14.readStringUntil('\r');
    Serial.print(line14);
  }
}

//flame end
//-----------------------------------------------------------------------------------------------------
//ir start
WiFiClient client5;
  
  if (!client5.connect(host, httpPort)) {
    Serial.println("connection failed");
    return;
  }
  
  String url5 = "/API/securityapi.php?sec_value=" + String(irvalue);
  Serial.print("Requesting URL: ");
  Serial.println(url5);
  
  client5.print(String("GET ") + url5 + " HTTP/1.1\r\n" +
               "Host: " + host + "\r\n" + 
               "Connection: close\r\n\r\n");
  delay(500);
  
  while(client5.available()){
    String line = client5.readStringUntil('\r');
    Serial.print(line);
  }
    if(irvalue==0){

    WiFiClient client15;
  
    if (!client15.connect(host, httpPort)) {
      Serial.println("connection failed");
      return;
    }

    String Securitysmsurl ="https://agriitech.000webhostapp.com/API/SecuritySMS.php";
    Serial.print("SMS URL:");
    Serial.println(Securitysmsurl);

  
  
  client15.print(String("GET ") + Securitysmsurl + " HTTP/1.1\r\n" +
               "Host: " + host + "\r\n" + 
               "Connection: close\r\n\r\n");
  delay(500);
  
  while(client15.available()){
    String line15 = client15.readStringUntil('\r');
    Serial.print(line15);
  }
}
// ir end
//-----------------------------------------------------------------------------------------------------
//smoke start
WiFiClient client6;
  
  if (!client6.connect(host, httpPort)) {
    Serial.println("connection failed");
    return;
  }
  
  String url6 = "/API/smokeapi.php?smoke_value=" + String(smokevalue);
  Serial.print("Requesting URL: ");
  Serial.println(url6);
  
  client6.print(String("GET ") + url6 + " HTTP/1.1\r\n" +
               "Host: " + host + "\r\n" + 
               "Connection: close\r\n\r\n");
  delay(500);
  
  while(client6.available()){
    String line = client6.readStringUntil('\r');
    Serial.print(line);
  }

  Serial.println();
  Serial.println("closing connection");
  delay(3000);

    if(smokevalue==0){

    WiFiClient client16;
  
    if (!client16.connect(host, httpPort)) {
      Serial.println("connection failed");
      return;
    }

    String smokesmsurl ="https://agriitech.000webhostapp.com/API/SmokeSMS.php";
    Serial.print("SMS URL:");
    Serial.println(smokesmsurl);

  
  
  client16.print(String("GET ") + smokesmsurl + " HTTP/1.1\r\n" +
               "Host: " + host + "\r\n" + 
               "Connection: close\r\n\r\n");
  delay(500);
  
  while(client16.available()){
    String line16 = client16.readStringUntil('\r');
    Serial.print(line16);
  }
}
}