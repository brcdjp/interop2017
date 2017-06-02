#!/usr/bin/env python

import wiringpi as pi
import requests
import time
import urllib3
from urllib3.exceptions import InsecureRequestWarning
urllib3.disable_warnings(InsecureRequestWarning)


st2host = 'bwc'
api_key =''

CATCH_DISTANCE = 5
TRIG_PIN = 23
ECHO_PIN = 24

pi.wiringPiSetupGpio()

pi.pinMode( TRIG_PIN, pi.OUTPUT )
pi.pinMode( ECHO_PIN, pi.INPUT )
pi.digitalWrite( TRIG_PIN, pi.LOW )
time.sleep( 1 )


def main():
    distance = measure()
    print ("Distance: ", distance)
    if distance < CATCH_DISTANCE:
        send()
        time.sleep(1)
    else:
        pass
    time.sleep(0.01)

def measure():
    pi.digitalWrite( TRIG_PIN, pi.HIGH )
    time.sleep(0.00001)
    pi.digitalWrite( TRIG_PIN, pi.LOW )
    while ( pi.digitalRead( ECHO_PIN ) == pi.LOW ):
        sigoff = time.time()
    while ( pi.digitalRead( ECHO_PIN ) == 1 ):
        sigon = time.time()
    return (( sigon - sigoff ) * 34000) / 2

def send():
    response = requests.post(
        'https://'+st2host+'/api/v1/webhooks/interop2017',
        headers={'St2-Api-Key':api_key, 'Content-Type':'application/json'},
        json={'vote':'goku'})

if __name__=='__main__':
    while True:
        main()
        
