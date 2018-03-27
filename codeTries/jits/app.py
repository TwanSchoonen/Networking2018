from car_request import Request, enqueue
import user
import requests
import json
from flask import jsonify


url = "http://127.0.0.1:5000/data"
headers = {'content-type': 'application/json'}


def represents_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def illegal_option(opt, low, high):
    if not represents_int(opt):
        return True
    elif int(opt) < low or int(opt) > high:
        return True
    return False


def find_nearest_center(lctn):
    return lctn


def new_request(user):
    print("Creating a new request...")
    location = raw_input("Location: ")
    no_passengers = raw_input("Number of passengers: ")
    while illegal_option(no_passengers, 1, 3):
        print("Number of passengers (" + no_passengers + ") illegal. Please enter a number between 1 and 3.")
        no_passengers = raw_input("Number of passengers: ")
    destination = raw_input("Destination: ")

    req = Request(user, location, find_nearest_center(location), no_passengers, destination)
    enqueue(req)

    print("New request: " + req.to_string())


def create_new_user(nm):
    print("Creating new user " + nm + "...")
    userID = str(20)
    new_user = {
        "balance": "100",
        "bankNumber": "JC44-5356-4200",
        "dateOfRegister": "21/3/2018",
        "firstName": nm,
        "lastLogin": "21/3/2018",
        "lastName": raw_input("Last name: "),
        "telephone": raw_input("Phone number: "),
        'usrId': userID,
    }
    return jsonify({'user': new_user}), 201



def track_ride():
    print("Tracking ride...")


def exists(nm):
    print("Checking if user exists...")
    req = requests.get(IP + nm)#.json()
    if 'user' in req:
        print("User " + nm + " exists")
        return True
    print "User " + nm + " does not yet exist"
    return False


def show_map():
    print("Showing map...")


def switch_user():
    print("Switch user")


def user_details():
    print("Showing user details...")


def make_user(res_json):
    print(res_json)
    print(res_json["username"])
    return 'a'


def register_new_user():
    username = raw_input("Username: ")
    while username == "":
        username = raw_input("Username: ")

    password = raw_input("Password: ")
    while password == "":
        password = raw_input("Password: ")

    data = {"username": username, "password": password}

    print("data = " )
    print(json.dumps(data))
    print(jsonify({'username': username, 'password': password}))

    res = requests.post(url, data=json.dumps(data), headers=headers)
    print("res = ")
    print(res)

    return make_user(res.json())


def log_in():
    auth = (raw_input("Username: "), raw_input("Password: "))

    res = requests.get(url, auth=auth)
    while res.status_code == 401:
        print("bad request")
        auth = (raw_input("Username: "), raw_input("Password: "))
        res = requests.get(url, auth=auth, headers=headers)

    print(res.json())
    return make_user(res.json())


#             start here             #
option = raw_input("- To register a new user, press '1'\n- To log in, press '2'.\n")
while illegal_option(option, 1,2):
    option = raw_input("- To register a new user, press '1'\n- To log in, press '2'.\n")

if int(option) == 1:
    current_user = register_new_user()
elif int(option) == 2:
    current_user = log_in()


while True:
    option = raw_input("- To request a new ride, press '1'\n- To track your ride, press '2'.\n"
                       "- To see the map, press '3'.\n- To see/change your account details, press '4'.\n"
                       "- To switch user, press '5'.\n- To log out press '6'.\n")

    while illegal_option(option, 1, 5):
        print("The picked option (" + option + ") is illegal.")
        option = raw_input("- To request a new ride, press '1'\n- To track your ride, press '2'.\n"
                           "- To see the map, press '3'.\n- To see/change your account details, press '4'.\n"
                           "- To switch user, press '5'\n- To log out press '6'.\n")

    opt = int(option)
    if opt == 1:
        new_request(user['user']['firstName'])
    elif opt == 2:
        track_ride()
    elif opt == 3:
        show_map()
    elif opt == 4:
        user_details()
    elif opt == 5:
        switch_user()
    elif opt == 6:
        print("Logging out...")
        break
