# reading file to file

import json

with open("f.json", "r") as file:
    file_1 = json.load(file)

with open("file_handle.json", "w") as file:
    json.dump(file_1, file, indent=4, sort_keys=True)
