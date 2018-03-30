#!/usr/bin/env python


class Request:
    def __init__(self, username, location, center, no_passengers, destination):
        self.user_name = username
        self.location = location
        self.center = center
        self.no_passengers = no_passengers
        self.destination = destination

    def to_string(self):
        return ", ".join([self.user_name, self.location, self.center, self.no_passengers, self.destination])
