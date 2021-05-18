import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(("tranfer.sh",80))
    s.sendall(b"GET / HTTP/1.1\r\nHost: transfer.sh\r\nAccept: text/html\r\nConnection: keep-alive\r\n\r\n")
    while 1:
        data = s.recv(1024)
        if not data:
            break
        print(data.decode())
