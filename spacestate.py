"""
spacestate.py - A spacestate check module for techincs williebot shardik
Copyright 2013, realitygaps
Licensed under the GPLv3.

http://willie.dfbta.net
"""

import willie
import urllib2

@willie.module.commands('spacestate')
@willie.module.example('.spacestate', 'Spacestate')
def spacestate(bot, trigger):
  """Replies with the current space state - Open/Closed"""
  response = urllib2.urlopen('http://techinc.nl/space/spacestate')
  html = response.read()
  bot.say('The space is currently ' + html)

@willie.module.commands('state')
def state(bot, trigger):
  spacestate(bot, trigger)

