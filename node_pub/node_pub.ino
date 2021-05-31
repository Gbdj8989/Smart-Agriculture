#include<arduino.h>
#include<ESP8266WiFi.h>
#include<PubSubClient.h>
#include"config.h"
#include<DHT.h>

//constants
//In Config file

//globals
WiFiClient wificlient;
PubSubClient client(wificlient);
DHT dht(DHTPIN,DHT11);

//Wifi connection Function
void wifi_connect()
{
    WiFi.disconnect();
    Serial.printf("Connecting to %s\n",ssid);
    WiFi.begin(ssid,pass);
    while(WiFi.status() != WL_CONNECTED)
    {
        Serial.print(".");
        delay(500);
    }
    Serial.print("\nConnected to ");
    Serial.println(WiFi.localIP());
}
//establishing a recconect and initial
void MQTT_connect()
{
    while(!client.connected())
    {
        Serial.println("Attempting MQTT connection...");
        String clientID="IoTLAB-";
        clientID+=String(random(0xffff),HEX);
        Serial.println(clientID.c_str());
        if(client.connect(clientID.c_str()))
        {
            Serial.println("Connected");
        }
        else
        {
            Serial.print("Failed, rc = ");
            Serial.println(client.state());
            delay(5000);
        }
    }
}
void setup()
{
    Serial.begin(9600);
    wifi_connect();
    client.setServer(mqtt_broker,port);
}
void loop()
{
    if(!client.connected())
        MQTT_connect();
    client.loop();


    //Humidity and temperature data
    float h = dht.readHumidity();
    float t = dht.readTemperature();
    Serial.print("Humidity: ");
    Serial.print(h);
    Serial.println(" %");
    Serial.print("Temperature: ");
    Serial.print(t);
    Serial.println(" *C");

    // Soil moisture data
    int soilMoisture=analogRead(0);
    soilMoisture=map(soilMoisture,890,670,0,100);  //Data to be calibarated for mapping purpose.
    Serial.print("Soil Moisture Percentage : ");
    Serial.print(soilMoisture);
    Serial.println("%");

   //Publishing into MQTT server
    if(!client.publish("node1/humidity",String(h).c_str()))
    {
        Serial.println("Humidity Data not published");
    }
    if(!client.publish("node1/temperature",String(t).c_str()))
    {
        Serial.println("Temperature Data not published");
    }
    if(!client.publish("node1/soilMoisture",String(soilMoisture).c_str()))      
    {
        Serial.println("Soil Moisture data published");
    }
    


    //optional delay 
    delay(2000);
    
    
}