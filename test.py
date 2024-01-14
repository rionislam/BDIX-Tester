import requests
import json

file = open("targets.json")
targets = json.load(file)
file.close()

try:
    for host in targets.get("hosts", []):
        try:
            response = requests.get(host, timeout=1)
            response.raise_for_status()
            status = response.status_code
        except requests.exceptions.RequestException as e:
            status = 'error'
            
            continue

        if status == 200:
            time = response.elapsed.total_seconds()
            size = len(response.content)
            speed = (size * 8) / (time * 1000000)
            print(f"Host: {host} AND Speed: {speed:.2f} Mbps\n")

        response.close()

except KeyboardInterrupt:
    print("\nScript terminated by user (Ctrl+C).")

