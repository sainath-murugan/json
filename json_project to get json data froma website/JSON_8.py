import json
import requests

request = requests.get("http://www.floatrates.com/daily/inr.json")
request_txt = request.text

data = json.loads(request_txt)

with open("project.json", "w", encoding="utf-8") as file_1:
    res = json.dump(data, file_1, indent=4, ensure_ascii=False, separators=(",", ":"))

# try this website to work with json data http://www.floatrates.com/json-feeds.html
