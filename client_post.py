import sys
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("144.76.136.153",80))  # socket.gethostbyname('transfer.sh')
# Do trang transfer.sh chưa có chức năng nào có thể dùng được POST request nên tạm thời để source request đến là "/" 
header = "POST / HTTP/1.1\r\n
Host: transfer.sh\r\n
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:46.0) Gecko/20100101 Firefox/46.0\r\n
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\n
Accept-Language: en-US,en;q=0.5\r\n
Accept-Encoding: gzip, deflate\r\n
Referer: http://google.com\r\n
Cookie: PHPSESSID=blub\r\n
Connection: keep-alive\r\n
Content-Type: application/x-www-form-urlencoded\r\n"

contentLength = "Content-Length: " + str(len( data )) + "\r\n"
request = header + contentLength
s.send(''.join(format(ord(i), '08b') for i in request)) 
response = s.recv(4096)
s.close()
print(request)
print(response,'\n')
sys.exit()
