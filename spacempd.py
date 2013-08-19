import urllib2
import time
import willie
import sys
from mpd import (MPDClient, CommandError)
from socket import error as SocketError

HOST = '10.0.20.3'
PORT = '6600'
PASSWORD = 'password goes here'

@willie.module.commands('mpd')
def mpd(bot, trigger):
  rulenum = trigger.group(2)

  ## MPD object instance
  client = MPDClient()

  try:
    client.connect(host=HOST, port=PORT)
  except SocketError:
    bot.say('socketerror')
    exit(1)


  # Auth if password is set non False
  if PASSWORD:
    try:
      client.password(PASSWORD)
    except CommandError:
      client.disconnect()
      sys.exit(2)

  mpdcommand = str(rulenum)

  if ((mpdcommand == 'playing') or (mpdcommand == 'state')) :
    currentsong = client.currentsong()
    currentstatus = client.status()

    if currentstatus['state'] == 'play':
      bot.say('Now playing: ' + currentsong['artist'] + ' - ' + currentsong['title'])
    elif currentstatus['state'] == 'pause':
      bot.say('Music is currently paused (' + currentsong['artist'] + ')')
    elif currentstatus['state'] == 'stop':
      bot.say('No music is playing')

  elif mpdcommand == 'play':
    bot.say('Pressing play on mpd...')
    client.play()
    currentsong = client.currentsong()
    bot.say('Now playing: ' + currentsong['artist'] + ' - ' + currentsong['title'])

  elif mpdcommand == 'pause':
    bot.say('Pausing mpd...')
    client.pause()

  elif mpdcommand == 'stop':
    bot.say('Stopping mpd...')
    client.stop()

  elif mpdcommand == 'next':
    bot.say('Moving to next song on mpd...')
    client.next()
    currentsong = client.currentsong()
    bot.say('Now playing: ' + currentsong['artist'] + ' - ' + currentsong['title'])

  else:
    bot.say('invalid mpd command')

