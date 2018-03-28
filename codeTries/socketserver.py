import socket
import threading

client_list = []

class ThreadedServer(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))

    def listen(self):
        self.sock.listen(5)
        i = 0
        while True:
            client, address = self.sock.accept()
            # client.settimeout(60)
            client_info = [client, address]
            client_list.append(client_info)
            print("[New connection from %s]:" % client_list[i][1][0])
            i += 1
            if i == 3:
                for j in range(0,i):
                    client_list[j][0].send(str.encode("test"))
            # threading.Thread(target = self.listenToClient,args = (client,address)).start()

    def listenToClient(self, client, address):
        size = 1024
        while True:
            try:
                data = client.recv(size)
                # if data:
                #     # Set the response to echo back the recieved data 
                #     # response = data
                #     # client.send(response)
                # else:
                #     raise error('Client disconnected')
            except:
                client.close()
                return False

if __name__ == "__main__":
    while True:
        port_num = input("Port? ")
        try:
            port_num = int(port_num)
            break
        except ValueError:
            pass

    ThreadedServer('localhost',port_num).listen()

