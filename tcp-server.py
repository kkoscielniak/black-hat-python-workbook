import socket
import threading

ip = "127.0.0.1"
port = 9999

def handle_client(client_socket):
    with client_socket as sock:
        request = sock.recv(1024)
        print(f"[+] Received: {request.decode('utf-8')}")
        sock.send(b"ACK")

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ip, port))
    server.listen(5) # 5 concurrent connections
    print(f"[+] Listening on {ip}:{port}")

    while True:
        client, address = server.accept()
        print(f"Accepted connection from {address[0]}:{address[1]}")
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()

if __name__ == '__main__':
    main()
