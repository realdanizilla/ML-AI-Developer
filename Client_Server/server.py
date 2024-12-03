import socket

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("servidor esperando conexões...")


conn, addr = s.accept()
with conn:
    print("conectado por", addr)
    while True:
        data = conn.recv(1024)
        if not data:
            break
        print("mensagem recebida: ", data.decode())
        conn.sendall(data)
