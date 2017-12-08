import urllib2
import json
# import time
import willie

# from willie.module import commands, interval

@willie.module.commands('alertspace')
@willie.module.example('.alertspace open door', 'alertspace')
def spacestate(bot, trigger):
    """Alerts the space by flashing the lights a few times"""
    _alert_lamps()
    _alert_ledslie(trigger.nick, trigger.groups()[1:])
    bot.say('The space has been alerted!')


def _alert_lamps():
    opener = urllib2.build_opener(urllib2.HTTPHandler)
    request = urllib2.Request('http://10.0.20.32/api/0123456789abdcef0123456789abcdef/groups/0/action',
                              data='{ "alert": "lselect" }')
    request.add_header('Content-Type', 'text/json')
    request.get_method = lambda: 'PUT'
    opener.open(request)


def _alert_ledslie(nick, message):
    opener = urllib2.build_opener(urllib2.HTTPHandler)
    data = {"who": nick, "text": message}
    request = urllib2.Request('http://ledslie.ti/alert', data=json.dumps(data))
    request.add_header('Content-Type', 'text/json')
    request.get_method = lambda: 'POST'
    opener.open(request)
