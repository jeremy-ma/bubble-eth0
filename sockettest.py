import socket
import json

data = {"type": "hello", "team": "BUBBLE"}
test_exchange = '10.0.39.122'
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((test_exchange, 25000))
s.send(json.dumps(data) + '\n')
result = json.loads(s.recv(1024))
print result
s.close()