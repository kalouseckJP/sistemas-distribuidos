import socket
import threading

print("Ingresa la IP del servidor")
HOST =  input()
PORT = 8080

def listen(sock):
    while True:
        data=sock.recv(1024)
        if not data:
            break
        print(data.decode().strip())

def main():
    Usr = input("-> Ingrese su nombre: ")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        threading.Thread(target=listen, args=(s,), daemon=True).start()
        print(f"Connecting to -> {HOST}:{PORT}")
        s.sendall((Usr + "\n").encode("utf-8"))

        print("write something, or 'EXIT' to close: ")
        while True:
            msg = input("> ")

            if msg == "EXIT":
                break

            s.sendall((msg + "\n").encode("utf-8"))

if __name__ == "__main__":
    main()