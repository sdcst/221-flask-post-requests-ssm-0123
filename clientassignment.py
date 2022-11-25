import requests
import hashlib


def postrequest():
    url = "http://127.0.0.1:5000/post"
    aa = input("")
    bb = input("")
    payload = {
        'post1'  : f"{aa}",
        'type'   : f"{bb}",
    }

    response = requests.post(url,data=payload)
    print(f"The response is {response}")
    print(f"The response text is {response.text}")

def listrequest():
    url = "http://127.0.0.1:5000/requestlist"
    bb = input("")
    payload = {
        'type'   : f"{bb}",
    }

    response = requests.post(url,data=payload)
    print(f"The response is {response}")
    print(f"The response text is {response.text}")

listrequest()