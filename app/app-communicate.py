# _*_ coding: utf-8 _*_
import socket
import subprocess
from subprocess import Popen, PIPE, STDOUT
import struct
import json
import os

phone = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
phone.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
phone.bind(('0.0.0.0',31225)) 
phone.listen(5) 
print('start runing.....')
while True: 
    coon,addr = phone.accept() 
    print(coon,addr)
    while True: 
        
        cmd = coon.recv(1024) 
        cmd = cmd.decode('utf-8').split()
        print('接收的是：%s',cmd)
        
        #with Popen(cmd, stdout=PIPE,stdin=PIPE, stderr=STDOUT, bufsize=1, text=True) as p:
        p = subprocess.Popen(cmd,stdout=PIPE,stdin=PIPE, stderr=STDOUT, bufsize=1, text=True)
        for line in p.stdout:
            print(line.strip())
            coon.send(line.encode('utf-8'))
            if line.endswith('number:\n'):
                cmd1 = coon.recv(1024).decode('utf-8')
                print('before')
                p.stdin.write(cmd1+'\n')
                print('Yes')
        print('inside',p.poll(),p.pid)
        break
    print('outside',p.poll(),p.pid)
    coon.close()
phone.close()
