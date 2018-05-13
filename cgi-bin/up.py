#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import cgi
import os.path

def modify_path(path):
    newpath=os.path.abspath(os.path.dirname(path))
    with open('config','w') as add_file:
        add_file.write(newpath)
    print("""\
        Content-type: text/html\n
        <html>
        <head>
        <script>window.location.href='list.py';</script> 
        </head></html>""")

form = cgi.FieldStorage()
  
path = form.getvalue('path')
modify_path(path)
