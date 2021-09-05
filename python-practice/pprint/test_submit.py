import json
import requests

json_string = ""
with open("json_string") as f:
    lines = f.readlines()
    json_string = lines[0]
loaded_json = json.loads(json_string)
formatted_string = json.dumps(loaded_json, indent=4)
# print(json_string)
print(formatted_string)
# print(type(formatted_string))
# print(json.loads(formatted_string))
# print(json_string)
# print(loaded_json)
# print(type(loaded_json))
# print(json.loads(formatted_string))
r = requests.post(
    "https://www.coursera.org/api/onDemandProgrammingScriptSubmissions.v1",
    json=loaded_json,
)
print(r.status_code)
print(r.json())