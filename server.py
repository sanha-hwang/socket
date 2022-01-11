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

serversocket = socket(AF_INET, SOCK_STREAM)
serversocket.bind(("172.30.1.12",port)) # 나 여기 있소, 빈 문자열은 broadcast, 아니면 본인 ip주소
serversocket.listen(1) # 2개 client 받아보기

print("%d번 포트로 접속 대기중..."%port)

ConnectionSocket, addr = serversocket.accept()
print("접속 ip:{}".format(str(addr)))

sender = threading.Thread(target=send,args=(ConnectionSocket,))
sender.daemon = True
receiver = threading.Thread(target=receive, args=(ConnectionSocket,))
receiver.daemon = True

sender.start()
receiver.start()

while 1:
    time.sleep(1)
    pass

# while True:
#     print("통신을 진행중입니다.")
#     data = ConnectionSocket.recv(1024)
#     print("IP {}의 메세지: {}".format(str(addr), data))

#     ConnectionSocket.send("Hello, I am Server.".encode("utf-8"))
#     print("Complete Sending Message")

#     if data.decode("uft-8") == " bye":
#         ConnectionSocket.send("bye")
#         break
# ConnectionSocket.close()
# serversocket.close()