import pymysql

# 连接数据库
conn = pymysql.connect(host='127.0.0.1',port=3306,database='jing_dong1',user='root',password='mysql',charset='utf8')

# 获取cursor对象，游标对象
cs = conn.cursor()

# 所谓的sql注入，用户输入一些恶意的sql语句，mysql服务器并不知道这个语句是否有恶意
# 让这个sql语句正常执行，如果这个恶意语句是查询所有信息，给它返回所有信息

name = input("请输入需要查询的name: ")
# 字符串拼接
# sql = 'select * from goods where name="%s"'%(name)
# print("sql = ", sql)

# 指向sql语句
# 里面的语句加不加分号一样
# 返回值受影响的记录个数（行数）
# 参数化, 可以防止sql注入
# count = cs.execute("select %s, %s from goods where name=%s", ["id", "price", name])
count = cs.execute("select id, price from goods where name=%s", [name])
# 字符串拼接，很容易sql注入
# count = cs.execute('select * from goods where name="%s"'%name)

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
