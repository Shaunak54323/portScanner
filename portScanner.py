#!/bin/python3

import sys
import socket
from datetime import datetime

# Define our target
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1]) # Translate hostname to IPv4
else:
    print('Invalid amount of arguments.')
    print('Syntax: python3 portScanner.py <ip>')
    sys.exit(0)


portCount = 0
# Add a pretty banner
print("-" * 50)
print("Scanning target " + target)
print("Time started: " + str(datetime.now()))
print("-" * 50)

try:
    for port in range(11300, 11500):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target , port)) # returns an error indicator
        if result == 0:
            print("Port {} is open".format(port))
            portCount += 1
        s.close()
except KeyboardInterrupt:
    print("\nExiting...")

except socket.gaierror:
    print('Hostname could not be resolved. Exiting...')
    sys.exit()

except socket.error:
    print("Couldn't connect to server")
    sys.exit()

if portCount == 0:
    print("No open ports found")

print("-" * 50)
print("Scanning completed: " + str(datetime.now()))
print("Total of " + str(portCount) + " open ports found")
print("-" * 50)