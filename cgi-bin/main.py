#!/usr/bin/env python
# -*- coding: utf-8 -*-
  
import cgi, os
print("""\
Content-type: text/html\n
<html>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,height=device-height,initial-scale=1.0, minimum-scale=1.0, maximum-scale=1.0, user-scalable=no"/>
<link href="./../css/main.css" rel="stylesheet" type="text/css"/>
<title>大麦二维传输</title>
</head>
<body>
    <div class='title'><div class='title_n'>欢迎使用大麦二维传输</div></div>
    <center><iframe style="margin:1%;border-style: solid;border-color: #ccc; border-width: 1px;" scrolling="auto" src="/cgi-bin/list.py" width="96%" height="70%"  frameborder="no" ></iframe></center>
    <div class='content'><form enctype="multipart/form-data" action="/cgi-bin/main.py" method="post">
        请选择要上传的文件: <br />
        <div class="left"><input type="file" name="filename" /></div>
        <div class="right"><input class="bt1" type="submit" value="上传"></div>
    </form></div>
""")

form = cgi.FieldStorage()
if form!="":
    item = form['filename']
    if item.filename:
        fn = os.path.basename(item.filename)
        f_path=open('config','r')
        path=f_path.read()
        f_path.close()
        path=os.path.dirname(path)+"/"
        open(path + fn, 'wb').write(item.file.read())
        msg = '文件：' + fn + ' 上传成功 !'
    else:
        msg = '没有文件被上传 '
    print("""<script>alert('提示: %s')</script>
        """ % (msg,))
     

print("""</body></html>""")

