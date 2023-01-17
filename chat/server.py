import socket 
from threading import Thread 
 
# server IP e PORT
SERVER_HOST = input('insira id do host: ') 
SERVER_PORT = int(input('insira port: ')) 
separator_token = "<SEP>"  # separa nome do cliente e mensagem 
 
# inicializa list/set dos sockets dos clientes conectados 
client_sockets = set() 
# cria socket tcp 
s = socket.socket() 
# faz o port ser reutilizavel 
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
# faz o bind 
s.bind((SERVER_HOST, SERVER_PORT)) 
# faz o listen 
s.listen(5) 
print(f"[*] Listen: {SERVER_HOST}:{SERVER_PORT}") 
 
 
def listen_for_client(cs): 
    # cs = socket 
    # a funçao faz o broadcast pros clientes conectados das mensagens recebidas 
    while True: 
        try: 
            # continua o listen por uma mensagem 
            global msg 
            msg = cs.recv(1024).decode() 
        except Exception as e: 
            # cliente não conectado 
            # remove do set 
            print(f"Error: {e}") 
            client_sockets.remove(cs) 
        else: 
            # substitui o <sep> pelo : 
            msg = msg.replace(separator_token, ": ") 
            # iterar todos os sockets conectados 
        for client_socket in client_sockets: 
            # manda mensagem 
            client_socket.send(msg.encode()) 
 
 
while True: 
    # faz o accept 
    client_socket, client_address = s.accept() 
    print(f"[+] {client_address} conectado.") 
    # adiciona cliente nos sockets 
    client_sockets.add(client_socket) 
    # thread que escuta as mensagens dos clientes 
    t = Thread(target=listen_for_client, args=(client_socket,)) 
    # start 
    t.start() 
 
# fecha sockets dos clientes 
for cs in client_sockets: 
    cs.close() 
# fecha tudo 
s.close() 