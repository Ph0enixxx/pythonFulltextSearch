#charset-utf8
import sqlite3
import jieba
import sys
import redis
from seaRead import *
#try:
#create database
"""conn = sqlite3.connect('./searchInfo.db')
cu = conn.cursor()
cu.execute('DELETE FROM info WHERE ID = 6;')
conn.commit()
#cu.execute("delete from info where id=(select min(id) from info)")
#r = cu.execute("DELETE FROM info where ID=5")#+str(5))
#print(r)
#except:
 #   pass
"""
print(read("µØ·½"))
