import cv2
import numpy as np
import utils 
curveList = []
avgVal = 10

def getLaneCurve(img, display = 2):

    intialTrackBarVals = [40,80, 10, 235]
    utils.initializeTrackbars(intialTrackBarVals)

    imgCopy = img.copy()
    imgResult = img.copy()

    ### STEP 1: FIND LAND
    imgThres = utils.thresholding(img)

    ### STEP 2: Find WARPing LANE
    h, w, c = img.shape
    points = utils.valTrackbars()
    imgWarp = utils.warpImg(imgThres, points, w, h)
    imgWarpPoints = utils.drawPoints(imgCopy, points)

    ### STEP3: FIND CURVE
    middlePoint, imgHist = utils.getHistogram(imgWarp, display=True, minVal=0.6, region=4)
    curveAveragePoint, imgHist = utils.getHistogram(imgWarp, display=True, minVal=0.9)
    curveRaw = curveAveragePoint - middlePoint
    #print('cure', curveRaw)

    #### SETP 4
    curveList.append(curveRaw)
    if len(curveList)>avgVal:
        curveList.pop(0)
    curve = int(sum(curveList)/len(curveList))

    ### DisPlay

    if display != 0:
        imgInvWarp = utils.warpImg(imgWarp, points, w, h, inv=True)
        imgInvWarp = cv2.cvtColor(imgInvWarp, cv2.COLOR_GRAY2BGR)
        imgInvWarp[0:h // 3, 0:w] = 0, 0, 0
        imgLaneColor = np.zeros_like(img)
        imgLaneColor[:] = 0, 255, 0
        imgLaneColor = cv2.bitwise_and(imgInvWarp, imgLaneColor)
        imgResult = cv2.addWeighted(imgResult, 1, imgLaneColor, 1, 0)
        midY = 450
        cv2.putText(imgResult, str(curve), (w // 2 - 80, 85), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 0, 255), 3)
        cv2.line(imgResult, (w // 2, midY), (w // 2 + (curve * 3), midY), (255, 0, 255), 5)
        cv2.line(imgResult, ((w // 2 + (curve * 3)), midY - 25), (w // 2 + (curve * 3), midY + 25), (0, 255, 0), 5)
        for x in range(-30, 30):
            w = w // 20
            cv2.line(imgResult, (w * x + int(curve // 50), midY - 10),
                     (w * x + int(curve // 50), midY + 10), (0, 0, 255), 2)
        # fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer);
        # cv2.putText(imgResult, 'FPS ' + str(int(fps)), (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (230, 50, 50), 3);
    if display == 2:
        imgStacked = utils.stackImages(0.7, ([img, imgWarpPoints, imgWarp],
                                             [imgHist, imgLaneColor, imgResult]))
        cv2.imshow('ImageStack', imgStacked)
    elif display == 1:
        cv2.imshow('Resutlt', imgResult)

    #cv2.imshow('Thres', imgThres)
    #cv2.imshow('Warp', imgWarp)
    #cv2.imshow('WarpPoints', imgWarpPoints)
    #cv2.imshow('Histogram', imgHist)
    #### NORMALIZATION
    curve = curve / 100
    if curve > 1:
        curve = 1
    elif curve < -1:
        curve = -1
    return curve

if __name__ == '__main__':
    cap = cv2.VideoCapture(0)

    #intialTrackBarVals = [110,90, 20, 220]  
    #utils.initializeTrackbars(intialTrackBarVals)
    #frameCounter = 0
    while True:

        #frameCounter += 1
        #if cap.get(cv2.CAP_PROP_FRAME_COUNT) == frameCounter:
        #    cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        #    frameCounter = 0

        success, img = cap.read()
        img = cv2.resize(img, (480, 240))
        curve = getLaneCurve(img, display=2)
        print('curve', curve)
        
        #cv2.imshow('vid', img)
        cv2.waitKey(1)
