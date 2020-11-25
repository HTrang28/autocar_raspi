import cv2

cap = cv2.VideoCapture(0)

def getImg(display=False,size=[960, 480]):
    _, img = cap.read()
    cap.set(cv2.CAP_PROP_FPS,60)#test
    fps = int(cap.get(60)) #j
    img = cv2.resize(img, (size[0], size[1]))
    if display:
        cv2.imshow('IMG', img)
    return img

if __name__ == '__main__':
    i = 1
    while True:
        img = getImg(True)
        if i<200:
            i+=1
            cv2.imwrite('/home/pi/auto_car/LaneDetection/vid/vid'+str(i)+'.png', img)
            print(i)
        if cv2.waitKey(1) and 0xFF == ord('q'):
            break