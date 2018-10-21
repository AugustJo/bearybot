import time

from bearychat import openapi
from bearychat import RTMClient

from rtm_loop import RTMLoop

# client = RTMClient("rtm_token", "https://rtm.bearychat.com")
client = RTMClient("4b7d8bc623ad2513c345f9284d1ed789", "https://rtm.bearychat.com")
# client = RTMClient('4b7d8bc623ad2513c345f9284d1ed789')
# client = openapi.Client('4b7d8bc623ad2513c345f9284d1ed789')

# init the rtm client
resp = client.start()  # get rtm user and ws_host
# resp = client.rtm.start()

user = resp["user"]
ws_host = resp["ws_host"]

loop = RTMLoop(ws_host)  # init the loop
loop.start()
time.sleep(2)
loop.ping()

while True:
    error = loop.get_error()

    if error:
        print(error)
        continue

    message = loop.get_message(True, 5)

    if not message or not message.is_chat_message():
        continue
    try:
        print("rtm loop received {0} from {1}".format(message["text"],
                                                      message["uid"]))
    except:
        continue

    if message.is_from(user):
        continue
    loop.send(message.refer("Pardon?"))