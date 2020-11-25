import cv2

def piCam(runCamera):
    if runCamera == True:
        frameWidth = 640
        frameHeight = 480
        cap = cv2.VideoCapture(0)
        cap.set(3, frameWidth)
        cap.set(4, frameHeight)
        while True:
            success, img = cap.read()
            cv2.imshow("Result", img)
            if cv2.waitKey(1) and 0xFF == ord('q'):
                break
if __name__ == '__main__':
    piCam(True)