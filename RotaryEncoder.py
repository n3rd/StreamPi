#!/usr/local/bin/python

# explanation: 
# http://guy.carpenter.id.au/gaugette/2013/01/14/rotary-encoder-library-for-the-raspberry-pi/

import RPi.GPIO as GPIO

class RotaryEncoder:

    DIRECTION_CLOCKWISE = 1
    DIRECTION_COUNTERCLOCKWISE = 3
    
    prv_seq = 0
    direction = 0
    
    def __init__(self, pinA, pinB, button, callback, btn_callback):
        self.pinA = pinA
        self.pinB = pinB
        self.button = button
        self.callback = callback
        self.btn_callback = btn_callback
        
        GPIO.setup(self.pinA, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.pinB, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        
        GPIO.add_event_detect(self.pinA, GPIO.FALLING, callback=self.evt)
        GPIO.add_event_detect(self.pinB, GPIO.FALLING, callback=self.evt)
        GPIO.add_event_detect(self.button, GPIO.FALLING, callback=self.btn_evt, bouncetime=200)
        
    def evt(self, channel):        
        a = GPIO.input(self.pinA)
        b = GPIO.input(self.pinB)
        c = a ^ b
        seq = c | b << 1
        delta = (seq - self.prv_seq) % 4
        
        if delta == 1:
            if self.direction == self.DIRECTION_CLOCKWISE:
                self.callback(self.DIRECTION_CLOCKWISE, self._is_button_pressed())
            else:
                self.direction = self.DIRECTION_CLOCKWISE
        elif delta == 2:
            if self.direction == self.DIRECTION_CLOCKWISE:
                self.callback(self.DIRECTION_CLOCKWISE, self._is_button_pressed())
            elif self.direction == self.DIRECTION_COUNTERCLOCKWISE:
                self.callback(self.DIRECTION_COUNTERCLOCKWISE, self._is_button_pressed())
        elif delta == 3:
            if self.direction == self.DIRECTION_COUNTERCLOCKWISE:
                self.callback(self.DIRECTION_COUNTERCLOCKWISE, self._is_button_pressed())
            else:
                self.direction = self.DIRECTION_COUNTERCLOCKWISE
        
        self.prv_seq = seq
        
    def _is_button_pressed(self):
        return GPIO.input(self.button) == GPIO.LOW
        
    def btn_evt(self, channel):
        self.btn_callback();
