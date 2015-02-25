import urllib2
import time
import willie

foodorder = {}
source = ""
orderstate = 0
owner = ""


@willie.module.commands('orderstart')
def startorder(bot, trigger):
  setsource(bot, trigger.group(2),trigger.nick)

def setsource(bot, restaurant, nick):
  global source
  global orderstate
  global owner
  if orderstate == 0:
    source = restaurant
    orderstate = 1
    owner = nick
    bot.say("Order with " + str(source) + " created")
  elif orderstate == 1:
    bot.say("Order already underway, please add your selections")
  else: 
    bot.say("Order closed and being delivered")

@willie.module.commands('order')
def getsource(bot, trigger):
  global source
  if source != "":
    bot.say("Order underway from: " + source)
  else:
    bot.say("No order currently active")

@willie.module.commands('orderadd')
def addtoorder(bot, trigger):
  global foodorder
  global orderstate
  user = trigger.nick
  stuff = trigger.group(2)
  if orderstate == 1:
    foodorder[user] = stuff
    bot.say("Added " + user + "'s order")
  else:
    bot.say("Order already completed or no order underway")

@willie.module.commands('orderdel')
def delfromorder(bot, trigger):
  global foodorder
  global orderstate
  user = trigger.nick
  if orderstate == 1:
    del foodorder[user]
    botsay("Order cleared for " + user)
  else:
    bot.say("Order already completed or no order underway")

@willie.module.commands('myorder')
def myorder(bot, trigger):
  global foodorder
  if trigger.nick in foodorder.keys():
    bot.say(trigger.nick + " - " + foodorder[trigger.nick])
  else:
    bot.say(trigger.nick + " has no order")

@willie.module.commands('orderfull')
def getwholeorder(bot, trigger):
  global foodorder
  global source
  global owner
  if owner == trigger.nick:
    bot.say(source)
    for k,v in foodorder.items():
       bot.say(k + " - " + v)
  else:
    print("Sorry this is not your order, please ask " + owner)

@willie.module.commands('orderclear')
def clearorder(bot, trigger):
  global owner
  if owner == trigger.nick:
    global foodorder
    foodorder = {}
    global source
    source = ""
    global orderstate
    nick = ""
    orderstate = 0
    bot.say("Order has been cleared")
  else:
    bot.say("This is not your order, please ask " + owner)

@willie.module.commands('orderfinal')
def finalorder(bot, trigger):
  global orderstate
  orderstate = 2
  bot.say("Order locked for delivery")
  



