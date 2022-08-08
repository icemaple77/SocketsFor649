import socket
import tqdm
import os

#from bt.txt
import serial
import time
import string

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096 # send 4096 bytes each time step

# the ip address or hostname of the server, the receiver
host = "54.252.235.11"
# the port, let's use 5001
port = 5001
# the name of file we want to send, make sure it exists
# filename = "data.csv"
# get the file size
# filesize = os.path.getsize(filename)

# create the client socket
s = socket.socket()

print(f"[+] Connecting to {host}:{port}")
s.connect((host, port))
print("[+] Connected.")


ser = serial.Serial("/dev/rfcomm0", 9600)
ser.write(str.encode('Start\r\n'))

# send the filename and filesize
# s.send(f"{filename}{SEPARATOR}{filesize}".encode())

# start sending the file
# progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024)
# with open(filename, "rb") as f:
while True:
    if ser.in_waiting > 0:
        rawserial = ser.readline()
        cookedserial = rawserial.decode('utf-8').strip('\r\n')
        # print(cookedserial)
        s.send(f"{cookedserial}".encode())

    # read the bytes from the file
    # bytes_read = f.read(BUFFER_SIZE)
    # if not bytes_read:
        # file transmitting is done
        # break
    # we use sendall to assure transimission in 
    # busy networks
    # s.sendall(bytes_read)
    # update the progress bar
    # progress.update(len(bytes_read))
# close the socket
s.close()