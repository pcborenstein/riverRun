import socket



s = socket.socket()
#http://www.gate-riverrun.com/Results%20files/grr09overallresB.htm
#http://www.1stplacesports.com/grr16overallres.htm
host=socket.gethostbyname('www.1stplacesports.com')
port = 80
s.connect((host, port))
print("host: ", host)
#s.sendall("GET /grr16overallres.htm\r\nHost: www.1stplacesports.com\r\n")
s.sendall("""
GET /grr16overallres.htm HTTP/1.1\r\n
Host: www.1stplacesports.com\r\n
\r\n
""")
val = s.recv(1000)

print(val)
