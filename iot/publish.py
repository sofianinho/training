#!/usr/bin/env python3
import argparse
import paho.mqtt.client as mqttc
import random
# Read the host address and port number of the broker
# You can add other parameters to make the code more useful

parser = argparse.ArgumentParser()
parser.add_argument("--broker", "-b", default="localhost", help="IP address of the broker", type=str)
parser.add_argument("--port", "-p", default=1883, help="Port number of the broker", type=int)
parser.add_argument("--topic", "-t", default="test", help="Topic to subscribe to", type=str)
parser.add_argument("--qos", default=0, help="QoS for the publish function", type=int)
parser.add_argument("--serial", "-s", default="/dev/ttyACM0", help="Serial path to Arduino", type=str)

args = parser.parse_args()


# Callback for the CONNACK from the server
def connect_callback(client, userdata, flags, reasonCode, properties):
    print("Connected to server with code "+str(reasonCode))
    pass


# Define the callback for publication (something to do once it's done)
def publish_callback(client,userdata,mid):
    print("All done publishing mid: ", mid)
    pass

def message_callback(client, userdata, msg):
    print(msg.topic,msg.payload, "QoS: ", msg.qos)
    pass

if __name__== "__main__" :
    client = mqttc.Client("Thermometer")
    client.on_connect = connect_callback
    client.on_publish = publish_callback
    client.on_message = message_callback
    # Auth
    # Last will and testament
    client.username_pw_set("publisher", "password")

    client.will_set("emergency","everything is going to explode", qos=0,retain=True)
    client.connect(args.broker, args.port)
    payld = str(random.randint(1,100))
    # 3. Remove this line and the stop line and see if the QoS 1 and 2 are supported
    # client.loop_start()
    ret = client.publish(args.topic, payload=payld, qos=args.qos)
    if not ret.is_published(): 
        ret.wait_for_publish()
        #client.loop_stop()
        #client.disconnect(reasoncode=0)
    else:
        client.disconnect(reasoncode=1)    