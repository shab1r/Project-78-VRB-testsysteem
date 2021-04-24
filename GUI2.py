from lib import *
from client import Client
Client = Client()
# kit = MotorKit()
mp = []
# adc = ADC()
# dac = DAC(2)
# plt.ion()
min_y = 0
max_y = 40

min2_y = -4
max2_y = 4


class GUI2(Frame):    
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.grid()
        self.widgets()
        self.running = False
        self.running2 = False
        self.running3 = False
        self.running4 = False
        self.addedUp = False
        self.pauseOdd = 0
        self.sumPausedTimes= 0.0
        self.startingTime = 0.0
        self.timePause = 0.0
        self.resumeTime = 0.0
        self.paused = False
        self.timer = [0,0,0]
        self.timer2 = [0,0,0]
        self.timeString = str(self.timer[0]) + ':'+ str(self.timer[1]) + ':' + str(self.timer[2])
        self.timeString2 = str(self.timer2[0]) + ':'+ str(self.timer2[1]) + ':' + str(self.timer2[2])
        self.update_time()
        self.update_time2()
        self.start_datalogging()
        self.master = master
        self.Temp = [0]
        self.Temperature()
        self.tempString = str(T)
        self.Battery_1()
        self.Battery_1()
        self.StartTime()
        self.returnEntry()
        self.TimeSet()
        self.StartSignal()
        self.SignalSet()
        running6 = False
        ST = self.StartTime()
         
    def widgets(self):
        
        global Power1
        Power1 = None
        Power1 = tk.DoubleVar()
        

        global Power2       
        Power2 = None
        Power2 = tk.DoubleVar()
        
        global Ch
        Ch = tk.DoubleVar()
        
        global SignalS
        SignalS = tk.DoubleVar()
        
        global ChromS
        ChromS = tk.DoubleVar()
        
        global T
        T = tk.DoubleVar()
        
        global Start
        Start = None
        Start = tk.DoubleVar()
        
        global TimeS
        TimeS = tk.DoubleVar()
        
        global Bat1
        Bat1 = tk.DoubleVar()
        
        global Bat2
        Bat2 = tk.DoubleVar()
        
        ##### power control motor 1 #####
        
        self.powerFrame1 = tk.LabelFrame(root, text='Power Control Motor 1')
        self.powerFrame1.grid(row=1, column=0, columnspan = 3, rowspan = 3, padx=5, pady=5)
        
        self.label_power1 = tk.Label(self.powerFrame1, text="Fractional power")
        self.label_power1.grid(row=1, column=0, padx=5, pady=5)
        
        self.Powerentry = tk.Entry(self.powerFrame1, width=7, textvariable=Power1)     
        self.Powerentry.grid(row=1, column=1, padx=5, pady=5)
        
        self.enterEntry1 = tk.Entry(self.powerFrame1, width=7, textvariable= "")
        self.enterEntry1.grid(row=1, column=2, padx=5, pady=5)
        
        self.StartMotor1Button = tk.Button(self.powerFrame1, text="Start motor 1", command=lambda:[Motor_Thread.Run_Motor1(self), self.returnEntry(arg=None)]).grid(column=2,row=2, padx=5, pady=5)
        self.StopMotor1Button = tk.Button(self.powerFrame1, text="Stop Motor1", command=lambda:Motor_Thread.turnOffMotor1(self)).grid(row=3,column=2, padx=5, pady=5)
        
        self.enterEntry1.insert(0, "")
        self.Powerentry.insert(0, "")
        
        ##### widget for counter motor 1#####
        
        self.label_power1 = tk.Label(self.powerFrame1, text="Timer")
        self.label_power1.grid(row=2, column=0, padx=5, pady=5)
        self.show = tk.Label(self.powerFrame1, width=7, text='00:00:00', background="black", foreground="yellow", font=('Helvetica',20))
        self.show.grid(row=3, column=0, padx=5, pady=5)
        
#         self.Startstopwatch = tk.Button(self.powerFrame1, text="Start", command=self.start).grid(column=1,row=3, padx=5, pady=5)
        self.Startstopwatch = tk.Button(self.powerFrame1, text="Reset", command=self.resetTime).grid(column=2,row=4, padx=5, pady=5)
        
        ##### power control motor 2 #####

        self.powerFrame2 = tk.LabelFrame(root, text='Power Control Motor 2')
        self.powerFrame2.grid(row=4, column=0, columnspan = 3, rowspan = 2, padx=5, pady=5)

        self.label_power2 = tk.Label(self.powerFrame2, text="Fractional power")
        self.label_power2.grid(row=4, column=0, padx=5, pady=5)
        
        self.Powerentry2 = tk.Entry(self.powerFrame2, width=7, textvariable=Power2)
        self.Powerentry2.grid(row=4, column=1, padx=5, pady=5)
        
        self.enterEntry2 = tk.Entry(self.powerFrame2, width=7, textvariable= "")
        self.enterEntry2.grid(row=4, column=2, padx=5, pady=5)
        
        self.StartMotor2Button = tk.Button(self.powerFrame2, text="Start Motor 2", command=lambda:[Motor_Thread.Run_Motor2(self), self.returnEntry2(arg=None)]).grid(column=2,row=5, padx=5, pady=5)
        self.StopMotor2Button = tk.Button(self.powerFrame2, text="Stop Motor 2", command=lambda:Motor_Thread.turnOffMotor2(self)).grid(row=6,column=2, padx=5, pady=5)
        
        self.enterEntry2.insert(0, "")
        self.Powerentry2.insert(0, "")
        
        ##### widget for counter motor 2 #####
        
        self.label_power2 = tk.Label(self.powerFrame2, text="Timer")
        self.label_power2.grid(row=5, column=0, padx=5, pady=5)     
        self.show2 = tk.Label(self.powerFrame2, width=7, text='00:00:00', background="black", foreground="yellow", font=('Helvetica',20))
        self.show2.grid(row=6, column=0, padx=5, pady=5)
        
#         self.Startstopwatch2 = tk.Button(self.powerFrame2, text="Start", command=self.start2).grid(column=1,row=6, padx=5, pady=5)
        self.Startstopwatch2 = tk.Button(self.powerFrame2, text="Reset", command=self.resetTime2).grid(column=2,row=7, padx=5, pady=5)
        
        ##### start/stop both motors #####
        
        self.buttonFrame1 = tk.LabelFrame(root, text='Both motor control')
        self.buttonFrame1.grid(row=6, column=0, columnspan = 2, padx=5, pady=5)
        
        self.Start_both_MotorsButton = tk.Button(self.buttonFrame1, width=15, text="Start Both Motors", command=lambda:[Motor_Thread.Run_BothMotors(self), Graph.returnEntry(self, arg=None), self.returnEntry(arg=None),self.returnEntry2(arg=None)]).grid(column=0,row=6, padx=5, pady=5)
        self.Stop_both_MotorsButton = tk.Button(self.buttonFrame1, width=15, text="Stop Both Motors", command=lambda:Motor_Thread.turnBothMotorsOff(self)).grid(row=6,column=1, padx=5, pady=5)
        
        ##### save directory file #####
        
        self.name = tk.StringVar()
        self.save_directoryFrame = tk.LabelFrame(root, text='Log File Directory')
        self.save_directoryFrame.grid(row=4, column=3, columnspan = 2, padx=5, pady=5)
        self.dir_box = tk.Entry(self.save_directoryFrame, width=10, textvariable=self.name).grid(row=4,column=4, padx=5, pady=5)
        self.Directory_button = tk.Button(self.save_directoryFrame, text="Save as", command=self.callback).grid(row=4,column=3, padx=5, pady=5)
    
        ##### Temp Label #####
        
        self.tempFrame = tk.LabelFrame(root, text='Outside Temperature', width=100)
        self.tempFrame.grid(row=1, column=3, columnspan = 2, padx=5, pady=5)

        self.TemperatureLabel = tk.Label(self.tempFrame, text='0', fg="black", bg="white", width=20)
        self.TemperatureLabel.grid(column=1,row=1, padx=5, pady=5)
        
        ##### Battery 1 voltage ######
        
        self.Bat1Frame = tk.LabelFrame(root, text='Battery 1 voltage', width=100)
        self.Bat1Frame.grid(row=2, column=3, columnspan = 2, padx=5, pady=5)
        self.Battery1Label = tk.Label(self.Bat1Frame, text='0', fg="yellow", bg="black", width=20)
        self.Battery1Label.grid(column=3,row=2, padx=5, pady=5)
        
                ##### Battery charge voltage ######
        
        self.Bat2Frame = tk.LabelFrame(root, text='Battery 2 voltage', width=100)
        self.Bat2Frame.grid(row=3, column=3, columnspan = 2, padx=5, pady=5)

        self.Battery2Label = tk.Label(self.Bat2Frame, text='0', fg="yellow", bg="black", width=20)
        self.Battery2Label.grid(column=3,row=3, padx=5, pady=5)
        
        ##### Battery charge control #####

        self.chargeFrame = tk.LabelFrame(root,  text='Battery charge voltage')
        self.chargeFrame.grid(row=1, column=5, columnspan = 2, rowspan = 4, padx=5, pady=5)
        
        self.Chargeentry = tk.Entry(self.chargeFrame, width=20, textvariable=Ch)
        self.Chargeentry.grid(row=2, column=5, columnspan = 2, padx=5, pady=5)
        
        self.StartCharge = tk.Button(self.chargeFrame, text="Start", command=lambda:Charge.Charge1()).grid(column=5,row=3, padx=5, pady=5)
        self.Stopcharge = tk.Button(self.chargeFrame, text="Stop", command=lambda:Charge.Charge1_stop(self)).grid(row=3,column=6, padx=5, pady=5)
        
        self.Chargeentry.insert(0, "")
        
        ##### Start Measurement Button #####
            
        self.Start_Measurement = tk.Button(self.chargeFrame, bg="green2", width=15, text="Start Measurement", command=lambda:[self.StartTime(), Motor_Thread.Run_BothMotors(self), DynamicUpdate_Bat1.__callBat1__(self), self.returnEntry(arg=None), self.returnEntry2(arg=None),self.returnEntry3(arg=None), Charge.Charge1(self)]).grid(column=5, row=4, columnspan=2, padx=5, pady=5)
        self.Stop_Measurement = tk.Button(self.chargeFrame, bg="red", width =15, text="Stop Measurement", command=lambda:[self.pause3(), Motor_Thread.turnBothMotorsOff(self), Charge.Charge1_stop(self)]).grid(row=5,column=5, columnspan=2, padx=5, pady=5)
        self.Show_Graph = tk.Button(self.chargeFrame, bg="gold", width=15, text="Plot Temperature", command=lambda:DynamicUpdate.__call__(self)).grid(column=5,row=6, columnspan=2, padx=5, pady=5)
        self.Show_Chromatogram = tk.Button(self.chargeFrame, bg="orchid1", width=15, text="Plot Chromatogram", command=lambda:[self.StartTime(), DynamicUpdate_Bat1.__callBat1__(self)]).grid(column=5,row=7, columnspan=2, padx=5, pady=5)

        ##### Start chromatogram injection
        self.chargeFrame = tk.LabelFrame(root,  text='Chromatography start')
        self.chargeFrame.grid(row=5, column=5, columnspan = 2, rowspan = 2, padx=5, pady=5)
        self.Start_Measurement = tk.Button(self.chargeFrame, bg="green2", width=15, text="Start Chromatogram", command=lambda:[RemoteProg2.Remote()]).grid(column=5, row=6, columnspan=2, padx=5, pady=5)


### Performance time entry ###
        
        self.enterEntry3 = tk.Entry(self.chargeFrame, width=7, textvariable= "")
        self.enterEntry3.grid(row=7, column=5, columnspan=2, padx=5, pady=5)

        self.enterEntry1.insert(0, "")
        self.enterEntry2.insert(0, "")
        self.enterEntry3.insert(0, "")
    
    def update_time(self):
        
        if (self.running == True):
            
            self.pausedTime = self.resumeTime - self.timePause
            
            if(self.addedUp == False):
                self.sumPausedTimes += round(self.pausedTime, 2)
                self.addedUp = True
            
            if self.pauseOdd % 2 == 0:
                if self.pauseOdd == 0:
                    stopwatch = time.time() - self.startingTime
                else:
                    stopwatch = time.time() - self.startingTime - self.sumPausedTimes                
            seconds = stopwatch
            seconds = round(seconds, 2)
            self.timer[1] = seconds
            milsString = str(seconds).split('.')[1]
            
            
            if((seconds / 60) >= 1):
                self.startingTime = time.time()
                self.timer[0] += 1
                self.sumPausedTimes = 0
            
            if(len(milsString) == 1):
                milsString = milsString + '0'
            
            if(seconds <= 10):
                secondsString = '0' +  str(seconds).split('.')[0]
            else:
                secondsString = str(seconds).split('.')[0]
            
            seconds = str(seconds).split('.')[0]
            
            if(self.timer[0] <= 9):
                minutesString = '0' + str(self.timer[0])
            else:
                minutesString = str(self.timer[0])
           
            self.timeString = minutesString + ':' + secondsString + ':' + milsString
            self.show.config(text=self.timeString)
        root.after(1, self.update_time)
        
    def start(self):
        if  1.0 >= Power1.get() > 0.0 :
            self.running = True
            if self.pauseOdd % 2 == 0:
                self.startingTime = time.time()
            if self.pauseOdd % 2 != 0:
                self.resumeTime = time.time()
                self.pauseOdd += 1
                self.paused = False
            Client.sendRequest("[1,1,1,"+str(Power1.get())+"]")
        else:
            messagebox.showerror("Invalide invoer", "Voer een getal boven de 0.0 en een getal met een maximale waarde van 1.0 (Motor 1)")
    
    def pause(self):
        self.running = False
        if self.paused == False:
            self.pauseOdd += 1
            self.timePause = time.time()
            self.paused = True
            self.addedUp = False
        
    
    def resetTime(self):
        self.running = False
        self.timer = [0,0,0]
        self.show.config(text='00:00:00')
        self.pauseOdd = 0
        self.paused = False
        self.sumPausedTimes = 0.0
        
    def update_time2(self):
          
        if (self.running2 == True):
            
            self.timer2[2] += 1
            
            if(self.timer2[2] >=100):
                self.timer2[2] = 0
                self.timer2[1] += 1
            
            if(self.timer2[1] >= 60):
                self.timer2[0] += 1
                self.timer2[1] = 0
            
            self.timeString2 = str(self.timer2[0]) + ':' + str(self.timer2[1]) + ':'+ str(self.timer2[2])
            self.show2.config(text=self.timeString2)
        root.after(10, self.update_time2)
        
    def start2(self):
        if  1.0 >= Power2.get() > 0.0 :
            self.running2 = True
        else:
            messagebox.showerror("Invalide invoer", "Voer een getal boven de 0.0 en een getal met een maximale waarde van 1.0 (Motor 2)")
    
    def pause2(self):
        self.running2 = False
    
    def resetTime2(self):
        self.running2 = False
        self.timer2 = [0,0,0]
        self.show2.config(text='00:00:00')
    
    def callback(self):
        filename = tk.filedialog.askdirectory()
        self.name.set(filename)
    
    def start_datalogging(self):
            
        if (self.running3 == True):
            
            headers = ['time (sec)', 'Power Motor 1', 'Power Motor 2', 'Temperature', 'V Battery 1']
            
            filename = self.name.get()       
                      
            full_rows = [TimeS, self.enterEntry1.get(),self.enterEntry2.get(),T,Bat1,Bat2]
            
            if not os.path.exists(filename):
                print("creating new file")
                with open(filename, 'w') as csvfile:
                    csvwriter = csv.writer(csvfile, delimiter=',')
                    csvwriter.writerow(headers)
            if os.path.exists(filename):
                print("updating existing file")
                with open(filename + str(1), 'w') as csvfile:
                    csvwriter = csv.writer(csvfile, delimiter=',')
                    csvwriter.writerow(headers)    
            with open(filename, "a", newline='') as csvfile:
                csvwriter = csv.writer(csvfile, delimiter=',')
                csvwriter = csvwriter.writerow(full_rows)
                csvfile.flush()
        root.after(1000, self.start_datalogging)
    
    def start3(self):
        self.running3 = True
        
    def pause3(self):
        self.running3 = False
    
    def returnEntry(self, arg=None):
        
        self.enterEntry1.delete(0, END)
        self.enterEntry1.insert(0, Power1.get())
        
    def returnEntry2(self, arg=None):
        
        self.enterEntry2.delete(0, END)
        self.enterEntry2.insert(0, Power2.get())
        
    def returnEntry3(self, arg=None):
        
        self.enterEntry3.delete(0, END)
        self.enterEntry3.insert(0, time.perf_counter())
        
    def start4(self):
        self.running4 = True
        
    def StartSignal(self):
    
        global Signal
        
        # Signal = adc.read_adc_voltage(8,0)
    
    def SignalSet(self):
        
        global ChromS
        
        # ChromS = (adc.read_adc_voltage(8,0) - Signal)
        
        root.after(100, self.SignalSet)
    
    def StartTime(self):
                          
        global Start
            
        Start = timer()
        
        print ('Hey! Time is started!')

    def TimeSet(self):
        
        global TimeS
                                       
        TimeS = (timer() - Start)
        
        root.after(100, self.TimeSet)
    
    def pause4(self):
        self.running4 = False
    
    def Temperature(self):
        
        global T
        
        # T = (adc.read_adc_voltage(1,0)-1.25)/0.005
        
        self.tempString = str(round(T, 2))
        self.TemperatureLabel.config(text=self.tempString)
                
        root.after(1000, self.Temperature)
    
    def Battery_1(self):
        
        global Bat1
        
        # Bat1 = adc.read_adc_voltage(8,0)
        
        self.Bat1String = Bat1
        self.Battery1Label.config(text=self.Bat1String)
                
        root.after(1000, self.Battery_1)
        
    def Battery_2(self):
          
        # Bat2 = adc.read_adc_voltage(3,0)
        
        self.Bat2String = str(round(Bat2, 2))
        self.Battery2Label.config(text=self.Bat2String)
        
        root.after(1000, self.Battery_2)

class Motor_Thread():
    def __init2__(self, Power1, Time1, Power2, Time2):
        self.Run_Motor1()
        self.Power1 = Power1
        self.Power2 = Power2
        self.Time1 = Time1
        self.Time2 = Time2
        
     
    def Run_Motor1(self):
        # kit.motor1.throttle = Power1.get()
        GUI2.start(self)

    def Run_Motor2(self):
        # kit.motor2.throttle = Power2.get()
        GUI2.start2(self)
    
    def Run_BothMotors(self):
        # kit.motor1.throttle = Power1.get()
        # kit.motor2.throttle = Power2.get()
        GUI2.start(self)
        GUI2.start2(self)
        GUI2.start3(self)
    
    def turnOffMotor1(self):
        # kit.motor1.throttle = 0.0
        GUI2.pause(self)
        GUI2.pause3(self)
    
    def turnOffMotor2(self):
        # kit.motor2.throttle = 0.0
        GUI2.pause2(self)
        
    def turnBothMotorsOff(self):
        # kit.motor1.throttle = 0.0
        # kit.motor2.throttle = 0.0
        GUI2.pause(self)
        GUI2.pause3(self)
        GUI2.pause2(self)
        
class Charge():
    def __init3__(self, Ch):
        self.Charge1()
        self.Charge1_stop()
        self.running6 = False
        self.Start6()
        
    def Charge1():
        period=0
        running6 = True        
        if (running6 == True):
            while True:
                period+=1
                # dac.set_dac_voltage(2, Ch.get())
                print ("This While True works")
                if period>100:
                    period=0
                    break
        
    def Charge1_stop(self):    
        period=0
        self.running6 = True        
        if (self.running6 == True):
            while True:
                period+=1
                # dac.set_dac_voltage(2, 0.0)
                print ("This While True works")
                if period>100:
                    period=0
                    break
        

class DynamicUpdate():
    
    def on_launch(self):
        #Set up plot
        self.figure, self.ax = plt.subplots()
        self.lines, = self.ax.plot([],[], 'o')
        self.ax.set_ylabel('Temperature (°C)')
        self.ax.set_xlabel('Time (sec)')
        #Autoscale on unknown axis and known lims on the other
        self.ax.set_autoscaley_on(True)
               
        self.ax.set_ylim(min_y, max_y)
        #Other stuff
        self.ax.grid()
        ...

    def on_running(self, xdata, ydata):
        #Update data (with the new _and_ the old points)
        self.lines.set_xdata(xdata)
        self.lines.set_ydata(ydata)
        #Need both of these in order to rescale
        self.ax.relim()
        self.ax.autoscale_view()
        #We need to draw *and* flush
        self.figure.canvas.draw()
        self.figure.canvas.flush_events()
    
    #Example
    def __call__(self):
        
        DynamicUpdate.on_launch(self)
        xdata = []
        ydata = []
        for x in np.arange(0,3600,0.5):
            xdata.append(time.time())
            # ydata.append((adc.read_adc_voltage(1,0)-1.25)/0.005)
            DynamicUpdate.on_running(self, xdata, ydata)
            plt.pause(5)
        return xdata, ydata

class DynamicUpdate_Bat1():
    
    def on_launch_Bat1(self):
        #Set up plot
        self.figure, self.ax = plt.subplots(num="Chromatogram 1")
        self.lines, = self.ax.plot([],[])
        
        
        self.ax.set_ylabel('Voltage (V)')
        self.ax.set_xlabel('Time (sec)')
        #Autoscale on unknown axis and known lims on the other
        self.ax.set_autoscaley_on(True)
               
        self.ax.set_ylim(min2_y, max2_y)
        #Other stuff
        self.ax.grid()
        ...

    def on_running_Bat1(self, xdata, ydata):
        #Update data (with the new _and_ the old points)
        self.lines.set_xdata(xdata)
        self.lines.set_ydata(ydata)
        #Need both of these in order to rescale
        self.ax.relim()
        self.ax.autoscale_view()
        #We need to draw *and* flush
        self.figure.canvas.draw()
        self.figure.canvas.flush_events()
    
    #Example
    def __callBat1__(self):
        
        DynamicUpdate_Bat1.on_launch_Bat1(self)
        xdata = []
        ydata = []
        for x in np.arange(0,3600,0.5):
            xdata.append(TimeS)
            ydata.append(ChromS)
            DynamicUpdate_Bat1.on_running_Bat1(self, xdata, ydata)
            plt.pause(0.5)
        return xdata, ydata

root = tk.Tk()
up = GUI2(root)
root.title('Chromatography software')


root.mainloop()