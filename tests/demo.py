import requests
import json

BASE_URL = "http://127.0.0.1:8000/validate"

for name in ["valid", "invalid"]:
    with open(f"samples/{name}.json") as f:
        payload = json.load(f)

    res = requests.post(BASE_URL, json=payload)
    print(f"\n{name.upper()} RESPONSE:")
    print(res.json())
