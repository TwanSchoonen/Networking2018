#!/usr/bin/python
import socket
import threading

class ThreadedServer(object):
    def __init__(self, host, port):
        self.client_list = set()
        self.client_lock = threading.Lock()
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))
        
    def start_server(self):
        print("starting server on %s:%s" % (self.host, self.port))
        self.sock.listen(5)
        while True:
            client, address = self.sock.accept()
            # client.settimeout(60)
            print("[New connection from %s:%s]:" % (address[0],address[1]))
            with self.client_lock:
                self.client_list.add(client)
            thrd = threading.Thread(target = self.listenToClient,args = (client,address))
            # makes sure the thread stops when main stops
            thrd.setDaemon(True)
            thrd.start()

    def askLocation(self):
        locations = []
        print("asking location")
        with self.client_lock:
            for c in self.client_list:
                c.send(str.encode("Location?"))
                location = c.recv(1024)
                locations.append(location.decode("utf-8"))
                # if not data:
        return locations

    def listenToClient(self, client, address):
        size = 1024
        while True:
            try:
                data = client.recv(size)
                if data:
                    # Set the response to echo back the recieved data 
                    print("got from client: %s\n" % data)
                    response = data
                    if data == str.encode("allloc"):
                        with self.client_lock:
                            for c in self.client_list:
                                print("sending: %s as broadcast\n" % data)
                                c.send(data)
                    else:
                        print("sending: %s as response\n" % data)
                        client.send(response)
                else:
                    raise error('Client disconnected')
            except:
                # connection clean up
                with self.client_lock:
                    print("remove client")
                    self.client_list.remove(client)
                    client.close()
                    return False

# if __name__ == "__main__":
#     ThreadedServer('localhost', 5555).start_server()

