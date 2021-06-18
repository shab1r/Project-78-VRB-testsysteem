import socket
import time
import threading


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

        if message == "{quit}":
            self.clientSocket.close()

        return 200


client = Client()

def receive(self, gui, Motor_thread):
        print("kont")
        while True:
            try:
                msg = self.clientSocket.recv(1024).decode("utf8")
                l = list(msg.split(','))

                if '1' in l[0]:
                    print( "motor moet aangestuurd worden")
                    if '1' in l[1]:
                        print( "motor 1 moet aangestuurd worden")
                        if  '1' in l[2]:
                            power = l[3].replace(']','')
                            print("motor 1 moet aangezet worden op: ",power)
                            
                            Motor_thread.Run_Motor1(gui, float(power))

                        else :
                            print("motor 1 moet uitgezet worden")
                            Motor_thread.turnOffMotor1(gui)

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
                        client.sendRequest("{quit}")
                else: 
                    print("no value")
                    
            except OSError:  # Possibly client has left the chat.
                break

def start(gui, Motor_thread):
    thread = threading.Thread(target=receive, args=(client,gui,Motor_thread,))
    thread.start()
    client.sendRequest("client")