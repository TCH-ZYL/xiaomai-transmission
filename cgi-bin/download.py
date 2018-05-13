#!/usr/bin/env python
# -*- coding: utf-8 -*-
  
import os
import sys
import cgi
  
form = cgi.FieldStorage()
  
targetname = form.getvalue('filename')
if os.path.isfile(targetname):
    filename=os.path.basename(targetname)
    print ('Content-Type: application/octet-stream')
    print ('Content-Disposition: attachment; filename = "%s"' % filename)
    print()  
    sys.stdout.flush()
    fo = open(targetname, "rb")
    sys.stdout.buffer.write(fo.read())
    fo.close()
else:
    print("""\
        Content-type: text/html\n
        <html>
        <head>
        <script>window.location.href='list.py';</script> 
        </head></html>""")

