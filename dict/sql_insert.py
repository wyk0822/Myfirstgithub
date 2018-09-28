import pymysql
import re


f = open('dict.txt')

db = pymysql.connect(host="localhost",
                     user="root",
                     password="123456",
                     database="dict",
                     charset="utf8")

cursor = db.cursor()


# for line in f:
#     l = re.split(r'\s+',line)
#     word = l[0]
#     interpret = ' '.join(l[1:])
#     sql = "insert into words(word,interpret)values('%s','%s');"%(word,interpret)

#     try:
#         cursor.execute(sql)
#         db.commit()
#     except:
#         db.rollback()
# f.close()






while True:
    
    data =f.readline()
    if not data:
        break
    s = data.split(maxsplit=1)
    try:
        if len(s)<2:
            L=[s[0].strip()]
            sql_insert = "insert into words(word,interpret)values(%s);"
            cursor.execute(sql_insert,L)
            db.commit()
        else:
            L=[s[0],s[1].strip()]
            sql_insert = "insert into words(word,interpret)values(%s,%s);"
            cursor.execute(sql_insert,L)
            db.commit()
    except:
        db.rollback()

cursor.close()
db.close()
f.close()










