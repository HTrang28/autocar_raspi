import pygame
#from Motor_Moule import Motor

#motor = Motor(2, 3, 4, 22, 17, 27)

def init():
    pygame.init()
    win = pygame.display.set_mode((100,100))

def getKey(keyName):
    ans = False
    for eve in pygame.event.get():pass
    keyInput = pygame.key.get_pressed()
    myKey = getattr(pygame,'K_{}'.format(keyName))
    if keyInput [myKey]:
        ans = True
    pygame.display.update()

    return ans

def main():
    if getKey('LEFT'):
        #motor.move(0, 0.5, 2)
        #motor.stop(1)
        print('Key Left was pressed')
    if getKey('RIGHT'):
        #motor.move(0.2,0.2,2)
        #motor.stop(1)
        print('Key Right was pressed')
    if getKey('UP'):
        #motor.move(0.2,0,2)
        #motor.stop(1)
        print('Key Up was pressed')
    if getKey('DOWN'):
        #motor.move(-0.2,0,2)
        #motor.stop(1)
        print('Key Down was pressed')

if __name__ == '__main__':
    init()
    while True:
        main()
