
class User:
    def __init__(self, username, password, age, street_name, house_number, city):
        self.user_name = username
        self.password = password
        self.age = age
        self.street_name = street_name
        self.house_number = house_number
        self.city = city
        self.balance = 0.0

    def user_exists(self):
        pass