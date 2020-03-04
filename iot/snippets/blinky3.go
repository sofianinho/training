package main

import (
	"machine"
	"time"
)

// ledOn turns on a LED and waits for 1 second
func ledOn(pinNum int) {
	var led machine.Pin = machine.Pin(pinNum)
	led.Configure(machine.PinConfig{Mode: machine.PinOutput})
	println("-")
	led.High()
	time.Sleep(time.Millisecond * 1000)
}

// ledOff turns on a LED and waits for 1 second
func ledOff(pinNum int) {
	var led machine.Pin = machine.Pin(pinNum)
	led.Configure(machine.PinConfig{Mode: machine.PinOutput})
	println("-")
	led.Low()
	time.Sleep(time.Millisecond * 1000)

}

func main() {
	var tab = []int{3, 5, 6}
	var i int
	for {
		ledOff(tab[i%3])
		i = i + 1
		ledOn(tab[i%3])
		i = i + 1
		ledOn(tab[i%3])
	}
}
