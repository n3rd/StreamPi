#!/usr/local/bin/python

# depends on: http://pyalsaaudio.sourceforge.net
# sudo apt-get install python-alsaaudio

import time
import alsaaudio

class Volume:

    def __init__(self):
        self.mixer = alsaaudio.Mixer(control='PCM')
    
    def get_volume(self):
        return self.mixer.getvolume('playback')[0]

    def set_volume(self, percentage):
        if percentage < 0:
            percentage = 0
        elif percentage > 100:
            percentage = 100
        
        self.mixer.setvolume(percentage)
        time.sleep(.2)
    
    def volume_up(self):
        self.set_volume(self.get_volume() + 5)
        
    def volume_down(self):
        self.set_volume(self.get_volume() - 5)
        
    
