import random
import socket

MAX_UDP_SEND_LEN = 1000

target_addr = ('192.168.0.128',1234)

def random_int_list(start, stop, length):
    start, stop = (int(start), int(stop)) if start <= stop else (int(stop), int(start))
    length = int(abs(length)) if length else 0
    random_list = []
    for i in range(length):
        random_list.append(random.randint(start, stop))
    return random_list

skt  = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

for length in range(1,MAX_UDP_SEND_LEN+1):
    send_data = bytes( random_int_list(1,200,length) )
    skt.sendto(send_data, target_addr)
    recv_data, recv_addr = skt.recvfrom(MAX_UDP_SEND_LEN)
    if not recv_data:
        print("recv timeout!")
    else:
        if send_data == recv_data:
            print("[okay ]", end=" ")
        else:
            print("[fail!]", end=" ")
        print("recv len %d from %s:%d" % (len(recv_data), recv_addr[0], recv_addr[1]) )

skt.close()
