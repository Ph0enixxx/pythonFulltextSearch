import sqlite3
import jieba
import sys
import redis

try:
#create database
    conn = sqlite3.connect('./searchInfo.db')
    cu = conn.cursor()
except:
    print("connect database error.\n if you first run this software please run \"python3 seaInstall.py\" first")
    sys.exit()
    
#get the data
try:
    doc={'content':'','title':'','id':0,'other':''}
    #添加对flask web服务的支持
    if __name__ == '__main__':
        doc['title']=sys.argv[1]
        doc['content']=sys.argv[2]
        doc['other']=sys.argv[3]
except:
    print("*********************************************")
    print("*Search engine write model written by Radish*")
    print("*********************************************") 
    print("usage:\npython3 seaWrite.py [title] [content] [other]")
    sys.exit()

def add(doc={}):
    #check the input!
    if (len(doc['title'])>20000) or len(doc['content'])>20000 or len(doc['other'])>2000 :
        print("\nData is too long!\n title(max=20000) content(max=20000) other(max=2000)")



    try:
    #insert to the info database
        cu.execute("""INSERT INTO info (content,title,other)
        VALUES ('"""+doc['content']+"""','"""+doc['title']+"""','"""+doc['other']+"""');""")
        conn.commit()
        res = cu.execute("""select max(id) from info""")
        doc['id']= cu.fetchone()
        doc['id']=doc['id'][0]
    except:
        print("faild to insert data to the database")
        sys.exit()
        
    try:
    #connect redis: 
        r = redis.Redis("127.0.0.1")
        doc['tokens']=jieba.cut(doc['content']+doc['title'])
        for i in doc['tokens']:
            r.lpush(i,doc['id'])
            print(i)
        #
        print(doc['tokens'])
        print("\nInsert data ok!")
    except:
        #del before in sql
        print("\nerror when connecting or writing to the redis server or making token")
        cu.execute("DELETE FROM info where id="+str(doc['id']))
        conn.commit()

if __name__ == '__main__':
    add(doc)
