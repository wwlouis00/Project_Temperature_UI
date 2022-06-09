import os
ip = str(input("Please input your IP address: "))
try:
    print("-" * 10 + "factory" + "-" * 10)
    os.system("scp factory.csv pi@" + ip + ":/home/pi/socket_cam/result")
    print("-" * 10 + "merged_image" + "-" * 10)
    os.system("scp merged_image.png pi@" + ip + ":/home/pi/socket_cam/para/ROIs")
except:
    print("連線失敗")