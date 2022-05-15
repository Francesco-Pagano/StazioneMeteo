import time
import board
import adafruit_tcs34725

i2c = board.I2C()
sensor = adafruit_tcs34725.TCS34725(i2c)

def getDataRGB():

    r, g, b = sensor.color_rgb_bytes
    temp = sensor.color_temperature
    lux = sensor.lux

    sensor_data = {'Red': r,
                   'Green': g,
                   'Blue': b,
                   'ColorTemperature': temp,
                   'Lux': lux
                  }

    return sensor_data
