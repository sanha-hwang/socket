from socket import *
from _thread import *
import threading
import time

# 소켓 통신 송신
def send(sock):
    while True:
        sendData = input(">>>")
        sock.send(sendData.encode("utf-8"))

# 소켓 통신 수신
def receive(sock, addr):
    while True:
        try:
            recvData = sock.recv(1024)
            if not recvData:
                print("Disconnected by {}, {}".format(addr[0], addr[1]))
                break
            print("msg from {}, {} : {}".format(addr[0],addr[1],recvData.decode("utf-8")))
        except:
            break
    return False

def threaded(client_socket, addr):
    print("connected by {}, {}".format(addr[0], addr[1]))
    while 1:
        try:
            sender = threading.Thread(target=send,args=(client_socket,addr))
            sender.daemon = True
            receiver = threading.Thread(target=receive, args=(client_socket,addr))
            receiver.daemon = True
            sender.start()
            receiver.start()
            if receiver == False:
                break
        except:
            break
    client_socket.close()
    return print("ㅋ")


port = 8081 # 소켓 프로그램에 할당해줄 포트 번호

serversocket = socket(AF_INET, SOCK_STREAM)
serversocket.bind(("172.30.1.12",port)) # 나 여기 있소, 빈 문자열은 broadcast, 아니면 본인 ip주소
serversocket.listen() # 2개 client 받아보기

print("%d번 포트로 접속 대기중..."%port)

i = 0
while i <2:
    ConnectionSocket, addr = serversocket.accept()
    i +=1
    start_new_thread(threaded,(ConnectionSocket, addr))


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