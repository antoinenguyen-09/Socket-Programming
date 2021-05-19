import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    s.connect(("144.76.136.153",80)) # using socket.gethostbyname('transfer.sh') to gain IP address of host
    s.sendall(b"GET / HTTP/1.1\r\nHost: transfer.sh\r\nAccept: text/html\r\nConnection: keep-alive\r\n\r\n")

    while 1:
        data = s.recv(100)
        if not data:
            break
        print(data.decode())
