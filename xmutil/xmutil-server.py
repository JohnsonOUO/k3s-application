# _*_ coding: utf-8 _*_
import socket
import subprocess
import struct
import json
phone = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #买手机
phone.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
phone.bind(('0.0.0.0',80)) #绑定手机卡
phone.listen(5) #阻塞的最大数
print('start runing.....')
while True: #链接循环
    coon,addr = phone.accept() # 等待接电话
    print(coon,addr)
    while True: #通信循环
        # 收发消息
        cmd = coon.recv(1024) #接收的最大数
        print('接收的是：%s'%cmd.decode('utf-8'))
        #处理过程
        res = subprocess.Popen(cmd.decode('utf-8'),shell = True,
                                          stdout=subprocess.PIPE, #标准输出
                                          stderr=subprocess.PIPE #标准错误
                                )
        stdout = res.stdout.read()
        stderr = res.stderr.read()
        # 制作报头
        header_dic = {
            'total_size': len(stdout)+len(stderr),  # 总共的大小
            'filename': None,
            'md5': None
        }
        header_json = json.dumps(header_dic) #字符串类型
        header_bytes = header_json.encode('utf-8')  #转成bytes类型(但是长度是可变的)
        #print(len(header_bytes))
        if(len(header_bytes)>48):
        #先发报头的长度
            #coon.send(struct.pack('i',len(header_bytes))) #发送固定长度的报头
        #再发报头
            #coon.send(header_bytes)
        #最后发命令的结果
            coon.send(stdout)
            coon.send(stderr)
            break
#            print("123")
        else:
            break
    coon.close()
phone.close()
