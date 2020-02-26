#make sure that you installed your requirements and activated the venv
#use the standard lib for logging
import logging
import paho.mqtt.client as mqtt

# set the level of information you want
logging.basicConfig(level=logging.DEBUG)

mqttc = mqtt.Client()

logger = logging.getLogger(__name__)
# connect your logger with paho to know the events
mqttc.enable_logger(logger)

#let's connect somewhere where mqtt is given for free
mqttc.connect("mqtt.eclipse.org", 1883, 60)

#This topic always exists, the $SYS is a system topic
mqttc.subscribe("$SYS/#", 0)

mqttc.loop_forever()
