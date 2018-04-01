#!/usr/bin/env python


class Request:
    def __init__(self, username, centerLocation, clientLocation, no_passengers, destination_center, destination_location):
        self.user_name = username
        self.centerLocation = centerLocation
        self.clientLocation = clientLocation
        self.no_passengers = no_passengers
        self.destination_center = destination_center
        self.destination_location = destination_location

    def to_string(self):
        return ", ".join([self.user_name, self.centerLocation, self.clientLocation, self.no_passengers,
                          self.destination_center, self.destination_location])
