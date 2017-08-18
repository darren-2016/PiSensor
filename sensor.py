######################################################################
# PiSensor
#
# Climate monitoring application.  
# Monitoring temperature, humidity and pressure.
# Send the readings to the generic receiver rdev.gpsbe.net port 5013 
# The generic receiver used for testing new receivers.
# http requests port 5013
#
# Use HTTP Requests to send formatted data to port 5013 at rdev.gpsbe.net
#
# TODO: Implement a task sheduling system, such as cron


#import socket
import json
import urllib2
import requests

# Define raspPi as True if running on a Raspberry Pi, otherwise False.
raspPi = True

# Define webaccess as True if access web services, otherwise False.
webaccess = True

if raspPi == True:
    from sense_hat import SenseHat

else:
    # Emulate SenseHat
    class SenseHat():
        # Get Temperature
        def get_temperature(self):
            print "**** Emulate Get Temperature "
            return 1

       # Get Pressure
        def get_pressure(self):
            print "**** Emulate Get Pressure"
            return 2

        # Get Humidity
        def get_humidity(self):
            print "**** Emulate Get Humidity"
            return 3

        # Display message
        def show_message(self, messageString):
            print "**** Emulate LED Matrix Display: " + messageString


############################################################
# Class:       Sensor
# Description: Object for storing the temperature, pressure 
#              and humidity readings.
class Sensor:
    temperature = 0;
    pressure = 0;
    humidity = 0;


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

    if webaccess == True:
        receiverUrl = "http://rdev.gpsbe.net"
        port = "5013"
        fullUrl = receiverUrl + ":" + port
        
        data = json.dumps({'Temperature' : sensorData.temperature, 'Humidity': sensorData.humidity, 'Pressure': sensorData.pressure})
        print data

        print "Full URL = " + fullUrl

        # Send to receiver using requests functionality
        try:
            r = requests.post(fullUrl, data, timeout=5)
        except requests.Timeout:
            print "Timeout!"
    
        #print r.status_code
    
        #u = urllib2.urlopen(fullUrl, data)
        #response = u.getcode()
        #print response
    
        #u.close()
    print "Done!"


# Global initialisations
sense = SenseHat()
sensor = Sensor()

############################################################
# Function:    monitorClimate
# Description:
def monitorClimate():
    sensor.temperature = sense.get_temperature()
    sensor.pressure = sense.get_pressure()
    sensor.humidity = sense.get_humidity()

    sendToReceiver(sensor)

    msg = "Temperature = {0}, Pressure = {1}, Humidity = {2}".format(sensor.temperature, sensor.pressure, sensor.humidity)
    
    #sense.show_message(msg) #, scroll_speed=0.05)

             
############################################################
# Main routine
# 
def main():
    print "Pi Sensor"

    sense.show_message("Climate Sensor")

    monitorClimate()


    #s = socket.socket()



# Main entry point
if __name__ == '__main__':
    main()

    