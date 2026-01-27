import json

json_data = """
{
  "name": "Ivanka",
  "age": "22",
  "isStudent": "false",
  "courses": ["Python", "QA Automation", "API Testing"],
  "address:": {
    "city": "NN",
    "zipcode": "050200"
  }

}"""
parsed_json = json.loads(json_data)
print(parsed_json['name'], type(parsed_json))

data = {
    'name': 'Roberto',
    'age': '22',
    'isStudent': 'false',
    'courses': ['DevOps', 'Golang', 'REST_API'],
}
json_string = json.dumps(data, indent=4)
print(json_string)
print(json_string, type(json_string))

with open('json_example.json', 'r', encoding="utf-8") as file:
    data = json.load(file)
    print(data, type(data))

with open('json_user.json', 'w', encoding="utf-8") as file:
    json.dump(data, file, indent=4)