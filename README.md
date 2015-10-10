#PySearch
##Written by Radish. 2015.10


###1.Introduction
**PySearch** is a fulltext search engine written by Python.


###2.Quick Start
**Please install Redis、Python3、pip3 first**

When you first use PySearch, after unpack the packge,use this command:
	
	./python3 seaInstall.py

Then the install code will automatically install.

Type ```python3 seaWrite.py 标题 文本鬼吹灯 http://baidu.com```
to add data.

Then type ```python3 seaRead.py 文本``` can search it!

###3.How to use?
This code include two main models :
####1.Write model
	seaWrite.py 

	usage:
	python3 seaWrite.py [title] [content] [other]
	
####2.Read model
	seaRead.py 
	
	usage:
	python3 seaRead.py [keywords]
	
###更新日志
2015.10.10 添加对输入长度的限制，并将write部分的代码重写成函数

2015.10.10 添加flask测试