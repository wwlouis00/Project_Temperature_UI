import os

# os.system("scp pi@192.168.50.238:/home/pi/socket_cam/result/factory.csv ./data")
os.system("scp ./data/factory.csv pi@192.168.50.238:/home/pi/socket_cam/result/")