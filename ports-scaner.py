import socket
host = input('please enter you ip address: ')
try:
  for port in range(1,2000):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    result = s.connect_ex((host,port))
    if result == 0:
      print("the port {} is open.".format(port))
except:
  print('error')

