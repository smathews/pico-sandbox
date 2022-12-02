import network, usocket as socket 

ap = network.WLAN(network.AP_IF)
ap.config(essid="foobar", password="foobarfoobar")
ap.active(True)

while ap.active() == False:
    pass

print(ap.ifconfig())

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('',80))
s.listen()

conn, addr = s.accept()
print("Got a connection from %s" % str(addr))
request = conn.recv(1024)
print("Content = %s" % str(request))
conn.send("<html><body><h1>Foobar</h1></body></html>")
conn.close()
