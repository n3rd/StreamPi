#!/usr/local/bin/python

import requests

class PlayList:
    
    token = '0a72fd75ad2d3c2a66c379e327'
    
    __stations = [ ]
    
    def __init__(self):
        self.__process_stations(self.__get_stations())
    
    def __get_stations(self):
        url = 'http://api.dirble.com/v2/countries/nl/stations?all=1&token={}'.format(self.token)
        r = requests.get(url)
        return r.json()

    def __process_stations(self, stations):
        for station in stations:
            self.__add_station(station)
            
    def __add_station(self, station):
        if len(station['streams']) > 0:
            self.__stations.append({
                'name': station['name'].encode('utf8'),
                'stream_url': station['streams'][0]['stream'].encode('utf8')
            })
            
    def get_stations(self):
        return self.__stations

    def do_print(self):
        for station in self.get_stations():
            print '{} - {}'.format(station['name'], station['stream_url'])
    
        
if __name__ == '__main__':
    try:
        pl = PlayList()
        pl.do_print()
    except KeyboardInterrupt:
        print >> sys.stderr, '\nExiting by user request.\n'
        sys.exit(0)