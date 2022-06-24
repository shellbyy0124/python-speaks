from datetime import date

import espeakng
import time
import json


class MyAssistant:
    def __init__(self):
        self.today = date.today()
        self.sayHello()

    def sayHello(self):
        with open('./users.json', 'r', encoding='utf-8-sig') as f:
            data = json.load(f)

            engine = espeakng.Speaker()
            engine.say(f'Hello {data["users"]["name"]}, Nice To Meet You!')
            time.sleep(3)
            self.getDate()

    def getDate(self):
        engine = espeakng.Speaker()
        today = self.today.strftime("%B, %d, %Y")
        engine.say(f"Today Is: {today}", wait4prev=True)
        time.sleep(5)
        self.getTime()

    def getTime(self):
        engine = espeakng.Speaker()
        timevalue_12hour = time.strftime("%I:%M %p")
        engine.say(f"The Current Time Is {timevalue_12hour}", wait4prev=True)


if __name__ == '__main__':
    MyAssistant()
