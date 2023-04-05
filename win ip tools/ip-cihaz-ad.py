import socket
import time as t

ip_address = input("Cihaz adını öğrenmek istediğiniz IP adresi: ")

try:
    host_name = socket.gethostbyaddr(ip_address)
    print("IP adresi {} için cihaz adı: {}".format(ip_address, host_name[0]))
except socket.herror:
    print("Belirtilen IP adresi geçersiz veya cihaz adı bulunamadı.")


t.sleep(100)