#!/usr/bin/env python3
import argparse
import paho.mqtt.client as mqttc
# Read the host address and port number of the broker
# You can add other parameters to make the code more useful

parser = argparse.ArgumentParser()
parser.add_argument("--broker", "-b", default="localhost", help="IP address of the broker", type=str)
parser.add_argument("--port", "-p", default=1883, help="Port number of the broker", type=int)
parser.add_argument("--user", "-u", default="", help="Login for your broker [Optional]", type=str)
parser.add_argument("--password", "-P", help="Password for your broker [Optional]", type=str)
parser.add_argument("--topic", "-t", default="test", help="Topic to subscribe to", type=str)
parser.add_argument("--serial", "-s", default="/dev/ttyACM0", help="Serial path to Arduino", type=str)

args = parser.parse_args()

# Callback for the CONNACK from the server
def connect_callback(client, userdata, flags, rc, properties=None):
    print("Connected to server with code "+str(rc))
    print(mqttc.connack_string(rc))
    pass

# The callback for when a PUBLISH message is received from the server.
def message_callback(client, userdata, msg):
    print(msg.topic,msg.payload)
    pass
    

if __name__== "__main__" :
    client = mqttc.Client("Security_Controler")
    client.on_connect = connect_callback
    client.on_message = message_callback
    #Auth: avoid hard coded and use these if valid (from the CLI, not for the broker)
     # Checking if parameters are valid usig XOR operator (^). 
    # Our logic: Continue IFF both of these statements below are false or both are true
    if (len(args.user)==0) ^ (args.password is None) :
        print('Set either user and password or none of them!')
        exit(1)
    else:
        client.username_pw_set(args.user, args.password)
    
    client.connect(args.broker, args.port, keepalive=120)
    #client.subscribe(args.topic)
    client.subscribe("emergency")
    try:
        client.loop_forever()
        
    except KeyboardInterrupt:
        # Try the following line and tell me what it does to the server
        client.disconnect(reasoncode=0)
        print("Quitting...")