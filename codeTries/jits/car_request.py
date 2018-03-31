#!/usr/bin/env python


class Request:
    def __init__(self, username, centerLocation, clientLocation, no_passengers, destination):
        self.user_name = username
        self.centerLocation = centerLocation
        self.clientLocation = clientLocation
        self.no_passengers = no_passengers
        self.destination = destination

    def to_string(self):
        return ", ".join([self.user_name, self.centerLocation, self.clientLocation, self.no_passengers, self.destination])
