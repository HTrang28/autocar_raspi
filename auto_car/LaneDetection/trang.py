import serial                   #Khai bao thu vien Serial
from time import sleep          #Khai bao lenh sleep tu thu vien time

ser = serial.Serial('/dev/ttyACM0',9600)                #Mo cong Serial baudrat

try:
        while (True):
          ser.write(1)
          if (ser.in_waiting>0):                  #Neu co tin hieu tu Arduino
             data = ser.readline()           #Doc vao data
             print(data)
#          else:
#            print("oh no !!! ")
          
#        while (True):
#                if (ser.in_waiting>0):                  #Neu co tin hieu tu Arduino
#                        data = ser.readline()           #Doc vao data
#                        print(data)                     #In ra man hinh
#                else:                                   #Nguoc lai
#                        string=input('Chang thay gi ca\n')  #Xuat ra man hinh va doc string
#                        ser.write(string.encode())                  #Encode va xuat ra arduino
#                        sleep(0.5)                                  #Dung 0.5s
except KeyboardInterrupt:                                           #Nhan Ctrl+C
        print('\nDone')                                               #In ra Done
finally:
        ser.close()                                     #Cuoi cung dong cong Serial