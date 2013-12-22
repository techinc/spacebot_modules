import urllib2
import time
import willie
from willie.module import commands, interval

INTERVAL = 5
SPACESTATE = "unknown"
CHANNEL = "#techinc"
SPACEURL = "http://techinc.nl/space/spacestate"

def checkstate():
  global SPACESTATE
  global SPACEURL
  response = urllib2.urlopen(SPACEURL)
  html = response.read()
  return html

def changestate(state):
  global SPACESTATE
  print 'State: %s' % state
  response = urllib2.urlopen('http://techinc.nl/space/index.php?state=%s&key=PASSWORDGOESHERE' % state)
  html = response.read()
  SPACESTATE = html
  return html


@interval(INTERVAL)
def trackstate(bot):
  global SPACESTATE
  global CHANNEL
  state = checkstate()
  if SPACESTATE != state:
        bot.msg('#techinc-testing','The space is now ' + state)
        newtopic = 'Welcome to Technologia Incognita, we are ' + state + '. https://www.techinc.nl/ - Social night every Wednesday at ACTA'
        bot.write(('TOPIC', CHANNEL + ' :' + newtopic))
        SPACESTATE = state

@willie.module.commands('togglestate')
def togglestate(bot, trigger):
  currentstate = checkstate()
  bot.say('Changing Spacestate')
  if currentstate == 'open':
    state = 'closed'
  else:
    state = 'open'
  changestate(state)

@willie.module.commands('spacestate')
def spacestate(bot, trigger):
  global SPACEURL
  response = urllib2.urlopen(SPACEURL)
  html = response.read()
  bot.say('The space is currently ' + html)

