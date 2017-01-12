import os
import willie
from willie.module import commands, interval

@willie.module.commands('sha')
@willie.module.example('.sha', 'sha')
def spacestate(bot, trigger):
  """Gives you a random SHA2017 slogan suggestion"""
  txt = "echo \"$(grep \"^s\" /usr/share/dict/cracklib-small | shuf -n1) $(grep \"^hack\" /usr/share/dict/cracklib-small | shuf -n1) $(grep \"^a\" /usr/share/dict/cracklib-small | shuf -n1) 2017\""  
  bot.say(os.popen(txt).read().title())

