#!/usr/bin/env python
import pika
import sys
import requests


IP = "192.168.0.109"


class Request:
    def __init__(self, username, location, center, no_passengers, destination):
        self.user_name = username
        self.location = location
        self.center = center
        self.no_passengers = no_passengers
        self.destination = destination

    def to_string(self):
        print("self: " + ", ".join([self.user_name, self.location, self.center, self.no_passengers, self.destination]))
        return ", ".join([self.user_name, self.location, self.center, self.no_passengers, self.destination])


def enqueue(req):
    # credentials = pika.PlainCredentials('twan', 'root')
    # connection = pika.BlockingConnection(pika.ConnectionParameters(host=IP,port=port,credentials=credentials))
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=IP))

    channel = connection.channel()

    channel.exchange_declare(exchange='topic_logs',
                             exchange_type='topic')

    routing_key = req.center

    channel.basic_publish(exchange='topic_logs',
                          routing_key=routing_key,
                          body=req.to_string())

    print(" [x] Sent %r%r" % (routing_key, req.to_string()))
    connection.close()
