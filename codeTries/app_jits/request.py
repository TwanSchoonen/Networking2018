class Request:
    def __init__(self, name, location, no_passengers, destination):
        self.name = name
        self.location = location
        self.no_passengers = no_passengers
        self.destination = destination

    def to_string(self):
        return ", ".join([self.name, self.location, self.no_passengers, self.destination])