import json


class User:
    def __init__(self, res_json): #res_json gives only username
        self.user_name = res_json["username"]
        self.first_name = res_json["firstname"]
        self.last_name = res_json["lastname"]
        self.birth_date = res_json["birthdate"]
        self.street_name = res_json["streetname"]
        self.house_number = res_json["housenumber"]
        self.city = res_json["city"]
        self.balance = res_json["balance"]

    def get_json(self, pw):
        data = {"username": self.user_name, "password": pw, "firstname": self.first_name, "lastname": self.last_name,
                "birthdate": self.birth_date, "streetname": self.street_name, "housenumber": self.house_number,
                "city": self.city, "balance": self.balance}
        return json.dumps(data)