import pymysql

# 连接数据库
conn = pymysql.connect(host='127.0.0.1',port=3306,database='jing_dong1',user='root',password='mysql',charset='utf8')

# 获取cursor对象，游标对象
cs = conn.cursor()


name = input("请输入需要查询的name: ")
sql = 'select * from goods where name="%s"'%(name)
print("sql = ", sql)

# 指向sql语句
# 里面的语句加不加分号一样
# 返回值受影响的记录个数（行数）
count = cs.execute(sql)

# 打印结果
print("count = ", count)

# 取完后，再取，返回(), 空
# cs.fetchone() 只取一行的结果，再取就是下一行
# cs.fetchmany(4) 每一次去4个
# cs.fetchall() 取所有
result = cs.fetchall()
print("result = ", result)




# 关闭，先关cursor，再关连接
cs.close()
conn.close()
