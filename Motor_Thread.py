from lib import *

class Motor_Thread():
    def __init2__(self, Power1, Time1, Power2, Time2):
        self.Run_Motor1()
        self.Power1 = Power1
        self.Power2 = Power2
        self.Time1 = Time1
        self.Time2 = Time2
        
     
    def Run_Motor1(self):
        # kit.motor1.throttle = Power1.get()
        GUI.start(self)

    def Run_Motor2(self):
        # kit.motor2.throttle = Power2.get()
        GUI.start2(self)
    
    def Run_BothMotors(self):
        # kit.motor1.throttle = Power1.get()
        # kit.motor2.throttle = Power2.get()
        GUI.start(self)
        GUI.start2(self)
        GUI.start3(self)
    
    def turnOffMotor1(self):
        # kit.motor1.throttle = 0.0
        GUI.pause(self)
        GUI.pause3(self)
    
    def turnOffMotor2(self):
        # kit.motor2.throttle = 0.0
        GUI.pause2(self)
        
    def turnBothMotorsOff(self):
        # kit.motor1.throttle = 0.0
        # kit.motor2.throttle = 0.0
        GUI.pause(self)
        GUI.pause3(self)
        GUI.pause2(self)