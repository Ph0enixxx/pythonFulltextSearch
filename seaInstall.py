import sqlite3
import sys
import os

try:
  import jieba
except:
  os.system('pip3 install jieba')

try:
  import redis
except:
  os.system('pip3 install redis')

#create database
try:
    conn = sqlite3.connect('./searchInfo.db')
    cu = conn.cursor()
    cu.execute("""CREATE TABLE info(
   ID INTEGER PRIMARY KEY   AUTOINCREMENT,
   title           TEXT      NOT NULL,
   other            varchar(2000)       ,
   content        VARCHAR(20000)
);""")
    print("\nCreate database ....ok!\n")
except:
    print("Creat database error,maybe the database already exist or the dir can't written?\n")
    sys.exit()
try:
    r = redis.Redis("127.0.0.1")
    r.ping()
    print("Connect redis ....ok!\n")
except:
    print("connect redis error\n")
    sys.exit()
