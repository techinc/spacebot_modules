import requests
import time
import willie

statetracking = False

class SpaceState():
    _session = requests.session()
    _space_tracking = 0
    _valid_states = ['open', 'closed']
    _state_url = "http://techinc.nl/space/spacestate"
    _update_url = None

    def __init__(self, update_key=None):
        if update_key:
            self._update_url = "http://techinc.nl/space/index.php?key={0}".format(update_key)

    def __get(self, url, payload=None):
        print(url)
        response = {}
        r = None
        try:
            if payload:
                r = self._session.get(url, data=payload)
            else:
                r = self._session.get(url)

        except requests.exceptions.ConnectionError, e:
            r = False
            response['result'] = False
            response['content'] = e
            print("Failed to retrieve space state: {0}".format(e))
        finally:
            if r and r.status_code == 200:
                response['result'] = True
                response['content'] = r.content
            else:
                response['result'] = False
                response['content'] = 'Request failed'

        return response

    def get(self):
        r = self.__get(self._state_url)
        if r["result"] == True:
            return r["content"]

    def set(self, state):
        if not self._update_url:
            print("Key not set, not updating space state")
        elif state not in self._valid_states:
            print("{0} is an invalid state".format(state))
        else:
            print("Setting state to {0}".format(state))
            r = self.__get(self._update_url + "&state={0}".format(state))
            if r["result"] == True and r["content"] != "invalid key":
                print("Set space state to {0}".format(state))
            else:
                print("Failed to update space state: {0}".format(r["content"]))

@willie.module.commands('trackstate')
def trackstate(bot, trigger):
    spacestate = SpaceState(update_key="secretpasswordhere")
    if not statetracking:
        cur_state = spacestate.get()
        bot.say("Now tracking spacestate")

        while True:
            new_state = spacestate.get()
            if new_state != cur_state:
                new_topic = "Welcome to Technologia Incognita, we are " + new_state + ". https://www.techinc.nl/ - Social night every Wednesday at ACTA"

                channel = trigger.sender.lower()
                bot.write(('TOPIC', channel + ' :' + new_topic))
                cur_state = new_state
                time.sleep(5)
    else:
        bot.say('Already tracking spacestate')

@willie.module.commands('togglestate')
def togglestate(bot, trigger):
    spacestate = SpaceState(update_key="secretpasswordhere")
    cur_state = spacestate.get()
    bot.say('Changing Spacestate')
    if cur_state == 'open':
        state = 'closed'
    else:
        state = 'open'
    bot.say('The space is now ' + state)
    newtopic = 'Welcome to Technologia Incognita, we are ' + state + '. https://www.techinc.nl/ - Social night every Wednesday at ACTA'
    channel = trigger.sender.lower()
    bot.write(('TOPIC', channel + ' :' + newtopic))
    spacestate.set(state)


if __name__ == '__main__':
    spacestate = SpaceState(update_key="secretpasswordhere")
    print("Current state: {0}".format(spacestate.get()))

    spacestate.set("open")
    print("Current state: {0}".format(spacestate.get()))

    spacestate.set("closed")
    print("Current state: {0}".format(spacestate.get()))

    spacestate.set("blaat")
    print("Current state: {0}".format(spacestate.get()))
