#!/usr/bin/env python
import pika
import sys
import request


def represents_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def illegal_no_passengers(n_psngrs):
    if not represents_int(n_psngrs):
        return True
    elif int(n_psngrs) < 1 or int(n_psngrs) > 3:
        return True
    return False


def find_nearest_center(lctn):
    return lctn


name = raw_input("Username: ")
location = raw_input("Location: ")
no_passengers = raw_input("Number of passengers: ")
while illegal_no_passengers(no_passengers):
    print("Number of passengers (" + no_passengers + ") illegal. Please enter a number between 1 and 3.")
    no_passengers = raw_input("Number of passengers: ")
destination = raw_input("Destination: ")

new_request = request.Request(name, location, no_passengers, destination)


connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='topic_logs',
                         exchange_type='topic')

routing_key = find_nearest_center(location)

channel.basic_publish(exchange='topic_logs',
                      routing_key=routing_key,
                      body=new_request.to_string())

print(" [x] Sent %r%r" % (routing_key, new_request.to_string()))
connection.close()