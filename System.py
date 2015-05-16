#!/usr/bin/python

import os
import pygame

class System:

    _shutdown_initiated = False

    def shutdown(self):
        if(not self._shutdown_initiated):
            self._shutdown_initiated = True
            self.play_sound('sounds/nooooo.mp3')
            os.system("shutdown -h now")
        
    def reboot(self):
        if(not self._shutdown_initiated):
            self._shutdown_initiated = True
            self.play_sound('sounds/err.mp3')
            os.system("shutdown -r now")
            
    def play_sound(self, sound_file):
        path = os.path.dirname(os.path.abspath(__file__))
        
        pygame.init()
        pygame.mixer.music.load(os.path.join(path, sound_file))
        pygame.mixer.music.play()
        