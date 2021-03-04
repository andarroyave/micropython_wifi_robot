from machine import Pin, PWM
import math

#You must define speed beetwen 0 and 100 like an int value ex: speed = 60

class Motor:
    

    def __init__(self,pinA,pinB,pinPWM, speed):
    
    #def __init__(self,pinA,pinB):
        
     
        self.dir1 = Pin(pinA, Pin.OUT)
        self.dir2 = Pin(pinB, Pin.OUT)
        self.pinPWM = PWM(Pin(pinPWM), freq=800, duty=(math.ceil(1023*speed/100)))

    def forward(self):
        self.dir1.off()
        self.dir2.on()
        
    def backward(self):
        self.dir2.off()
        self.dir1.on()
     
    def stop(self):
        self.dir1.off()
        self.dir2.off()
         
    def setSpeed(self, speed):
        self.pinPWM.duty(math.ceil(1023*speed/100))
         
    def getSpeed(self):
        return math.ceil(self.pinPWM.duty()*100/1023)