import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 5250)
sock.connect(server_address)

message = 'PLAY 1-10 "ENCHD" CUT 1 Linear RIGHT LOOP\r\n'
sock.sendall(message)