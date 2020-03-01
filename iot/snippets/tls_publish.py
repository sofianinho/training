#!/usr/bin/env python3

# Make sure you followed the security part of the tutorial, you will use those certicates that you generated and the configuration file for your broker


import argparse
import paho.mqtt.client as mqttc
import random
import time
# Read the host address and port number of the broker
# You can add other parameters to make the code more useful

parser = argparse.ArgumentParser()
parser.add_argument("--broker", "-b", default="dev", help="IP address of the broker", type=str)
parser.add_argument("--port", "-p", default=8883, help="Port number of the broker", type=int)
parser.add_argument("--topic", "-t", default="test", help="Topic to subscribe to", type=str)
parser.add_argument("--qos", default=0, help="QoS for the publish function", type=int)


args = parser.parse_args()

conn_flag=False

# Define the callback for publication (something to do once it's done)

def connect_callback(client, userdata, flags, rc):
    global conn_flag
    conn_flag=True
    print("connected")

def publish_callback(client,userdata,mid):
    print("All done publishing mid: ", mid)
    pass

def message_callback(client, userdata, msg):
    print(msg.topic,msg.payload, "QoS: ", msg.qos)
    pass

def log_callback(client, userdata, level, buf):
    print("buffer: ", buf)

def disconnect_callback(client, userdata, rc):
    print("client is disconncted")

if __name__== "__main__" :
    client = mqttc.Client("Secure Lamp")
    client.on_connect = connect_callback
    client.on_publish = publish_callback
    client.on_message = message_callback
    client.on_log = log_callback
    client.on_disconnect = disconnect_callback
    # Auth
    client.username_pw_set("sofiane", "imadali")
    # Last will and testament
    client.will_set("test", payload="Goodbye", qos=0, retain=False)
    # Use TLS
    client.tls_set('./clients/ca.crt')
    # Connect first
    client.connect(args.broker, args.port)
    while not conn_flag:
        time.sleep(1)
        print("reconnecting: ")
        client.loop()
    # 3. Remove this line and the stop line and see if the QoS 1 and 2 are supported
    #client.loop_start()
    payld = str(random.randint(1,100))
    ret = client.publish(args.topic, payload=payld, qos=args.qos)
    if not ret.is_published(): 
        ret.wait_for_publish()
        client.loop_stop()
        client.disconnect(reasoncode=0)
    else:
        client.disconnect(reasoncode=1)    
