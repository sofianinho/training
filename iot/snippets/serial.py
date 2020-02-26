#make sure that you installed your requirements and activated the venv
import serial 

# tell your system where is the arduino plugged
# you may want to use sudo to access this port
ser = serial.Serial("/dev/ttyACM0", 9600)

# read some value from the serial port
val = ser.readline()

# print it or send it away with mqtt
print(val)

