# MQTT tutorial and project

We will build an end to end IoT application that ties together several aspects of the MQTT protocol:
- Publish/Subscribe
- Securing the broker
- Making use of the different options of the protocol: QoS, Last will, persistance
We will use two open source projects from the Eclipse foundation: Mosquito for the broker and Paho for the client library. You will use your Arduino kits to upload metrics through your Raspberry Pis using MQTT. 

In this tutorial, you will see `Discover` if you should play around and see the documentation or test. You will see `Action` if you should run a command, write a program, or something similar.

## General setup

In this first section, we will setup our systems to play with MQTT and IoT

### Prepare your system

`Action` 
- Your raspberrypi:

Take your raspbian OS from [this link](https://www.raspberrypi.org/downloads/raspbian/). Use one of `dd` on linux (use the [instructions here](https://www.raspberrypi.org/documentation/installation/installing-images/linux.md)) or
[Balena Etcher](https://www.balena.io/etcher/) (all platforms) to burn the image on the SD card.

Connect your raspberrypi using the default credentials "pi"/"raspberry" on your device. You can use SSH or connect it to a screen.

- Update and install new packages

Here we are going to install packages in the `apt.txt` (system) and `requirements.txt` for python3

```
# Update lists
sudo apt update -qq
# Upgrade packages
sudo apt upgrade -y
# Install necessary packages
for p in $(cat ./apt.txt); do sudo apt install $p; done
# Install python3 libraries
pip3 install -r requirements.txt
``` 
- Test your installation

These commands should work

```
mosquitto --help
pip3 show paho-mqtt
``` 


### Getting to know and use Mosquito

`Discover`
- Mosquitto service

What is the status of the mosquitto service on you system ? and use two different commands to know this information. A bit of help for the second one: your program listens on a well known service port...

- Systemd

Use these two commands and get to know how the system and mosquitto are linked

```
# Systemd status 
systemctl status mosquitto.service
# The package installed
dpkg -s mosquitto 
``` 

The `mosquito.service` is under `/usr/lib/systemd/system/mosquitto.service`. What configuration file is used by your system for mosquitto ? what are the additional information given by the dpkg command earlier ?

Does the systemd Unit file contains special instructions for hot reload ? what is it used for ?

### Configuration file

`Discover`
- Where is the default location of your config file ? and what is the folder `conf.d` used for ?

- What linux command should I use to understand the content of the file and parameters

- Change the listening port from the default one to 9999 and reload your mosquitto app and use `lsof` to check that it works

`Action`

- Write your first configuration file following these steps:
    - Find the complete example file in the documentation of your system
    - Put the smallest set of instructions to start mosquitto correctly. Take inspiration from the default file
    - Change the default location for logging

### Use the command line

`Discover`

- What are all the tools linked to mosquitto that we installed earlier
- If I want to publish a message, which command do I use ? same question if I want to sbscribe to a topic ?
- What is the `mosquitto_passwd` used for ?
- What are the options available to us in the command line with each program

`Action`

- Start the mosquitto broker using your configuration file
- Publish a random value in the broker. Decide of the topic you want (example: `myTopic`)
```
#Use this command to generate a random value each time
echo $RANDOM
``` 
- Subscribe to the topic you created before. Have you received that message ? why ?
- Let's publish another random value. What happened at the susbscriber side.
- Let's stop the broker. What happened to previous connections ? what if a new connection is attempted.


### Observe the packets

`Action`

Let's redo the previous actions with the mosquitto programs and observe what happened with wireshark (also tshark or tcpdump to save power in you raspberrypi)


### Setup of basic auth and more

### Installing a mobile application for MQTT

## Writing our client program

### Getting to know Paho 

### Writing your publish and subscribe programs

### Last will, reconnection, persistance

### Setting up options for QoS 1 and QoS 2

## Using the kit

### See the examples given in the Arduino folder

### Read the metrics from RPi

### Integration