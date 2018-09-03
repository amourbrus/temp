# http服务器
import socket
import gevent
from gevent import monkey
import re

# 打补丁  把耗时的地方用于切换任务
monkey.patch_all()


def client_handle(client_socket):
    # receive
    recv_data = client_socket.recv(1024)
    # 判断浏览器断开连接
    if len(recv_data) == 0:
        client_socket.close()
        return
    # 以行为单位对 recv_data 切割,以列表返回
    lines = recv_data.decode().splitlines()
    # lines[0] = GET /xxx HTTP/1.1
    # 正则匹配出请求 xxx
    result = re.match(r"[^/]+/([^ ]+)", lines[0])
    # 设置默认网址
    if result:
        filename = "html" + "/" + result.group(1)
    else:
        filename = "html/index.html"
    print("filename = ", filename)
    # 成功打开文件
    try:
        with open(filename, "rb") as f:
            content = f.read()
        # 报文格式
        send_data = "HTTP/1.1 200 OK\r\n"  # 状态行
        send_data += "\r\n"  # 空行
    except Exception as ret:
        send_data = "HTTP/1.1 404 NOT FOUND\r\n"
        send_data += "\r\n"
        content = "404 NOT FOUND".encode()

    # send
    client_socket.send(send_data.encode())
    client_socket.send(content)

    client_socket.close()


def main():
    # 创建TCP套接字(监听、链接套接字)
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 端口复用
    tcp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # 绑定
    tcp_socket.bind(("", 8888))
    # 监听，将套接字变为被动，系统创建一个链接队列
    tcp_socket.listen(128)
    # 为多个用户服务
    while True:
        new_socket, cli_addr = tcp_socket.accept()
        print(cli_addr, "连接成功")
        # 开协程  调用函数处理 new_socket
        gevent.spawn(client_handle, new_socket, )

    tcp_socket.close()


if __name__ == '__main__':
    main()
