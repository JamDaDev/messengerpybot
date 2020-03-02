from cgi import log
import threading
import requests
import random
from fbchat import Client, log
from fbchat.models import *

client = Client("email", "pass")
if not client.isLoggedIn():
    client = Client("email", "pass")

alreadyDone = False



def reset():
    global alreadyDone
    alreadyDone = False


def set_interval(func, sec):
    def func_wrapper():
        set_interval(func, sec)
        func()

    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t


def isTrue():

    global alreadyDone
    if check() == "1" and alreadyDone is False:
        client.send(Message(text='UPDATE: Wind speed is between 30-60kph. \n '
                                 'Intermittent rains may be expected in at least 36 hours. '
                                 '(When the tropical cyclone develops very close to an area, '
                                 'a shorter lead time of the occurrence of the winds will be '
                                 'specified in the warning bulletin.) There is a possibility that '
                                 'the Storm warning signal will be raised if the storm moves closer to '
                                 'land                                                  '
                                 '*WAIT FOR SUSPENSION FOR CLASSES, THIS IS NOT A OFFICIAL WARNING SIGNAL.* \n'
                                 '-Powered by DarkSky Weather API.'),
                    thread_id="2695213210490883",
                    thread_type=ThreadType.GROUP)

        alreadyDone = True
    elif check() == "2" and alreadyDone is False:
        client.send(Message(text='UPDATE: Wind speed is now between 61 - 120kph. \n '
                                 'Light to moderate damage. '
                                 'Winds of greater than 60 kph and up to 100 kph may be expected in at least 24 hours. '
                                 'Special attention should be given to the latest position, direction and movement '
                                 'speed, '
                                 'and intensity of the storm as it moves toward an area.'
                                 'The public especially people traveling by sea and air are cautioned.'
                                 'Outdoor activities of children should be postponed.'
                                 'Secure properties before the signal is upgraded.'
                                 'Disaster preparedness agencies/organizations are in action to alert'
                                 ' their communities.'
                                 '*WAIT FOR SUSPENSION FOR CLASSES, THIS IS NOT A OFFICIAL WARNING SIGNAL.* \n'
                                 '-Powered by DarkSky Weather API.'),
                    thread_id="2695213210490883",
                    thread_type=ThreadType.GROUP)

        alreadyDone = True
    elif check() == "3" and alreadyDone is False:
        client.send(Message(text='UPDATE: Winds of greater than 100 kph up to 185 kph'
                                 ' may be expected in at least 18 hours. \n '
                                 'Travel is very risky especially by air and sea.'
                                 'People are advised to seek shelter in strong '
                                 'buildings, '
                                 'evacuate low-lying areas, and stay away from the coasts and riverbanks.'
                                 'Watch out for the passage of the eye of the typhoon indicated by a sudden occurrence'
                                 ' of fair weather immediately after very bad weather, '
                                 'with very strong winds coming generally from the north.'
                                 'When the eye of the typhoon hit the community, '
                                 'do not venture away from the safe shelter because after one'
                                 ' to two hours, the worst weather will resume,'
                                 ' with the very strong winds coming from the south.'
                                 'Classes in all levels should be suspended and '
                                 'children should stay in the safety of strong buildings.'
                                 'Disaster preparedness and response agencies/organizations are in action with '
                                 'appropriate response to emergency. '
                                 '*WAIT FOR SUSPENSION FOR CLASSES, THIS IS NOT A OFFICIAL WARNING SIGNAL.* \n'
                                 '-Powered by DarkSky Weather API.'),
                    thread_id="2695213210490883",
                    thread_type=ThreadType.GROUP)

        alreadyDone = True
    elif check() == 4 and alreadyDone is False:
        client.send(
            Message(text='UPDATE: Very strong winds of more than 185 kph may be expected in at least 12 hours. \n '
                         'The situation is potentially very destructive to the community. '
                         'The area is very likely to be hit directly by the eye of the typhoon. '
                         'As the eye of the typhoon approaches, the weather will worsen continuously, with winds'
                         ' increasing to its strongest coming generally from the north. '
                         'A sudden improvement of the weather with light winds will be experienced, which means the area is under the eye of the typhoon. '
                         'Depending on the eye’s diameter and movement speed, this improved weather may last for an hour or two. '
                         'As the eye moves out of the area, weather conditions will worsen, with strong winds generally coming from the south.'
                         '*DONT GO TO SCHOOL TODAY* \n'
                         '-Powered by DarkSky Weather API.'),
            thread_id="2695213210490883",
            thread_type=ThreadType.GROUP)

        alreadyDone = True
    elif check() == 5 and alreadyDone is False:
        client.send(Message(text='UPDATE: Wind speed can reach over 220kph. \n '
                                 'Stay safe, i dont know what ill say to you, but please stay safe, dont go outside.'
                                 '*DONT GO TO SCHOOL TODAY.* \n'
                                 '-Powered by DarkSky Weather API.'),
                    thread_id="2695213210490883",
                    thread_type=ThreadType.GROUP)

        alreadyDone = True
    elif check() == "no" and alreadyDone is True:

        alreadyDone = False


def check():
    i = requests.get("https://api.darksky.net/forecast/b2f13b2632333395c57e9dbb5f082cda/14.8528, 120.8154")
    data = i.json()

    for key, value in dict.items(data):
        if key != "currently":
            pass
        else:
            a = value
            val = int(a['windSpeed'])
            if 30 <= val <= 60:
                return "1"
            elif 61 <= val <= 120:
                return "2"
            elif 121 <= val <= 170:
                return "3"
            elif 171 <= val <= 220:
                return "4"
            elif val > 220:
                return "4"
            else:
                return "no"

    isTrue()
    reset()


class punkjj(Client):
    def onMessage(self, author_id=None, message_object=None, thread_id=None, thread_type=ThreadType.USER, **kwargs):
        toggle = client.fetchThreadMessages(thread_id=client.uid, limit=1)  # client.uid means its our own acc
        for message in toggle:
            pText = message.text.lower()
        if ("online" in pText):
            self.markAsRead(author_id)
        log.info("Message {} from {} in {}".format(message_object, thread_id, thread_type))
        msgText = message_object.text.lower()

        if msgText == "say hello, delpi bot!" or msgText == "say hi to them, delpi bot! ":
            client.send(Message(text="Hello! I am delpi bot, created and managed by "
                                     "@Jam Emmanuel Arevalo Villarosa, written in "
                                     "python, using the "
                                     "python FBChat API! I am currently in progress, "
                                     "i would appreciate it if you all could give "
                                     "suggestions as to what i can do, thank you! :)"),
                        thread_id=thread_id,
                        thread_type=thread_type)
        elif msgText == "tell me the weather today" or msgText == "whats the weather like today?" or msgText == "tell me the weather" or msgText == "":
            i = requests.get("https://api.darksky.net/forecast/b2f13b2632333395c57e9dbb5f082cda/14.8528, 120.8154")
            data = i.json()
            for key, value in dict.items(data):
                if key != "currently":
                    pass
                else:
                    a = value
                    val = str(a['windSpeed'])
                    t = round(int((a["temperature"]) - 32) / 1.8)
                    temp = str(round(int((a["temperature"]) - 32) / 1.8))
                    precipProb = str(a['precipProbability'])
                    if 30 <= t <= 32:
                        client.sendRemoteImage(
                            "https://scontent.fmnl8-1.fna.fbcdn.net/v/t1.15752-0/p280x"
                            "280/88225254_655687121857925_6008140458004316160_n.png?_nc"
                            "_cat=107&_nc_sid=b96e70&_nc_ohc=_6zpM_NdEu0AX9pxo1N&_nc_ht="
                            "scontent.fmnl8-1.fna&oh=24fd7c985f65333a985eed448c22aab9&oe=5EFCD9D3",
                            message=Message(text="What's the weather like today?\n"
                                                 + "*OVERCAST*\n" +
                                                 "Wind Speed: " + val + "\n" +
                                                 "Rain probability: " + precipProb + "\n" +
                                                 "Temperature (C): " + temp + "°C \n"
                                                 + "It's getting hot!"),
                            thread_id=thread_id,
                            thread_type=thread_type,
                        )

                    elif 31 <= t <= 35:
                        client.send(Message(text="What's the weather like today?\n "
                                                 + "*OVERCAST*\n" +
                                                 "Windspeed: " + val + "\n" +
                                                 "Rain probability: " + precipProb + "\n" +
                                                 "Temperature (C): " + temp + "°C \n"
                                                 + "It's getting REALLY hot! Make sure to drink water!"
                                            ),
                                    thread_id=thread_id,
                                    thread_type=thread_type)
                    elif t <= 30:
                        client.send(Message(text="What's the weather like today?\n "
                                                 + "*OVERCAST*\n" +
                                                 "Windspeed: " + val + "\n" +
                                                 "Rain probability: " + precipProb + "\n" +
                                                 "Temperature (C): " + temp + "°C \n"
                                                 + "Normal temperature!"
                                            ),
                                    thread_id=thread_id,
                                    thread_type=thread_type)
                    elif 20 <= t <= 25:
                        client.send(Message(text="What's the weather like today?\n "
                                                 + "*OVERCAST*\n" +
                                                 "Windspeed: " + val + "\n" +
                                                 "Rain probability: " + precipProb + "\n" +
                                                 "Temperature (C): " + temp + "°C \n"
                                                 + "It's so cold today!"
                                            ),
                                    thread_id=thread_id,
                                    thread_type=thread_type)
        elif msgText == "am i a dumbbell" or msgText == "dumbbell ba ako":
            rand = random.randrange(1, 100)
            if 1 < rand < 15:
                client.send(Message(
                    text="Pare isa ka sa mga pinaka-malaking dumbbell sa lahat, sorry to tell you the truth."),
                    thread_id=thread_id,
                    thread_type=thread_type)
            elif 15 < rand < 25:
                client.send(Message(
                    text="Pabigat ka, pero hindi ka sobrang pabigat."),
                    thread_id=thread_id,
                    thread_type=thread_type)
            elif 25 < rand < 50:
                client.send(Message(
                    text="Nagiging dumbbell ka kapag malungkot or pagod."),
                    thread_id=thread_id,
                    thread_type=thread_type)
            elif 50 < rand < 75:
                client.send(Message(
                    text="Dumbbell ka talaga, pero kapag tinatamad ka lang."),
                    thread_id=thread_id,
                    thread_type=thread_type)
            elif 75 < rand < 80:
                client.send(Message(
                    text="Dumbbell ka, pero nakakabawi pa rin."),
                    thread_id=thread_id,
                    thread_type=thread_type)
            elif 80 < rand < 100:
                client.send(Message(
                    text="It's your lucky day! Hindi ka dumbbell!"),
                    thread_id=thread_id,
                    thread_type=thread_type)

        elif msgText == "ano commands" or "ano commands nung bot" in msgText:
            client.send(Message(
                text="COMMANDS:\n"
                     "weather: just say 'tell me the weather today.'\n"
                     ""
                     ""
                     "dumbbell-o-meter: just say 'dumbbell ba ako?'\n"
                     "More explanation of the features @ : https://pastebin.com/6yUEA0sR"),
                thread_id=thread_id,
                thread_type=thread_type)



        def sendMsgg():
            if author_id != self.uid:
                self.send(Message(text="Hello!"), thread_id=thread_id, thread_type=thread_type)
            self.markAsDelivered(author_id, thread_id)

        if "online" in pText:
            sendMsgg()


# ####################################################################
# Assigning values


set_interval(check, 18000)
client1 = punkjj("email", "pass")
client1.listen()
