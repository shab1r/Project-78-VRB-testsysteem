import socket
import time
import threading

HEADER = 140
FORMAT = 'utf-8'

class Client():
    def __init__(self):
        self.clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clientSocket.connect(("95.217.181.53", 5050))
        self.message = ''

    def sendRequest(self, message):
        print('this will send the message=' + str(message))
        x = "A"
        b = "!/$0"        
        name = "api"
        self.clientSocket.send(bytes(name, "utf8"))
        time.sleep(0.1)
        strMessage = str(message)
        # print(strMessage)
        self.clientSocket.send(bytes(strMessage, "utf8"))
        time.sleep(0.1)
        # self.clientSocket.send(bytes(str("{quit}"), "utf8"))
        # time.sleep(0.1)
        # self.clientSocket.close()
        if message == "{quit}":
            self.clientSocket.close()

        return 200


    def receive(self):  
        while True:
            try:
                msg = self.clientSocket.recv(1024).decode("utf8")
                l = list(msg.split(','))

                if '1' in l[0]:
                    print( "motor moet aangestuurd worden")
                    if '1' in l[1]:
                        print( "motor 1 moet aangestuurd worden")

                        if  '1' in l[2]:
                            print("motor 1 moet aangezet worden op: ",l[3])

                        else :
                            print("motor 1 moet uitgezet worden")

                    elif '2' in l[1]:
                        print("motor 2 moet aangezet worden")

                        if  '1' in l[2]:
                            print("motor 2 moet aangezet worden op: ",l[3])

                        else :
                            print("motor 2 moet uitgezet worden")

                    elif '3' in l[1]:
                        print("beide motors moeten aan")

                elif '2' in l[0]:
                        print("timer moet aangestuurd worden")
                elif '3' in l[0]:
                        print("geen idee wat aangestuurd moet worden")
                elif '4' in l[0]:
                        "weer geen idee"
                        client.sendRequest("{quit}")
                else: 
                    print("no value")
                    
            except OSError:  # Possibly client has left the chat.
                break

client = Client()
thread = threading.Thread(target=client.receive)
thread.start()
client.sendRequest("client")