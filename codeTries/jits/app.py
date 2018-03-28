#!/usr/bin/env python
from car_request import Request, enqueue
import user
import requests
import json
from flask import jsonify
import sys


# url = "http://145.97.184.144:5000/data" #default url

url = "http://127.0.0.1:5000/data"  # default REST url
default_rabbit_url = "localhost"


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


def option_menu(options, low, high):
    cnt = 1
    for opt in options:
        print("- To " + opt + ", press " + str(cnt))
        cnt += 1

    decision = int(input("Option: "))
    while illegal_option(decision, low, high):
        print("Illegal option '" + str(decision) + "'. Please ty again")
        decision = int(input("Option: "))

    return decision


def find_nearest_center(lctn):
    return lctn


def choose_ip():
    rabbit_ip = default_rabbit_url
    answer = input("Do you want to connect to " + rabbit_ip + "? (y/n): ")
    while not (answer == "y" or answer == "n"):
        answer = input("Invalid response, do you want to connect to " + rabbit_ip + "? (y/n): ")
    if answer == "y":
        return rabbit_ip
    elif answer == "n":
        rabbit_ip = input("Give the IP you want to connect to: ")
        return rabbit_ip


def new_request(user):

    print("Creating a new request...")
    location = input("Location: ")
    no_passengers = input("Number of passengers: ")
    while illegal_option(no_passengers, 1, 3):
        print("Number of passengers (" + no_passengers + ") illegal. Please enter a number between 1 and 3.")
        no_passengers = input("Number of passengers: ")
    destination = input("Destination: ")
    
    req = Request(user.user_name, location, find_nearest_center(location), no_passengers, destination)

    rabbit_ip = choose_ip()
    enqueue(req, rabbit_ip) #TODO give IP as arg

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
        "lastName": input("Last name: "),
        "telephone": input("Phone number: "),
        'usrId': userID,
    }
    return jsonify({'user': new_user}), 201


def track_ride():
    print("Tracking ride...")


def show_map():
    print("Showing map...")


def switch_user():
    print("Switch user")


def delete_account(current_user):
    auth = (current_user.user_name, input("You want to delete your account, please reenter your password: "))
    res = requests.delete(url, auth=auth, headers=headers)

    print(res)
    if res.status_code == 201:
        return True

    return False


def user_details(current_user):
    opts = ["change password/username", "delete account", "go back"]
    opt = option_menu(opts, 1, 3)
    if opt == 1:
        pass
    elif opt == 2:
        if delete_account(current_user):
            return True
    elif opt == 3:
        pass
    return False


def make_user(res_json):
    print("make user:")
    print(res_json)
    usr = res_json["username"]
    return user.User(usr)


def register_new_user():
    username = input("Username: ")
    while username == "":
        username = input("Username: ")

    password = input("Password: ")
    while password == "":
        password = input("Password: ")

    data = {"username": username, "password": password}

    print("data = " )
    print(json.dumps(data))

    res = requests.post(url, data=json.dumps(data), headers=headers)
    print(res)

    return make_user(res.json())


def log_in():
    auth = (input("Username: "), input("Password: "))
    res = requests.get(url, auth=auth)
    while res.status_code == 401:
        print("bad request")
        auth = (input("Username: "), input("Password: "))
        res = requests.get(url, auth=auth, headers=headers)
        
    print(res.json())
    return make_user(res.json())


def show_database():
    auth = ("root", "root")

    res = requests.get(url + "all", auth=auth, headers=headers)
    print(res.json())


def show_admin_options():
    print("admin options")


def new_server_ip():
    global url
    new_url = input("Give the new ip that should be used for the server: ")
    url = new_url


def main(argv):
    while True:
        if len(argv) == 2 and argv[1] == "admin":
            show_admin_options()
            break

        opts = ["register a new user", "log in", "change server ip", "exit"]
        opt = option_menu(opts, 1, 4)
        if opt == 1:
            current_user = register_new_user()
        elif opt == 2:
            current_user = log_in()
        elif opt == 3:
            new_server_ip()
            # go through this menu again
            continue
        elif opt == 4:
            print("Bye bye...")
            break

        log_out = False
        while True:
            print("\nCurrently logged in as " + current_user.user_name)
            opts = ["request a new ride", "track your ride", "see the map", "see/change your account details", "log out"]
            opt = option_menu(opts, 1, 5)
            if opt == 1:
                new_request(current_user)
            elif opt == 2:
                track_ride()
            elif opt == 3:
                show_map()
            elif opt == 4:
                log_out = user_details(current_user)
            elif opt == 5:
                log_out = True
            if log_out:
                print("Logging out...")
                break


if __name__ == "__main__":
    main(sys.argv)
