#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import cgi
import os.path

def modify_path(newpath):
    with open('config','w') as add_file:
        add_file.write(newpath)
    print("""\
        Content-type: text/html\n
        <html>
        <head>
        <script>window.location.href='list.py';</script> 
        </head></html>""")

form = cgi.FieldStorage()
  
depath = form.getvalue('docname')
modify_path(depath+"/")
