import requests
import hashlib

url = "http://127.0.0.1:5000/post"
aa = input("")
aa = hashlib.sha256(aa.encode)

print(aa)
bb = input("")
payload = {
    'post1'  : f"{aa}",
    'type'   : f"{bb}",
}

response = requests.post(url,data=payload)
print(f"The response is {response}")
print(f"The response text is {response.text}")