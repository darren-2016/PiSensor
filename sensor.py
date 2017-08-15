######################################################################
# PiSensor
#
# Get the temperate, humidity and pressure readings
# Send the readings to the generic receiver rdev.gpsbe.net port 5013 - 
# The generic receiver used for testing new receivers.
#  http requests port 5013
#
#
# Use HTTP Requests to send formatted data to port 5013 at rdev.gpsbe.net
#

#
#import socket
import json
import urllib2

# Define raspPi as True if running on a Raspberry Pi, otherwise False.
raspPi = False

if raspPi == True:
    from sense_hat import SenseHat

else:
    class SenseHat():
        # Get Temperature
        def get_temperature(self):
            
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
# sendToReceiver
# Send the sensor readings to the generic receiver.
# 
def sendToReceiver():
    print "SendToReceiver"


sense = SenseHat()

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

    t = sense.get_temperature()
    p = sense.get_pressure()
    h = sense.get_humidity()
    msg = "Temperature = {0}, Pressure = {1}, Humidity = {2}".format(t,p,h)
    sense.show_message(msg) #, scroll_speed=0.05)


    #url = "http://rdev.gpsbe.net:5013"
    #port = "5013"
    #fullUrl = url + ":" + port
    
    url = "http://dev-messaging-service.appspot.com"

    data = json.dumps({'Temperature' : t, 'Humidity': h, 'Pressure': p})
    print data


    u = urllib2.urlopen(url, data)
    response = u.read()
    
    
    print response
    
    u.close()

    #s = socket.socket()










if __name__ == '__main__':
    main()

    