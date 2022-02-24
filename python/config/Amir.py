#!/usr/bin/python

import logging
import ecs_logging
import time
from random import randint

#logger = logging.getLogger(__name__)
logger = logging.getLogger("app")
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler('Amir.json')
handler.setFormatter(ecs_logging.StdlibFormatter())
logger.addHandler(handler)

print("Generating log entries...")

messages = [
    "Amir has left the building.",#
    "Amir has left the oven on.",
    "Amir has two left feet.",
    "Amir was left out in the cold.",
    "Amir was left holding the baby.",
    "Amir left the cake out in the rain.",
    "Amir came out of left field.",
    "Amir exited stage left.",
    "Amir took a left turn.",
    "Amir left no stone unturned.",
    "Amir picked up where he left off.",
    "AMir's train has left the station."
    ]

while True:
    random1 = randint(0,15)
    random2 = randint(1,10)
    if random1 > 11:
        random1 = 0
    if(random1<=4):
        logger.info(messages[random1], extra={"http.request.body.content": messages[random1]})
    elif(random1>=5 and random1<=8):
        logger.warning(messages[random1], extra={"http.request.body.content": messages[random1]})
    elif(random1>=9 and random1<=10):
        logger.error(messages[random1], extra={"http.request.body.content": messages[random1]})
    else:
        logger.critical(messages[random1], extra={"http.request.body.content": messages[random1]})
    time.sleep(random2)
