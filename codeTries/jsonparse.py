import os, json

    
path_to_json = '../testUsers'
json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]
print(json_files)  # for me this prints ['foo.json']

for user in json_files:
    with open("../testUsers/" + user) as json_data:
        d = json.load(json_data)
        print(d)
