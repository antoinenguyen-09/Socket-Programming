import socket
import select

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('144.76.136.153', 80))   # using socket.gethostbyname('transfer.sh') to gain IP address of host
s.sendall(b'GET /pAsmS/HoangNCH_challege4.md HTTP/1.1\r\nHOST: transfer.sh\r\n\r\n')

reply = b''

while select.select([s], [], [], 3)[0]:
    data = s.recv(2048)
    if not data: break
    reply += data

headers =  reply.split(b'\r\n\r\n')[0]
image = reply[len(headers)+4:]

# save image
f = open('HoangNCH_challege4.md', 'wb')
f.write(image)
f.close()
