#!/bin/python3


import sys #from system
import socket
from datetime import datetime

 #Dfine target
if len(sys.argv) == 2:
     target = socket.gethostbyname(sys.argv[1]) #translate a host name to ipv4
else:
     print("Invalid amont of arguments sir")
     print("syntax error: exmaple :: python3 portscanner.py <your target ip>")
     sys.exit()

#banner
print("*" * 70)
print("we had scanning your target:: "+target)
print("Time started at=>> "+str(datetime.now()))
print("*" * 70)
print("{Y}    ██╗  ██╗██╗██╗     ██╗     ███████╗██████╗      ██████╗  ██████╗ ███████╗ ")
print("{Y}    ██║ ██╔╝██║██║     ██║     ██╔════╝██╔══██╗    ██╔═████╗██╔═████╗╚════██║ ")
print("{Y}    █████╔╝ ██║██║     ██║     █████╗  ██████╔╝    ██║██╔██║██║██╔██║    ██╔╝")
print("{Y}    ██╔═██╗ ██║██║     ██║     ██╔══╝  ██╔══██╗    ████╔╝██║████╔╝██║   ██╔╝")
print("{Y}    ██║  ██╗██║███████╗███████╗███████╗██║  ██║    ╚██████╔╝╚██████╔╝   ██║ ")
try:
      for port in range (1,1025):
          s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
          socket.setdefaulttimeout(1) # is detect the port
          result = s.connect_ex((target,port))# returns error or not
          # if there is no error is turn  0
          print("Checking port {}".format(port))
          if result == 0:
              print("Port {} is open".format(port))

              s.close()
        
except KeyboardInterrupt:
    print("\nGood bye Sir.")
    sys.exit()

except socket.gaierror:
       print("Sorry sir ,we cannot connect.Hostname could not be solved.")
       sys.exit()

except socket.error:
       print("Server is down. we can connect it")
       sys.exit()
