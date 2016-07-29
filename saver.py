# coding=utf-8
import MySQLdb as mysql
con = mysql.connect(user='fable',\
                    passwd='fableAdmin',\
                    db='Fable_log',\
                    host='localhost')
con.autocommit(True)
cur = con.cursor()
# 处理文件省略
for s in res_list:
    sql = 'insert log values ("%s","%s",%s,%s)' % s
    try:
        # 入库
        cur.execute(sql)
    except Exception, e:
        pass
