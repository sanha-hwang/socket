from socket import *
import threading
import time
# 소켓 통신 송신
def send(sock):
    while True:
        sendData = input(">>>")
        sock.send(sendData.encode("utf-8"))
# 소켓 통신 수신
def receive(sock):
    while True:
        recvData = sock.recv(1024)
        print('상대방: {}'.format(recvData.decode('utf-8')))

port = 8081 # 소켓 프로그램에 할당해줄 포트 번호

clientsocket = socket(AF_INET, SOCK_STREAM)
clientsocket.connect(("172.30.1.12",port)) # 나 여기 있소, 빈 문자열은 broadcast, 아니면 본인 ip주소

print("접속 완료")

sender = threading.Thread(target=send,args=(clientsocket,))
sender.daemon = True
receiver = threading.Thread(target=receive, args=(clientsocket,))
receiver.daemon = True
sender.start()
receiver.start()
while 1:
    time.sleep(1)
    pass