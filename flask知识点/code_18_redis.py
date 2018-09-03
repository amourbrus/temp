# 不用导入flask， 单独的
import redis

# host ,port 可以不用写，默认的就行，加一个decode_response
redis_obj = redis.StrictRedis(decode_responses=True)


def add_name():

    set1 = redis_obj.set("name", "py")  # 设置值，key-vlaue形式
    set2 = redis_obj.set("name", "python")  # 修改
    setex = redis_obj.setex("name", 50, "python_bomb")
    mset = redis_obj.mset({"project": "do_list", "name_1": "true_man", "what": "ever"})
    append_key = redis_obj.append("name1", "yes i append")
    keys = redis_obj.keys("*")   # keys pattern 查看所有键
    exist_if = redis_obj.exists("hello")
    type_key = redis_obj.type("name")   # single para
    # dele = redis_obj.delete("name", "i")  # return 删除key的数目，可多个key作为参数
    print(set1, set2,)
    print("setex ---> %s " % setex)
    print("mset --->%s" % mset)
    print("append key -->%s" % append_key)
    print ("keys * ---> %s" % keys)
    print("exist_if ---> %s" % exist_if)
    print("type key --->%s" % type_key)
    # print("del key1 key2 --->%s" % dele)
    print("*"*40)


def string_get_name():
    todo = redis_obj.get("name")
    todo1 = redis_obj.get("name")
    todo2 = redis_obj.mget("project", "name", "what")  # 获取多个键的value值
    print(todo, todo1, todo2)


def hash_type():
    # hset what_hash whatsthis itheima  --- hset key name(field属性) value
    single_field = redis_obj.hset(name="what_hash", key="whatsthis", value="itheima")

    many_field = redis_obj.hmset(name="school", mapping={"name": "python", "age": 10})
    hmget = redis_obj.hmget(name="school", keys=("name", "age"))

    all_values = redis_obj.hvals("school")  # 单个参数 name, todo 所有参数的=前面都可以不写

    dele = redis_obj.hdel(name="school", )  # todo ??
    # value = redis_obj.hvals("school")
    print("hset key field value --->%s" % single_field)
    print("many_field --->%s" % many_field)
    print("hmget --- > %s" % hmget)
    print("all values -->%s" % all_values)
    print("dele ---> %s , value = %s" % dele)
    # print("after del --> %s" % value)


if __name__ == '__main__':
    add_name()
    string_get_name()
    print("$"*40)
    hash_type()
