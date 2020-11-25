from Motor_Moule import Motor
import Keyboard_Module as kp
#from CameraModule import piCam
import Joystick_Module as js
from time import sleep
#runCamera = False
motor= Motor(2, 3, 4, 22, 17, 27)
movement = 'joyStick'
def main():
    if movement == 'joyStick':
        jsVal = js.getJS()
        motor.move(-(jsVal['axis2']*0.5),-(jsVal['axis1']*0.5), 0.1)
    else:
        kp.init()
        if kp.getKey('UP'):
            motor.move(0.15,0,0.1)
        if kp.getKey('DOWN'):
            motor.move(-0.15,0,0.1)
        if kp.getKey('LEFT'):
            motor.move(0.075,-0.075,0.1)
        if kp.getKey('RIGHT'):
            motor.move(0.075,0.075,0.1)
    #piCam(True)
#    motor.move(0.6,0,2)
#    motor.stop(2)
#    motor.move(-0.5,0.2,2)
#    motor.stop(2)

if __name__ == '__main__':
    while True:
        main()
