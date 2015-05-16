#!/usr/bin/python

import json
from flask import Flask, Response
from Player import Player
from Volume import Volume
from PlayList import PlayList
from System import System

_player = Player()
_volume = Volume()
_playList = PlayList()
_system = System()

app = Flask(__name__)

@app.route('/player/play', defaults = {
    'stream': 'http://icecast.omroep.nl/3fm-bb-mp3' 
    })
@app.route('/player/play/<path:stream>')
def play(stream, player=_player):
    print 'play stream {}'.format(stream)
    player.play(stream)
    print player.currentsong()
    return Response(json.dumps({
        'status'  : player.status(),
        'currentSong': player.currentsong()
    }), status=200, mimetype='application/json')

@app.route('/player/stop')
def stop(player=_player):
    player.stop()
    return Response(json.dumps({
        'status'  : player.status()
    }), status=200, mimetype='application/json')
    
@app.route('/player/currentSong')
def currentSong(player=_player):
    return Response(json.dumps({
        'status': player.status(),
        'currentSong': player.currentsong()
    }), status=200, mimetype='application/json')
    
@app.route('/player/volume/<direction>')
def volume(direction, volume=_volume):
    if(direction == 'up'):
        volume.volume_up()
    else:
        volume.volume_down()
        
    return Response(json.dumps({
        'volume': volume.get_volume()
    }), status=200, mimetype='application/json')
    
@app.route('/stations')
def stations(pl=_playList):
    return Response(json.dumps({
        'stations': pl.get_stations()
    }), status=200, mimetype='application/json')

@app.route('/system/reboot')
def reboot(system=_system):
    system.reboot()
    return Response('', status=204)

@app.route('/system/shutdown')
def shutdown(system=_system):
    system.shutdown()
    return Response('', status=204)

if __name__ == '__main__':
    app.run('0.0.0.0', 8080, debug=True)