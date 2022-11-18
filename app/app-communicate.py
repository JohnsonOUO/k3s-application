# _*_ coding: utf-8 _*_
import socket
import subprocess
from subprocess import Popen, PIPE, STDOUT
import struct
import json
import os

phone = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #买手机
phone.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
phone.bind(('0.0.0.0',31225)) #绑定手机卡
phone.listen(5) #阻塞的最大数
print('start runing.....')
while True: #链接循环
    coon,addr = phone.accept() # 等待接电话
    print(coon,addr)
    while True: #通信循环
        # 收发消息
        cmd = coon.recv(1024) #接收的最大数
        cmd = cmd.decode('utf-8').split()
        print('接收的是：%s',cmd)
        #处理过程
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
