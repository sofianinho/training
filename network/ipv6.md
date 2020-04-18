# Internet Protocol version 6 tutorial

In this tutorial, we are going to learn the fundamentals of using IPv6 in our local area network with the Neighbor discovery protocol, and see the global deployment of the next generation of netwokring protocols.

## Prerequisites:

For this tutorial, we need to have a working `Linux (preferably debian-based)` virtual machine with 2 network interfaces.

- If you already have one, ensure that you either one of the following 2 options:
    - You have one interface that is created in `Bridged` mode, and bridged to your host machine's default interface (e.g. your wfi interface)
    - Create an additional private interface, with a private network (e.g. set the 192.168.70.10 address on that interface)

- If you don't have a virtual machine on your system, these are the steps:
    - Install [VirtualBox](https://www.virtualbox.org/wiki/Downloads) and [Vagrant](https://www.vagrantup.com/downloads.html) on your system
    - Create a folder in your workspace called `ipv6_tutorial`
    - Copy the [`Vagrantfile`](./Vagrantfile) of this tutorial inside your `ipv6_tutorial` folder
    - Run `vagrant up` command in the same folder. This will download and boot an Ubuntu 18.04 on your system (about 300MB).
    - While booting up, you are going to be asked which interface you'd like to set as your bridge. Write the number that corrsponds to the default interface (e.g. Wifi) for a better experience of this tutorial.
    - Once the machine finishes booting, you can enter the machine using the command: `vagant ssh` (in the same `ipv6_tutorial` folder). You can type: `ip addr` to check that you have succesfully configured your bridged interface.

## State of IPv6 deployment worldwide

### Activate and deactivate IPv6 in your home CPE

A home Customer Premise Equipment (CPE) is your Internet box (router, Wifi Acces Point). Depending on the menu of your box, you can modify the IPv6 parameters to enable it and disable it. In the following section, I am describing what happens on my Orange Livebox equipment but you are free to experiment with your own Internet provider's CPE equipment. 

#### Checking that IPv6 is enabled

For this test, we are going to use the [test-ipv6](https://test-ipv6.com/) service online in our browser. Please open the page and see the results after it finishes running the tests. Here is a screenshot of my results

- IPv6 disabled on my box
![IPv6 disabled](./images/no-ipv6.png)

- IPv6 enabled on my box
![IPv6 enabled](./images/with-ipv6.png)

In order to see the results of accessing some websites and finding out if they are IPv6 ready, we can use a browser extension. For Firefox, you can use [IPvFoo for Firefox](https://addons.mozilla.org/en-US/firefox/addon/ipvfoo-pmarks/?src=search), and for chrome(or chromium) use [IPvFoo for Chrome](https://chrome.google.com/webstore/detail/ipvfoo/ecanpcehffngcegjmadlcijfolapggal). Here are some screenshots.

- IPv6 only website
![IPv6 only](./images/ipv6-only.png)

- IPv6 and IPv4 website
![IPv6 only](./images/ipv6-and-v4.png)

`Note:`
From the previous test-ipv6 report, you can read that it diagnoses my Internet access as not capable of reaching IPv6 only websites. The screenshot on [this IPv6 only website](https://www.mythic-beasts.com/order/rpi) seems to contradict that. We can also see that my current Internet provider certifies that my IPv6 access is native (no tunneling) [here, since 1st trimester of 2016](https://assistance.orange.fr/livebox-modem/toutes-les-livebox-et-modems/installer-et-utiliser/piloter-et-parametrer-votre-materiel/le-parametrage-avance-reseau-nat-pat-ip/gerer-votre-adresse-ip/ipv6-chez-orange_238184-528413). Probably an unreliable feature of the test-ipv6 website.

### Work with your Linux machine

This part you can do using your VM or your personnal computer for now. `Your box should have IPv6 enabled now`. The commands are going to be Linux-based.

- Get your default egress interface. You can use the result of this command:
`echo  $(ip route get 8.8.8.8|awk -F 'dev ' '{print $2}'|cut -d' ' -f1)`
    - Explain this one-liner scipt ?
- Find your IPv6 configuration for this interface using the `ip -6` command
    - How many IPv6 addresses can you see ?
    - Can you explain why ?

## Fundamentals of the IPv6 protocol on Linux

## Neighbor Discovery protocol

## Scapy and IPv6

## Security
