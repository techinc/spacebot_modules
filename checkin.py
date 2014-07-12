import urllib2
import time
import willie
from willie.module import commands, interval

INTERVAL = 5
SPACESTATE="unknown"
CHANNEL = "#techinc-testing"
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
        bot.msg(CHANNEL,'Space closed, emptying check-in list')
        WHO = []

@willie.module.commands('checkin')
def checkin(bot, trigger):
  global WHO
  if trigger.host == 'bugblue.sponsor.oftc.net':
    bot.say(trigger.nick + ' could not be checked in')
    return
  if trigger.nick in WHO:
    bot.say(trigger.nick + ' is already checked in')
  else:
    WHO.append(trigger.nick)
    bot.say(trigger.nick + ' is now checked in')

@willie.module.commands('checkout')
def checkout(bot, trigger):
  global WHO
  if trigger.nick in WHO:
    WHO.remove(trigger.nick)
    bot.say(trigger.nick + ' is now checked out')
  else:
    bot.say(trigger.nick + ' was not checked in')

@willie.module.commands('emptylist')
def emptylist(bot, trigger):
  global WHO
  WHO = []
  bot.say('Check-in list has been emptied')

@willie.module.commands('who')
def checkwho(bot, trigger):
  global WHO
  peoplelist = ''
  if not WHO:
    bot.say('Nobody currently checked in at the space')
  else:
    for people in WHO:
      peoplelist += people + ','
    bot.say(peoplelist)

@willie.module.commands('anoncheckin')
def anoncheckin(bot, trigger):
  global WHO
  WHO.append('anonymous')
  bot.say('anonymous is now checked in')

@willie.module.commands('anoncheckout')
def anoncheckout(bot, trigger):
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

