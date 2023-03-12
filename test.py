import requests
import json

file = open("targets.json")
targets = json.load(file)
length = len(targets["hosts"])
for i in range(0, length):
    host = targets["hosts"][i]
    try:
        response = requests.get(host, timeout=1)
        status = response.status_code
    except:
        status = 'error'
        response.close()
    if status == 200:
        time = response.elapsed.total_seconds()/1000
        size = ((len(response.text))/1000000)/8
        speed = size/time
        print (f"Host: {host} AND Speed: {format(speed, '.2f') }MBps\n")

