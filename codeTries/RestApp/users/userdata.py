import os, json
from flask import jsonify

class UserData:
    userList = []
    def __init__(self, userDir):
        self.userDir = userDir
        self.userID = self.populate_users(userDir)
        
    def populate_users(self, userDir):
        json_files = [pos_json for pos_json in os.listdir(userDir)
                      if pos_json.endswith('.json')]
        for user in json_files:
            with open(userDir + user) as json_data:
                d = json.load(json_data)
                self.userList.append(d)
        return len(json_files)

    def write_user_file(self, user): 
        with open(self.userDir + 'usr' + user['usrId']
                  + '.json', 'w') as outfile:
            json.dump(user, outfile)


