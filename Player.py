#!/usr/bin/python

from mpd import MPDClient, MPDError, ConnectionError

class Player:
    
    def __init__(self, host="localhost", port=6600):
        self._host = host
        self._port = port
        self._client = MPDClient()
        
    def _connect(self):
        self._client.connect(self._host, self._port)
    
    def _disconnect(self):
        try:
            self._client.disconnect()           
        except:
            pass

    def _ensure__connection(self):
        try:
            self._client.ping()
        except (MPDError, ConnectionError, IOError):
            self._disconnect()
            self._connect()
        
    def play(self, stream):
        self._ensure__connection()
            
        songId = self._client.addid(stream, 0)
        self._client.playid(songId)
        
    def stop(self):
        self._ensure__connection()
        
        self._client.stop()
        
    def status(self):
        self._ensure__connection()
        
        return self._client.status()
        
    def currentsong(self):
        self._ensure__connection()
        
        return self._client.currentsong()
        
    def is_playing(self):
        status = self.status()
        
        return status['state'] == 'play'
