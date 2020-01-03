from hcsr04sensor import sensor
import time
import RPi.GPIO as gpio
import sys
gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)
# 車車
gpio.setup(7, gpio.OUT)
gpio.setup(11, gpio.OUT)
# 超音波
TRIGGER_PIN = 25
ECHO_PIN = 8
# 土壤感測器

gpio.setup(13, gpio.IN)


try:
    while True:
        sr04 = sensor.Measurement(TRIGGER_PIN, ECHO_PIN)
        raw_measurement = sr04.raw_distance()
        distance = sr04.distance_metric(raw_measurement)

        # 如果偵測到物品在正中間了
        if distance > 3:
            gpio.output(7, True)
            gpio.output(11, True)
        else:
            gpio.output(7, False)
            gpio.output(11, False)
            # 插土壤感測器
            if gpio.input(13) == False:
                # 不澆水
                print :"不澆水"
            elif gpio.input(13) == True:
                # 澆水
                print :"澆水"


except KeyboardInterrupt:
    print('關閉程式 ')
