import socket
import threading

clients = [] #Lista de clientes conectados
HOST = "0.0.0.0"
PORT = 8080

def handle_client(conn, addr):
    data = conn.recv(1024)
    name = data.decode().strip()
    print(f"[+] CLiente conectado: {name}-{addr}", flush=True)
    clients.append(conn)
    
    try:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            msg = data.decode().strip()
            print(f"{name}: {msg}", flush=True)
            
            #reenviar a los demas
            for client in clients:
                if client != conn:
                    try:
                        client.sendall(f"{name}: {msg}\n".encode())
                    except:
                        pass
    finally:
        print(f"[-] Cliente desconectado: {name}", flush=True)
        clients.remove(conn)
        conn.close()

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"Listening on: {HOST}:{PORT}...", flush=True)

        while True:
            conn, addr = s.accept() #Cuando se conecta un cliente
            threading.Thread(target=handle_client, args=(conn, addr), daemon=True).start() #abre un hilo de cliente

main()

