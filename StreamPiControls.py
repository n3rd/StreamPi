#!/usr/local/bin/python

# KY040 Rotary Encoder
# ===
# + (5V) e.g. GPIO.BOARD 2
# BTN is on GPIO.BOARD 12
# GND e.g. GPIO.BOARD 14
# B (DT) is on GPIO.BOARD 16
# A (CLK) is on GPIO.BOARD 18

# Switch
# ===
# GPIO.BOARD 20 (GND)
# GPIO.BOARD 22 

import sys
import time
from RotaryEncoder import RotaryEncoder
from Volume import Volume
from Player import Player
from System import System
import RPi.GPIO as GPIO

# (!) use BOARD NRs for PINs
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

class StreamPiControls:

    def __init__(self, btn_pwr, re_a, re_b, re_btn):
        self._volume = Volume()
        self._player = Player()
        self._rotary_encoder =  RotaryEncoder(re_a, re_b, re_btn, self.re_callback, self.re_btn_callback)
        self._system = System()
        
        GPIO.setup(btn_pwr, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(btn_pwr, GPIO.FALLING, callback=self.pwr_callback, bouncetime=200)
        
    def re_callback(self, direction, btn_pressed):
        if direction == RotaryEncoder.DIRECTION_CLOCKWISE:
            self._volume.volume_up()
        elif direction == RotaryEncoder.DIRECTION_COUNTERCLOCKWISE:
            self._volume.volume_down()
            
    def re_btn_callback(self):
        if(self._player.is_playing()):
            self._player.stop()
        else:
            self._player.play("http://icecast.omroep.nl/3fm-bb-mp3")
            
    def pwr_callback(self, channel):
        self._system.shutdown()

def main_loop():
    while True:
        time.sleep(0.5)
        
if __name__ == '__main__':
    try:
        controls = StreamPiControls(22, 18, 16, 12)
        
        main_loop()
    except KeyboardInterrupt:
        print >> sys.stderr, '\nExiting by user request.\n'
        sys.exit(0)
