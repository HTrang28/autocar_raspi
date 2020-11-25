from MotorModule import Motor
from LaneModule import getLaneCurve
import WebcamModule
#import serial                   #Khai bao thu vien Serial
from time import sleep
#ser = serial.Serial('/dev/ttyACM0',9600,timeout=1)  
#import Joystick_Module as js
import cv2
##################################################
motor = Motor(2, 3, 4, 22, 17, 27)
##################################################

def main():
#    jsVal = js.getJS()
#    motor.move(-(jsVal['axis2']*0.3),-(jsVal['axis1']*0.3), 0.1)
    #try:
    #while(True):
        #int=input('What do you want to send? ')  #Xuat ra man hinh va doc string
        #int=int+"\r"                          #Cong them ki tu \r
    #    ser.write(1) 
    #except KeyboardInterrupt:
        #print('Done')                                               #In ra Done
    #finally:
        #ser.close()  
    img = WebcamModule.getImg()
    curveVal= getLaneCurve(img,1)
    print("curveVal1", curveVal)
    sen = 0.5  # SENSITIVITY
    maxVAl= 0.3 # MAX SPEED
    #if curveVal>maxVAl:curveVal = maxVAl
    #if curveVal<-maxVAl: curveVal =-maxVAl
    #print(curveVal)
    if curveVal>0:
        #sen =1.7
        if curveVal<0.05: curveVal=0
    else:
        if curveVal>-0.08: curveVal=0
    if abs(curveVal) > 0.2:
        sen = 0.3
  
    motor.move(0.20,-curveVal*sen,0.01)
    #cv2.waitKey(1)

if __name__ == '__main__':
    while True:
        main()