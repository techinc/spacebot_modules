import urllib2

import willie
from willie.module import commands, interval

from spacestatechange import SPACESTATE

INTERVAL = 5
SPACESTATE="unknown"
CHANNEL = "#techinc"
SPACEURL = "http://techinc.nl/space/spacestate"
WHO = []

def checkstate():
  global SPACESTATE
  global SPACEURL
  response = urllib2.urlopen(SPACEURL)
  html = response.read()
  return html

@interval(INTERVAL)
def trackstate(bot):
  global CHANNEL
  global WHO
  state = checkstate()
  if state == "closed":
        WHO = []

@willie.module.commands('checkin')
@willie.module.example('.checkin','checkin')
def checkin(bot, trigger):
  """Adds you in to the list of people currently in the space"""
  global WHO
  if SPACESTATE == "closed":
    "Space is closed. %s cannot check-in. D'oh!" % trigger.nick
    return
  if trigger.host == 'bugblue.sponsor.oftc.net':
    bot.say(trigger.nick + ' could not be checked in')
    return
  if trigger.nick in WHO:
    bot.say(trigger.nick + ' is already checked in')
  else:
    WHO.append(trigger.nick)
    bot.say(trigger.nick + ' is now checked in')

@willie.module.commands('checkout')
@willie.module.example('.checkout','checkout')
def checkout(bot, trigger):
  """Removes you from the list of people currently in the space"""
  global WHO
  if trigger.nick in WHO:
    WHO.remove(trigger.nick)
    bot.say(trigger.nick + ' is now checked out')
  else:
    bot.say(trigger.nick + ' was not checked in')

@willie.module.commands('emptylist')
@willie.module.example('.emptylist','emptylist')
def emptylist(bot, trigger):
  """Emptys the list of people currently checked in at the space"""
  global WHO
  WHO = []
  bot.say('Check-in list has been emptied')

@willie.module.commands('who')
@willie.module.example('.who','who')
def checkwho(bot, trigger):
  """Returns the list of people currently checked in at the space"""
  global WHO
  peoplelist = ''
  if not WHO:
    bot.say('Nobody currently checked in at the space')
  else:
    peoplelist = ", ".join(WHO)
    bot.say(peoplelist)

@willie.module.commands('anoncheckin')
@willie.module.example('.anoncheckin','anoncheckin')
def anoncheckin(bot, trigger):
  """Adds an anonymous user to the list of people currently checked in at the space"""
  global WHO
  WHO.append('anonymous')
  bot.say('anonymous is now checked in')

@willie.module.commands('anoncheckout')
@willie.module.commands('.anoncheckout','anoncheckout')
def anoncheckout(bot, trigger):
  """Removes an anonymous user from the list of people currently checked in at the space"""
  global WHO
  if 'anonymous' in WHO:
    WHO.remove('anonymous')
    bot.say('anonymous is now checked out')
  else:
    bot.say('no anonymous users currently checked in')

@willie.module.commands('guestcheckin')
def guestcheckin(bot, trigger):
  global WHO
  WHO.append('guest')
  bot.say('guest is now checked in')

@willie.module.commands('guestcheckout')
def guestcheckout(bot, trigger):
  global WHO
  if 'guest' in WHO:
    WHO.remove('guest')
    bot.say('guest is now checked out')
  else:
    bot.say('no guests currently checked in')

