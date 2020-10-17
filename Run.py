import socket
host = '192.168.66.136'
port = 7777
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))
import os 
os.system("nc -lnvp 7777")
