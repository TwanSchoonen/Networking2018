#!/usr/bin/env python
from car_request import Request
from enqueue import enqueue
import local_user
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

    decision = input("Option: ")
    while illegal_option(decision, low, high):
        print("Illegal option '" + str(decision) + "'. Please try again")

        decision = input("Option: ")

    return int(decision)


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


def wrong_pos(pos, low, high):
    if pos < low or pos > high:
        return True
    return False


def correct_xy_coordinate(location):
    xy_pos = location.split(',')
    if not len(xy_pos) == 2:
        return False
    if not (represents_int(xy_pos[0]) and represents_int(xy_pos[1])):
        return False
    if wrong_pos(int(xy_pos[0]), 0, 8) or wrong_pos(int(xy_pos[1]), 0, 6):
        return False
    return True


def get_location_xy(request_string):
    location = input(request_string)
    while not correct_xy_coordinate(location):
        location = input("Wrong input, try again. " + request_string)
    return location


def new_request(user):

    print("Creating a new request...")
    centerLocation = input("Center name: ")
    clientLocation = get_location_xy("Client location 'x,y': ")
    no_passengers = input("Number of passengers: ")
    while illegal_option(no_passengers, 1, 3):
        print("Number of passengers (" + no_passengers + ") illegal. Please enter a number between 1 and 3.")
        no_passengers = input("Number of passengers: ")
    destination_center = input("Destination center name: ")
    destination_location = get_location_xy("Destination location 'x,y': ")
    
    req = Request(user.user_name, centerLocation, clientLocation, no_passengers, destination_center, destination_location)

    rabbit_ip = choose_ip()
    enqueue(req, rabbit_ip) #TODO give IP as arg

    print("New request sent: " + req.to_string())


def delete_account(current_user):
    auth = (current_user.user_name, input("You want to delete your account, please reenter your password: "))
    res = requests.delete(url, auth=auth, headers=headers)

    print(res)
    if res.status_code == 201:
        return True

    return False


def change_details(current_user):
    opts = ["change password", "change your username", "change your first name", "change your last name",
            "change your date of birth", "change your street name", "change your house number", "change your city"]
    opt = option_menu(opts, 1, 8)
    pw = input("You want to change your details, please reenter your password: ")
    auth = (current_user.user_name, pw)

    if opt == 1:
        new_pw = input("Please enter your new password: ")
        data = current_user.get_json(new_pw)
    elif opt == 2:
        current_user.user_name = input("Please enter your new username: ")
        data = current_user.get_json(pw)
    elif opt == 3:
        current_user.first_name = input("Please enter your new first name: ")
        data = current_user.get_json(pw)
    elif opt == 4:
        current_user.last_name = input("Please enter your new last name: ")
        data = current_user.get_json(pw)
    elif opt == 5:
        current_user.birthdate = input("Please enter your new date of birth: ")
        data = current_user.get_json(pw)
    elif opt == 6:
        current_user.street_name = input("Please enter your new street name: ")
        data = current_user.get_json(pw)
    elif opt == 7:
        current_user.house_number = input("Please enter your new house number: ")
        data = current_user.get_json(pw)
    elif opt == 8:
        current_user.city = input("Please enter your new city of residence: ")
        data = current_user.get_json(pw)

    requests.put(url, data=json.dumps(data), auth=auth, headers=headers)


def user_details(current_user):
    opts = ["change details", "delete account", "go back"]
    opt = option_menu(opts, 1, 3)
    if opt == 1:
        change_details(current_user)
    elif opt == 2:
        if delete_account(current_user):
            return True
    elif opt == 3:
        pass
    return False


def receive_input(field_name):
    field = input(field_name + ": ")
    while field == "":
        field = input(field_name + ": ")
    return field


def get_user_info():
    user_name = receive_input("Username")
    password = receive_input("Password")
    first_name = receive_input("First name")
    last_name = receive_input("Last name")
    birth_date = receive_input("Date of birth")
    street_name = receive_input("Street name")
    house_number = receive_input("House number")
    city = receive_input("City of residence")

    data = {"username": user_name, "password": password, "firstname": first_name, "lastname": last_name,
            "birthdate": birth_date, "streetname": street_name, "housenumber": house_number, "city": city, "balance": 0.0}

    return requests.post(url, data=json.dumps(data), headers=headers)


def register_new_user():
    res = get_user_info()
    while res.status_code == 500:
        print("Error in creating user, try again")
        res = get_user_info()

    return local_user.User(res.json())


def log_in():
    auth = (input("Username: "), input("Password: "))
    res = requests.get(url, auth=auth, headers = headers)
    while res.status_code == 401:
        print("bad request")
        auth = (input("Username: "), input("Password: "))
        res = requests.get(url, auth=auth, headers=headers)
    print("status code: " + str(res.status_code))
    return local_user.User(res.json())


def show_database():
    auth = ("root", "root")
    res = requests.get(url + "all", auth=auth, headers=headers)
    print(res.json())


def delete_database():
    auth = ("root", "root")
    res = requests.delete(url + "all", auth=auth, headers=headers)
    print(res.status_code)
    print(res.json())


def show_admin_options():
    opts = ["show the database", "delete the database"]
    opt = option_menu(opts, 1, 2)
    if opt == 1:
        show_database()
    elif opt == 2:
        delete_database()


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
            opts = ["request a new ride", "see/change your account details", "log out"]
            opt = option_menu(opts, 1, 3)
            if opt == 1:
                new_request(current_user)
            elif opt == 2:
                log_out = user_details(current_user)
            elif opt == 3:
                log_out = True
            if log_out:
                print("Logging out...")
                break


if __name__ == "__main__":
    main(sys.argv)
