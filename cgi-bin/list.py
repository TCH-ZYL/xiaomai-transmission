#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import cgi
import os.path

s_path=""
s_filename=""

def get_FileSize(filePath):
    fsize = os.path.getsize(filePath)
    fsize = fsize/float(1024*1024)
    return round(fsize,2)

def read_path():
    read_file=open('config','r')
    path=read_file.readline()
    return path
    read_file.close()

def split_name():
    path=read_path()
    global s_path
    s_path=os.path.dirname(path)
    global s_filename
    s_filename=os.path.basename(path)

def is_file(fn):
    if os.path.isfile(fn):
        print("""<div class='isfile'><div class='left'><a href='download.py?filename=%s'>%s</a></div><div class='right'>  %s Mb</div></div>
        """ % (fn,os.path.basename(fn),get_FileSize(fn)))
    else:
        print("""<div class='isdoc'><div class='left'><a href='cd.py?docname=%s'>%s</a></div><div class='right'> </div></div>
        """ % (fn,os.path.basename(fn)))


split_name()
filename=s_filename
dir_path=s_path
target_path = dir_path+str(filename)
print("""\
        Content-type: text/html\n
        <html>
        <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width,initial-scale=1.0, minimum-scale=1.0, maximum-scale=1.0, user-scalable=no"/>
        <link href="./../css/main.css" rel="stylesheet" type="text/css"/>
        <title>大麦二维传输</title>
        </head>
        <body>""")
print("""
     <div class='doc'><div class='left'>当前目录 %s </div><div class='right'> <button class='bt1' onclick="window.location.href='up.py?path=%s'" type="button">向上</button></div></div>
     <div class='content'>""" % (dir_path,dir_path+"/"))
fl=os.listdir(dir_path)
fl.sort()
for fn in fl:
    if not fn.startswith('.'):
        is_file(dir_path+"/"+fn)

print('</div></body> </html>')



