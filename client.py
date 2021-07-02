import socket
import time
import threading


class Client():
    def __init__(self):
        self.clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clientSocket.connect(("95.217.181.53", 5050))
        self.message = ''

    def sendRequest(self, message, name):
#         print('this will send the message=' + str(message))
        x = "A"
        b = "!/$0"        
        name = name
        self.clientSocket.send(bytes(name, "utf8"))
        time.sleep(0.1)
        strMessage = str(message)
        # print(strMessage)
        self.clientSocket.send(bytes(strMessage, "utf8"))
        time.sleep(0.1)

        if message == "{quit}":
            self.clientSocket.close()
    
            

def receive(self, gui, Motor_thread, Charge, GUI2):
    while True:
        try:
            msg = self.clientSocket.recv(1024).decode("utf8")
            #print(msg)
            l = list(msg.split(','))
            if '[1' in l[0]:
#                 print( "motor moet aangestuurd worden")
                if '1' in l[1]:
#                     print( "motor 1 moet aangestuurd worden")
                    if  '1' in l[2]:
                        power = l[3].replace(']','')
#                         print("motor 1 moet aangezet worden op: ",power)
                        
                        Motor_thread.Run_Motor1(gui, float(power))
                    elif '2' in l[2] :
#                         print("motor 1 moet uitgezet worden")
                        Motor_thread.turnOffMotor1(gui)

                elif '2' in l[1]:
#                     print("motor 2 moet aangezet worden")
                    if  '1' in l[2]:
                        power2 = l[3].replace(']','')
#                         print("motor 2 moet aangezet worden op: ",power2)

                        Motor_thread.Run_Motor2(gui, float(power2))
                    elif '2' in l[2]:
#                         print("motor 2 moet uitgezet worden")
                        Motor_thread.turnOffMotor2(gui)

                elif '3' in l[1]:
#                     print("beide motors moeten aan")
                    if '1' in l[2]:
                        print("=============")
                        print(l)
                        print("===")
                        power3 = l[3].replace(',', '')
                        print(power3)
                        power4 = l[4].replace(']','')
#                         print("beide motoren moeten aan op: ",power3)
                        Motor_thread.Run_BothMotors(gui, float(power3), float(power4))

                    elif '2' in l[2]:
#                         print("beide motors moeten uit")
                        Motor_thread.turnBothMotorsOff(gui)

            elif '[2' in l[0]:
                    print("timer moet aangestuurd worden")
                    if '1' in l[1]:
#                         print("timer 1 moet aangestuurd worden")
                        GUI2.resetTime(gui)
                        
                    if '2' in l[1]:
#                         print("timer 2 moet gereset worden")
                        GUI2.resetTime2(gui)
                    
                    elif '3' in l[1]:
#                         print("beide timers moeten gereset worden")
                        GUI2.resetTime(gui)
                        GUI2.resetTime2(gui)

            elif '[3' in l[0]:
#                     print("batterij moet worden opgeladen")
                    if '1' in l[1]:
                        voltageAmount = float(l[2].replace(']',''))
                        Charge.Charge1(gui, voltageAmount)
                        #functie charge
#                         print("batterij moet worden opgeladen met: ",voltageAmount)
                    elif '2' in l[1]:
                        Charge.Charge1_stop(gui)
                        #functie charge
                    
                
        except OSError:  # Possibly client has left the chat.
#             print("stop the try")?
            break

def start(gui, Motor_thread, client, Charge, GUI2):
    thread = threading.Thread(target=receive, args=(client,gui,Motor_thread, Charge, GUI2))
    thread.daemon = True
    thread.start()
    #client.sendRequest("client", null)