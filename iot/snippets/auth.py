#make sure that you installed your requirements and activated the venv
import paho.mqtt.client as mqttc
import random

client = mqttc.Client("Lamp")

# Auth: make sure that your broker has included these credentials
# Follow the steps using mosquitto_passwd and declaring the file 
# to your broker using the configuration file option for passwords
client.username_pw_set("user", "mySuperPassword")

client.connect("mqtt.eclipse.org", 1883, 60)
payld = str(random.randint(1,100))
# 3. Remove this line and the stop line and see if the QoS 1 and 2 are supported
client.loop_start()
ret = client.publish(args.topic, payload=payld, qos=args.qos)
if not ret.is_published(): 
    ret.wait_for_publish()
    client.loop_stop()
    print("Mission accomplished")
    client.disconnect(reasoncode=0)
else:
    print("Something went wrong")
    client.disconnect(reasoncode=1)    