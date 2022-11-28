# _*_ coding: utf-8 _*_
import socket
import subprocess
import struct
import json
phone = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
phone.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
phone.bind(('0.0.0.0',80)) 
phone.listen(5) 
print('start runing.....')
while True: 
    coon,addr = phone.accept() 
    print(coon,addr)
    while True: 
        
        cmd = coon.recv(1024) 
        print('接收的是：%s'%cmd.decode('utf-8'))
        
        res = subprocess.Popen(cmd.decode('utf-8'),shell = True,
                                          stdout=subprocess.PIPE, 
                                          stderr=subprocess.PIPE 
                                )
        stdout = res.stdout.read()
        stderr = res.stderr.read()
        
        header_dic = {
            'total_size': len(stdout)+len(stderr),  
            'filename': None,
            'md5': None
        }
        header_json = json.dumps(header_dic)
        header_bytes = header_json.encode('utf-8')  
        #print(len(header_bytes))
        if(len(header_bytes)>48):

            coon.send(stdout)
            coon.send(stderr)
            break
        else:
            break
    coon.close()
phone.close()
