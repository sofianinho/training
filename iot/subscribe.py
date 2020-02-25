#!/usr/bin/env python3
import argparse
import paho.mqtt.client as mqttc
import serial 
# Read the host address and port number of the broker
# You can add other parameters to make the code more useful

parser = argparse.ArgumentParser()
parser.add_argument("--broker", "-b", default="localhost", help="IP address of the broker", type=str)
parser.add_argument("--port", "-p", default=1883, help="Port number of the broker", type=int)
parser.add_argument("--topic", "-t", default="test", help="Topic to subscribe to", type=str)
parser.add_argument("--serial", "-s", default="/dev/ttyACM0", help="Serial path to Arduino", type=str)

args = parser.parse_args()
ser = serial.Serial(args.serial, 9600)

# Callback for the CONNACK from the server
def connect_callback(client, userdata, rc):
    print("Connected to server with code "+str(rc))

# The callback for when a PUBLISH message is received from the server.
def message_callback(client, userdata, msg):
    print(msg.topic,msg.payload)
    if msg.payload == b'all' :
        ser.write(b'3')
        ser.write(b'5')
        ser.write(b'6')
    elif msg.payload == b'green' :
        ser.write(b'6')
    pass
    

if __name__== "__main__" :
    client = mqttc.Client("Controler")
    client.on_connect = connect_callback
    client.on_message = message_callback
    #
    client.username_pw_set("haja", "zouj")
    client.connect(args.broker, args.port)
    client.subscribe(args.topic)
    try:
        client.loop_forever()
    except KeyboardInterrupt:
        # Try the following line and tell me what it does to the server
        client.disconnect(reasoncode=0)
        print("Quitting...")