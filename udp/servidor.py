import socket

HOST = input('insira ip: ')
PORT = int(input('insira porta: '))

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
orig = (HOST, PORT)
try:
    udp.bind(orig)
except:
    print('Deu ruim no bind')

while True:
    msg, cliente = udp.recvfrom(1024)
    print(cliente, msg)
udp.close()