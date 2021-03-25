#=======ExpanderPi stuff
from ExpanderPi import ADC
from ExpanderPi import DAC

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
            ydata.append((adc.read_adc_voltage(1,0)-1.25)/0.005)
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