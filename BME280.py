import time
import board
import adafruit_bmp280
from adafruit_bme280 import basic as adafruit_bme280

i2c = board.I2C()
bme280 = adafruit_bmp280.Adafruit_BMP280_I2C(i2c, address = 0x76)

def getDataBME280():

  sensor_dataBME280 = {'Temperature': bme280.temperature,
                       'Pressure': bme280.pressure,
                       'Altitude': bme280.altitude
                      }

  return sensor_dataBME280
