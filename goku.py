import json
import wiringpi as pi
import time
import os
from pygame import mixer as mi
import random

def goku():
    print("goku")
    return

def init():
    pi.wiringPiSetupGpio()

def led(cmd):
    LED_PIN = 4
    flash_time = 100
    pi.pinMode(LED_PIN, pi.OUTPUT)
    for i in range(flash_time):
        pi.digitalWrite(LED_PIN, pi.HIGH)
        time.sleep(0.05)
        pi.digitalWrite(LED_PIN, pi.LOW)

def voice(cmd):
    mp3_path = '/home/pi/sound'
    files = os.listdir('/home/pi/sound')
    mi.init()
    if cmd == 'effect':
        mi.music.load(mp3_path+'/koukaon_kamehameha.mp3')
    else:
        mi.music.load(mp3_path+'/'+random.choice(files))
    mi.music.play()

def vote(cmd):
    json_file = '/home/pi/interop2017/result.json'
    with open(json_file) as data_file:
        data = json.load(data_file)
    if cmd == 'goku':
        data['goku'] = data['goku'] +1
    else:
        data['freeza'] = data['freeza'] +1
    print(data)
    with open(json_file,'w') as outfile:
        json.dump(data,outfile)

if __name__=="__main__":
    goku()
    
