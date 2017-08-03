from sense_hat import SenseHat

sense = SenseHat()

sense.show_message("Sensor")

while True:
    t = sense.get_temperature()
    p = sense.get_pressure()
    h = sense.get_humidity()

    msg = "Temperature = {0}, Pressure = {1}, Humidity = {2}".format(t,p,h)

    sense.show_message(msg, scroll_speed=0.05)
