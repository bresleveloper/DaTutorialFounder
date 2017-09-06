import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("http://www.python.org", 80))

ans = s.recv(500)

print(ans)

s.close()