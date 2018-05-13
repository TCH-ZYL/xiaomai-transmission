#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from http.server import BaseHTTPRequestHandler, HTTPServer, CGIHTTPRequestHandler
import socket
#import qrcode_terminal
import qrcode
import webbrowser
import os

path=""
def get_host_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip
    
def add_path(fullpath):
    global path
    with open('config','w') as add_file:
        path=fullpath
        add_file.write(path)
        
def creatQR(path):
    img = qrcode.make(path)
    img.save("qr.png")
    
def welcome():
    print('欢迎使用大麦二维传输!')
    print('=='*16)
    print('请选择工作模式：')
    print('开启指定文件下载模式，请按 1')
    print('开启自由浏览上传模式，请按 2')
    print('退出请按 0')
    mod_choice=str(input("请选择："))
    if mod_choice=="1":
        print("请在下面输入完整文件路径")
        fullpath=str(input(""))
        if os.path.isfile(fullpath):
            add_path(fullpath)
            qr_url="http://"+ip+":8080/cgi-bin/download.py?filename="+path
            creatQR(qr_url)
        else:
            print("您输入的文件不存在！")
            welcome()
    elif mod_choice=="2":
        print("请输入需要浏览的目录")
        fullpath=str(input(""))
        add_path(fullpath)
        qr_url="http://"+ip+":8080/cgi-bin/main.py"
        creatQR(qr_url)
    elif mod_choice=='0':
        exit()
    else:
        print("您的选择有误！")
        welcome()
        
if __name__ == '__main__':
    try:
        handler = CGIHTTPRequestHandler
        handler.cgi_directories = ['/cgi-bin', '/htbin']
        port = 8080
        print('port is %d'% port)
        server = HTTPServer(('', port), handler)
        ip=get_host_ip()
        welcome()
        webbrowser.open("index.html", new=0, autoraise=True)
        print("服务已启动，如需退出，请按^C！")
        server.serve_forever()

        
  
    except KeyboardInterrupt:
        print ('^C received, shutting down server')
        server.socket.close()
