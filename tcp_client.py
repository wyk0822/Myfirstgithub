from socket import *

# 创建套接字
sockfd = socket(AF_INET, SOCK_STREAM)

# 发起连接
server_addr = ("0.0.0.0", 8888)
sockfd.connect(server_addr)

# 发送接收
while True:

    data = input("发送>>")
    sockfd.send(data.encode())

    if data == '##':
        break
    data = sockfd.recv(1024)
    print("接收到：", data.decode())

# 关闭
sockfd.close()


