import time
from pprint import pprint

from bearychat import RTMClient
# from bearychat import openapi
from rtm_loop import RTMLoop


def main():
    # init the rtm client
    # client = RTMClient("rtm_token", "https://rtm.bearychat.com")
    client = RTMClient("4b7d8bc623ad2513c345f9284d1ed789", "https://rtm.bearychat.com")
    # client = openapi.Client('4b7d8bc623ad2513c345f9284d1ed789')
    # client = openapi.Client('4b7d8bc623ad2513c345f9284d1ed789')

    resp = client.start()  # get rtm user and ws_host
    # resp = client.rtm.start()
    print("client.start()")

    user = resp["user"]
    ws_host = resp["ws_host"]
    pprint(user)
    pprint(ws_host)

    loop = RTMLoop(ws_host)  # init the loop
    loop.start()
    time.sleep(10)
    loop.ping()

    while True:
        error = loop.get_error()

        if error:
            print(error)
            print(1)
            continue

        message = loop.get_message(True, 5)

        if not message or not message.is_chat_message():
            print(2)
            continue
        try:
            pprint()
            print("rtm loop received {0} from {1}".format(message["text"],
                                                          message["uid"]))
        except Exception:
            print(3)
            continue

        if message.is_from(user):
            print(4)
            continue
        loop.send(message.refer("Pardon?"))


if __name__ == '__main__':
    main()
