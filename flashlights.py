import urllib2
import time
import willie
from willie.module import commands, interval

@willie.module.commands('alertspace')
@willie.module.example('.alertspace','alertspace')
def spacestate(bot, trigger):
  """Alerts the space by flashing the lights a few times"""
  opener = urllib2.build_opener(urllib2.HTTPHandler)
  request = urllib2.Request('http://10.0.20.32/api/0123456789abdcef0123456789abcdef/groups/0/action', data='{    "alert": "lselect" }')
  request.add_header('Content-Type', 'text/json')
  request.get_method = lambda: 'PUT'
  url = opener.open(request)
  bot.say('The space has been alerted!')

