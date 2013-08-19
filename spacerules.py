import urllib2
import time
import willie
from bs4 import BeautifulSoup
  

def getrules():
  response = urllib2.urlopen('http://wiki.techinc.nl/index.php/Rules')
  html = response.read()
  soup = BeautifulSoup(html)  
  
  rulediv = soup.findAll('div', {"class" : "mw-content-ltr"})

  myrulediv = str(rulediv)
  myrulediv = myrulediv.replace("[<div","<div")
  myrulediv = myrulediv.replace("</div>]","</div>")
  ruleset = BeautifulSoup(myrulediv)

  therules = [];
  for li in ruleset.findAll('li'):
    ruletext = li.text.replace("</li>", "")
    ruletext = ruletext.replace("</ol>", "")
    therules.append(ruletext.rstrip())
  return therules

@willie.module.commands('rule')
def rule(bot, trigger):
  rulenum = trigger.group(2)
  therules = getrules()
  try:
    rule = therules[int(rulenum)]
    bot.say('Rule ' + rulenum + ': ' + rule)
  except IndexError:
    bot.say('sorry, no such rule')
