import re
import gevent
from gevent import monkey
import socket


# 打补丁，把耗时的地方用于切换任务
monkey.patch_all()


class WebServer(object):
    def __init__(self):
        # 创建TCP套接字(监听、链接套接字)
        self.tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # 端口复用
        self.tcp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # 绑定
        self.tcp_socket.bind(("", 8888))

        # 监听，将套接字变为被动，系统创建一个链接队列
        self.tcp_socket.listen(128)

    def __del__(self):
        self.tcp_socket.close()

    def start(self):
        while True:
            new_socket, cli_addr = self.tcp_socket.accept()
            print(cli_addr, "成功连接")

            gevent.spawn(self.handle_client, new_socket)

    # 处理客户的数据，参数为成功连接的客户端套接字
    def handle_client(self, new_socket):
        # 接收客户端的数据，客户没有发送内容，阻塞，注意，使用服务套接字接收内容
        recv_data = new_socket.recv(1024)
        if len(recv_data) == 0:  # 说明浏览器断开连接
            new_socket.close()
            return

        print("*" * 40)

        # 以行为单位，切割，以列表方式返回
        lines = recv_data.decode().splitlines()
        print("lines[0] = ", lines[0])

        # lines[0] = GET /aaaa HTTP/1.1
        result = re.match(r"[^/]+/([^ ]+)", lines[0])
        if result:
            filename = "html" + "/" + result.group(1)
        else:
            filename = "html/index.html"

        print("filename = ", filename)

        try:  # 成功打开文件
            # 打开 只读二进制方式打开
            with open(filename, "rb") as f:
                content = f.read()

            send_data = "HTTP/1.1 200 OK\r\n"  # 状态行
            send_data += "\r\n"  # 空行
        except Exception as ret:  # 打开文件失败
            send_data = "HTTP/1.1 404 Not Found\r\n"  # 状态行
            send_data += "\r\n"  # 空行
            content = "404 Not Found".encode()

        new_socket.send(send_data.encode())  # 先发响应包体之前的内容
        new_socket.send(content)  # 再发响应包体内容， content本来就是二进制，无需转码

        # 关闭套接字
        new_socket.close()


def main():

    obj = WebServer()
    obj.start()


if __name__ == "__main__":
    main()
