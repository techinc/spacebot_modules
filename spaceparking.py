import urllib2
import time
import willie

@willie.module.commands('parking')
def parking(bot, trigger):
  f = open('parkingcodefile', 'r')
  parkingcode = f.read()
  if (parkingcode == ""):
    bot.say("No parking code is currently set")
  else:
    bot.say('Parking code is currently ' + parkingcode)

@willie.module.commands('setparking')
def setparking(bot, trigger):
  parkingcode = trigger.group(2)
  f = open('parkingcodefile', 'w')
  if parkingcode is None:
    parkingcode = ""
    bot.say("Parking code has been cleared")
  else:
    bot.say("Parking code has been set to " + parkingcode)
   f.write(parkingcode)

