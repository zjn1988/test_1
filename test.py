# encoding: utf-8

def getCode(strText,codec):
    b = bytes((ord(i) for i in strText))  
    return b.decode(codec)

import pymssql
SQLSERVER='172.22.131.85'
USER='zjn'
PASSWORD='zhangjiannan'
cn=pymssql.connect(SQLSERVER,USER,PASSWORD,charset='utf8')
cursor=cn.cursor()
sqlstr="SELECT TOP 4 *  FROM [Position_DB].[PFP].[M_Cash_Product_Relation]"
cursor.execute(sqlstr)
row = cursor.fetchone()
while row:
   print((row[0], getCode(row[1],'gb2312'),getCode(row[2],'gb2312')))
   row = cursor.fetchone()
#insertSql = "insert into WeiBo([UserId],[WeiBoContent],[PublishDate]) values(1,'测试','2012/2/1')".encode("utf8")
