#encoding:utf-8
import sys
import time
import json
import threading

import websocket

from bearychat import RTMMessage, RTMMessageType
from bearychat import openapi
from bearychat import incoming

from pprint import pprint

client = openapi.Client('4b7d8bc623ad2513c345f9284d1ed789')
client.rtm.start()

client.channel.list()
pprint.pprint(client.channel.list())


if sys.version_info > (3, ):
    from queue import Queue
    from _thread import start_new_thread
else:
    from Queue import Queue
    from thread import start_new_thread



data = {
  "text": "愿原力与你同在",
  "attachments": [
    {
      "title": "Star Wars III",
      "text": "Return of the Jedi",
      "color": "#ffa500"
    }
  ]
}