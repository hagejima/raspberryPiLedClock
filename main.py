import RPi.GPIO as GPIO
import time
import datetime

gpios = [21, 20, 26, 16, 19, 13, 12, 6, 5, 25, 18, 24, 23, 22, 27, 17, 4]

GPIO.setmode(GPIO.BCM)
for i in gpios:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, False)

hour = 0
minute = 0
seconds = 0

while(1):
    #時間取得
    nowTime = datetime.datetime.now()
    hour = nowTime.hour
    print(hour)
    minute = nowTime.minute
    print(minute)
    seconds = nowTime.second
    print(seconds)

    #2進数への変換
    decimal = ""
    decimal += format(hour, '05b')
    decimal += format(minute, '06b')
    decimal += format(seconds, '06b')

    #LEDの更新
    count = 0
    for i in decimal:
        if i=='1':
            GPIO.output(gpios[count], True)
        else:
            GPIO.output(gpios[count], False)
        count+=1

    #1秒ごとに更新
    time.sleep(1)
