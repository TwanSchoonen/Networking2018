import request


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


def exists(nm):
    print("Checking if user exists...")
    print("Not implemented yet, returns true")
    return True


def find_nearest_center(lctn):
    return lctn


def new_request(nm):
    print("Creating a new request...")
    name = nm
    location = raw_input("Location: ")
    no_passengers = raw_input("Number of passengers: ")
    while illegal_option(no_passengers, 1, 3):
        print("Number of passengers (" + no_passengers + ") illegal. Please enter a number between 1 and 3.")
        no_passengers = raw_input("Number of passengers: ")
    destination = raw_input("Destination: ")

    req = request.Request(name, location, no_passengers, destination)
    print("New request: " + req.to_string())


def track_ride():
    print("Tracking ride...")


def show_map():
    print("Showing map...")


def user_details():
    print("Showing user details...")


def log_out():
    print("Logging out...")


name = raw_input("Username: ")
print("Ignoring input '" + name + "', username not implemented yet")
password = raw_input("Password: ")
print("Ignoring input '" + password + "', password not implemented yet")


if exists(name):
    print("Retrieving user " + name + "...")
    #TODO user = db.retrieve_from_server(name, password)
    print("Not implemented yet, continuing")
else:
    age = raw_input("Age: ")
    street_name = raw_input("Streetname: ")
    house_number = raw_input("House number: ")
    city = raw_input("City: ")

    print("Creating user " + name + "...")
    print("Not implemented yet, continuing")
    #TODO user = db.make_new_user(name, age, street_name, house_number, city, password)


while True:
    option = raw_input("- To request a new ride, press '1'\n- To track your ride, press '2'.\n"
                       "- To see the map, press'3'.\n- To see/change your account details, press '4'.\n"
                       "- To log out press '5'.\n")

    while illegal_option(option, 1, 5):
        print("The picked option (" + option + ") is illegal.")
        option = raw_input("- To request a new ride, press '1'\n- To track your ride, press '2'.\n"
                           "- To see the map, press'3'.\n- To see/change your account details, press '4'.\n"
                           "- To log out press '5'.\n")

    opt = int(option)
    if opt == 1:
        new_request(name)
    elif opt == 2:
        track_ride()
    elif opt == 3:
        show_map()
    elif opt == 4:
        user_details()
    elif opt == 5:
        log_out()
        break
