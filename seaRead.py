import redis
import sys
import sqlite3
import json

try:
#conntet the database
    conn = sqlite3.connect('./searchInfo.db')
    cu = conn.cursor()
    r = redis.Redis("127.0.0.1")
except:
    print("connect database error")
    sys.exit()

#print("aaaa")


def read(cmd=""):
    try:
    #get the id in redis:
        if __name__=='__main__':
           cmd = sys.argv[1]
        print("aaaa")

        id=r.lrange(cmd,0,-1)
    except:
        print("usage:\npython3 seaRead.py [keywords]")
        sys.exit()
        #select the data

    try:
        #此处性能需要优化
        if __name__=='__main__':
        #print("aaaa")
            for i in id:
                data = cu.execute("""select * from info where id="""+str(int(i)))
                print(data.fetchall())#fetchone?
        #    return 1
        result = []
        for i in id:
            data = cu.execute("""select * from info where id="""+str(int(i)))
            result.append(data.fetchone())
        print(result)
        data = json.dumps(result[0][1])
        return data
    except:
        print("read data error!")

if __name__=='__main__':
    #print("aaaa")
    print(read())
