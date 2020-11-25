"""
- Mô-đun này lưu hình ảnh và tệp nhật ký.
- Hình ảnh được lưu trong một thư mục.
- Thư mục nên được tạo thủ công với tên "DataCollected"
- Tên của hình ảnh và góc lái được ghi lại
trong tệp nhật ký.
- Gọi hàm saveData để khởi động.
- Gọi hàm saveLog kết thúc.
- Nếu chạy độc lập, sẽ lưu mười hình ảnh dưới dạng demo.
"""
import pandas as pd
import os
import cv2
from datetime import datetime

global imgList, steeringList
countFolder = 0
count = 0
imgList = []
steeringList = []

# NHẬN PATH TRỰC TIẾP HIỆN TẠI
myDirectory = os.path.join(os.getcwd(), 'DataCollected')
# print(myDirectory)

# TẠO THƯ MỤC MỚI DỰA TRÊN ĐẾM THƯ MỤC TRƯỚC
while os.path.exists(os.path.join(myDirectory,f'IMG{str(countFolder)}')):
        countFolder += 1
newPath = myDirectory +"/IMG"+str(countFolder)
os.makedirs(newPath)

#  LƯU HÌNH ẢNH TRONG THƯ MỤC
def saveData(img,steering):
    global imgList, steeringList
    now = datetime.now()
    timestamp = str(datetime.timestamp(now)).replace('.', '')
    #print("timestamp =", timestamp)
    fileName = os.path.join(newPath,f'Image_{timestamp}.jpg')
    cv2.imwrite(fileName, img)
    imgList.append(fileName)
    steeringList.append(steering)

# SLƯU TẬP TIN ĐĂNG NHẬP KHI PHẦN KẾT THÚC
def saveLog():
    global imgList, steeringList
    rawData = {'Image': imgList,
                'Steering': steeringList}
    df = pd.DataFrame(rawData)
    df.to_csv(os.path.join(myDirectory,f'log_{str(countFolder)}.csv'), index=False, header=False)
    print('Log Saved')
    print('Total Images: ',len(imgList))

if __name__ == '__main__':
    cap = cv2.VideoCapture(1)
    i = 0 
    while True:
        _, img = cap.read()
        i = i+1
        if i % 5 ==0:        
          
          saveData(img, 0.5)
          #cv2.imwrite(newPath+'/{}.jpg'.format(i), img)
          cv2.waitKey(1)
          cv2.imshow("Image", img)
        else:
          continue
    saveLog()