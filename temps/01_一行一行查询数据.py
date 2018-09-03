import pymysql

# 连接数据库
conn = pymysql.connect(host='127.0.0.1', port=3306, database='jing_dong', user='root',password='mysql', charset='utf8')

# 获取cursor对象，游标对象
cs = conn.cursor()

# 指向sql语句
# 里面的语句加不加分号一样
# 返回值受影响的记录个数（行数）
count = cs.execute("select * from goods")

# 打印结果
print("count = ", count)

# cs.fetchone() 只取一行的结果，再取就是下一行
for i in range(count):
    # 返回值为元素，就是一行记录的信息
    result = cs.fetchone()
    print("result = ", result)


# 关闭，先关cursor，再关连接
cs.close()
conn.close()
