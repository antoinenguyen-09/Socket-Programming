import socket
import tqdm
import os

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096 # send 4096 bytes each time step
filename = "message.txt"
# get the file size
filesize = os.path.getsize(filename)
# create the client socket
s = socket.socket()
print(f"[+] Connecting to 144.76.136.153:80") # using socket.gethostbyname('transfer.sh') to gain IP address of host
s.connect(('144.76.136.153', 80))
print("[+] Connected.")
# send the filename and filesize
s.send(f"{filename}{SEPARATOR}{filesize}".encode())
# start sending the file
progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024)
with open(filename, "rb") as f:
    while True:
        # read the bytes from the file
        bytes_read = f.read(BUFFER_SIZE)
        if not bytes_read:
            # file transmitting is done
            break
        # we use sendall to assure transimission in busy networks
        s.sendall(bytes_read)
        # update the progress bar
        progress.update(len(bytes_read))
# close the socket
s.close()
