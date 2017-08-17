######################################################################
# PiSensor
#
# Get the temperate, humidity and pressure readings
# Send the readings to the generic receiver rdev.gpsbe.net port 5013 - 
# The generic receiver used for testing new receivers.
# http requests port 5013
#
#
# Use HTTP Requests to send formatted data to port 5013 at rdev.gpsbe.net
#


#import socket
import json
import urllib2

# Define raspPi as True if running on a Raspberry Pi, otherwise False.
raspPi = False

class Sensor:
    temperature = 0;
    pressure = 0;
    humidity = 0;



if raspPi == True:
    from sense_hat import SenseHat

else:
    class SenseHat():
        # Get Temperature
        def get_temperature(self):
            print "Get Temperature"
            return 1

       # Get Pressure
        def get_pressure(self):
            print "Get Pressure"
            return 2

        # Get Humidity
        def get_humidity(self):
            print "Get Humidity"
            return 3

        # Display message
        def show_message(self, messageString):
            print messageString


############################################################
# Function:    sendToReceiver
# Description: Post the sensor readings to the generic receiver.
# Parameters:  sensorData - the sensor readings passed in by 
#                           means of the Sensor class.
def sendToReceiver(sensorData):
    print ">> sendToReceiver"
    print "Temperature: " + str(sensorData.temperature)
    print "Humidity:    " + str(sensorData.humidity)
    print "Pressure:    " + str(sensorData.pressure)

    receiverUrl = "http://rdev.gpsbe.net"
    port = "5013"
    fullUrl = receiverUrl + ":" + port
    
    #fullUrl = "http://dev-messaging-service.appspot.com"

    data = json.dumps({'Temperature' : sensorData.temperature, 'Humidity': sensorData.humidity, 'Pressure': sensorData.pressure})
    print data

    print "Full URL = " + fullUrl

    u = urllib2.urlopen(fullUrl, data)
    #response = u.getcode()
    #print response
    
    u.close()
    print "Done!"



sense = SenseHat()

sensor = Sensor()

sense.show_message("Sensor")

#while True:
#    t = sense.get_temperature()
#    p = sense.get_pressure()
#    h = sense.get_humidity()

#    msg = "Temperature = {0}, Pressure = {1}, Humidity = {2}".format(t,p,h)

#    sense.show_message(msg) #, scroll_speed=0.05)


############################################################
# Main routine
# 
def main():
    print "Pi Sensor"

    sensor.temperature = sense.get_temperature()
    sensor.pressure = sense.get_pressure()
    sensor.humidity = sense.get_humidity()

    sendToReceiver(sensor)

    msg = "Temperature = {0}, Pressure = {1}, Humidity = {2}".format(sensor.temperature, sensor.pressure, sensor.humidity)
    
    sense.show_message(msg) #, scroll_speed=0.05)

    #s = socket.socket()




if __name__ == '__main__':
    main()

    