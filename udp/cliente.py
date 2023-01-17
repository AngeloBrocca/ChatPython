import socket

HOST = input('insira ip: ')
PORT = int(input('insira porta: '))

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest = (HOST, PORT)

udp.connect(dest)
udp.sendall(str.encode('FOIFOIFOI'))
data = udp.recv(1024)

print('Mensagem ecoada: ', data.decode())