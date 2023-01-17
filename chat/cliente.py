import socket 
import random 
from threading import Thread 
# cores pra cada usuario 
from colorama import Fore, init, Back 
 
# inicia cores 
init() 
 
# as cores 
colors = [Fore.BLUE, Fore.CYAN, Fore.GREEN, Fore.LIGHTBLACK_EX, 
          Fore.LIGHTBLUE_EX, Fore.LIGHTCYAN_EX, Fore.LIGHTGREEN_EX, 
          Fore.LIGHTMAGENTA_EX, Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX, 
          Fore.LIGHTYELLOW_EX, Fore.MAGENTA, Fore.RED, Fore.YELLOW 
          ] 
 
# escolhe cor 
client_color = random.choice(colors) 
 
# dai começa 
SERVER_HOST = input('insira id do host: ') 
SERVER_PORT = int(input('insira port: ')) 
separator_token = "<SEP>"  # faz a separação nome e mensagem 
 
# TCP socket 
s = socket.socket() 
print(f"[*] conectando em {SERVER_HOST}:{SERVER_PORT}...") 
# connecta o server 
s.connect((SERVER_HOST, SERVER_PORT)) 
print("[+] Connectado.") 
# insere o nome do cliente 
name = input("Insira seu nome: ") 
 
 
def listen_for_messages(): 
    while True: 
        message = s.recv(1024).decode() 
        print("\n" + message) 
 
    # thread listen mensagem e printa 
 
t = Thread(target=listen_for_messages) 
 
# start 
t.start() 
 
while True: 
    # input da mensagem 
    to_send = input() 
    # um jeito de sair do programa 
    if to_send.lower() == 'q': 
        break 
 
    to_send = f"{client_color} {name}{separator_token}{to_send}{Fore.RESET}" 
    # manda mensagem 
    s.send(to_send.encode()) 
 
# fecha socket 
s.close() 