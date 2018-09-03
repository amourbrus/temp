from datetime import datetime
import time
"""
datetime 简单使用，，计算总生命天数
time  简单使用  计算星期几
"""

# dt = datetime(1998, 4, 23)     # 输出为年月日格式：1998-04-23 00:00:00
#
# t = dt.timestamp()         # 分割为秒   距离那个初始年  1967？？
#
# oldname = datetime.fromtimestamp(t)   # 秒的格式》》》》datetime format
#
# # print(oldname)
# today = datetime.now()        # 目前时间  2018-05-04 15:43:33.866544
#
# one = today - oldname    # >>   2018-1-3 - 2018-1-1  = 2   故第多少天，就加1;
# print(one)                   # 需要??  才可以直接计算 + 1, 否则类型fail, 这个只适用于同一年

# 计算两个日期相隔多少天， 相对时间， 都化为距离开始多少秒的格式
# dt = datetime(1994, 9, 3)  # 8645
dt = datetime(1994, 7, 19)
yesterday = dt.timestamp()
# now = datetime.now().timestamp()  # 选目前
now = datetime(2018, 3, 19).timestamp()  # 选任意日期
day = (now-yesterday)/(24*60*60)
print("%d" % (day + 1))


"""
time.gmtime()
Out[17]: time.struct_time(tm_year=2018, tm_mon=5, tm_mday=3, tm_hour=13, tm_min=47, tm_sec=34, tm_wday=3, tm_yday=123, tm_isdst=0)

time.localtime()
Out[20]: time.struct_time(tm_year=2018, tm_mon=5, tm_mday=3, tm_hour=21, tm_min=51, tm_sec=7, tm_wday=3, tm_yday=123, tm_isdst=0)

"""
#
# now = datetime.now()
#
# print('%02d/%02d/%04d' % (now.month, now.day, now.year))
# print('%02d:%02d:%02d' % (now.hour, now.minute, now.second))
#
# print(now)
# print(now.year)
# print(now.month)
# print(now.day)
# print(time.gmtime())


# $ pydoc time