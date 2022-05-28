import os
os.system("scp ./data/factory.csv pi@192.168.1.108:/home/pi/socket_cam/result/")
#os.system("sshpass -p '123' scp ./data/factory.csv pi@192.168.50.238:/home/pi/socket_cam/result/")
# os.system("ssh pi@192.168.50.238")
# os.system("echo '123' | ssh pi@192.168.50.238")
# os.system("scp ./data/factory.csv pi@192.168.50.238:/home/pi/socket_cam/result/")