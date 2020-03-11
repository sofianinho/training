#include <ESP8266WiFi.h>
#include "EspMQTTClient.h" //using the EspMQTTClient library

EspMQTTClient client(
  "AccessPoint",
  "PassWord",
  "192.168.1.24",  // MQTT Broker server ip
  "ESP8266"      // Client name that uniquely identify your device
);

int ledPin = 0; //using GPIO0 tu control the LED
void setup() {
  pinMode(ledPin, OUTPUT); 
}

void onConnectionEstablished() {

  client.subscribe("home/esp", [] (const String &payload)  {
    Serial.println(payload);
  });

  client.publish("home/esp", "Hello from ESP!");
}

void loop() {
  client.loop();
  digitalWrite(ledPin, HIGH); // sets the LED on
  client.publish("home/esp", "LED On");
  delay(2000);                // waits for a second
  digitalWrite(ledPin, LOW);  // sets the LED off
  delay(2000); 
  client.publish("home/esp", "LED Off");
}
