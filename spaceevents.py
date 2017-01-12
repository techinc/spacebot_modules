import urllib2
import time
import willie
import bs4
import re

def getevents(bot, number):
  response = urllib2.urlopen('http://wiki.techinc.nl/index.php/Events')
  html = response.read()
  soup = bs4.BeautifulSoup(html)
  rulediv = soup.findAll('table', {"class" : "wikitable"})
  soup2 = bs4.BeautifulSoup(str(rulediv))
  eventdiv = soup2.findAll('tr')
  eventfinallevel = []
  x = 1
  while x < (number+1):
    theevent = str(eventdiv[x])
    eventdetails = []
    soup3 = bs4.BeautifulSoup(theevent)
    theeventdiv = soup3.findAll('td')
    for y in theeventdiv:
      y = re.sub("<.*?>", "", str(y))
      y = re.sub("\n", "", y)
      eventdetails.append(y)
    eventfinallevel.append(eventdetails)
    x = x + 1
  botmessage = ""
  for stuff in eventfinallevel:
    print(str(stuff))
    try:
      bot.say(stuff[0] + " - " + stuff[1])
    except IndexError:
      break

@willie.module.commands('nextevents')
@willie.module.example('.nextevents','nextevents')
def eve(bot, trigger):
  """Returns a list of the next events at the space"""
  eventnum = trigger.group(2)
  getevents(bot, 3)

@willie.module.commands('nextevent')
@willie.module.example('.nextevent','nextevent')
def nexteve(bot, trigger):
  """Returns the next event at the space"""
  getevents(bot, 1)

