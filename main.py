import socket
import pygame
import threading
import time
players = 0
ready_cnt = 0
ready_list = {}
Now_Map = 
class Map:
    H = 10
    W = 10
    ter = {}
    camp = {}
    Val = {}
def Write_log( buf ) :
    with open( "GeneralSoil&Yy-Log.txt" , "a" ) as file:
        file.write( buf )
def New():
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    address = ('', 7788)
    tcp_server_socket.bind(address)
    tcp_server_socket.listen(128)
    return tcp_server_socket
def Make_Send(to):
    global tcp_socket
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_addr = (to, 7788)
    tcp_socket.connect(server_addr)
def Send( buf ):
    tcp_socket.send(buf.encode("gbk"))
def fast_send( to , buf ) :
    tmp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_addr = (to, 7788)
    tmp_socket.connect(server_addr)
    tmp_socket.send(buf.encode("gbk"))
def Listening( From , Player ):
    while True :
        get = From.recv(1024)
        if get :
            get = get.decode('gbk').split()
            if get[0] == "ready" :
                if ready_list[Player] != True :
                    ready_list[Player] = True
                    ready_cnt += 1
                    if ready_cnt == players :
                        
        else:
            break
def Match() :
    Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    address = ('', 7788)
    Socket.bind(address)
    Socket.listen(128)
    while True :
        client_socket , clientAddr = Socket.accept()
        get = client_socket.recv(1024).decode('gbk').split()
        if get[0] == "join" :
            Write_log( "[" + time.ctime() + "] Player " + get[1] + " join.\n" )
            players += 1
            Lanch_Listening = threading.Thread( target = Listening , args = ( client_socket , get[1] ) )
            Lanch_Listening.start()
def Server() :
    Lanch_Net = threading.Thread( target = Match )
    Lanch_Net.start()
res = input( "Server（s）？" )
LiBack = []
if res == 's' :
    Lanch_Server = threading.Thread( target = Server )
    Lanch_Server.start()
to_server = input( "目标服务器IP？" )
nick = input( "昵称？" )
print( "连接到服务器..." )
Make_Send( to_server )
Send( "join " + nick )
