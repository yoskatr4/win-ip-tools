import tkinter as tk
import socket

def scan_proxies():
    proxies = []
    for port in [8080, 3128, 80, 4040, 1]:
        for host in ["", "127.0.0.1",  "127.0.0.2", "127.0.0.3", "127.0.0.167","localhost"]:
            try:
                addr = socket.getaddrinfo(host, port, socket.AF_INET, socket.SOCK_STREAM, socket.SOL_TCP)
                proxies.append((host, port))
            except socket.error:
                pass
    return proxies

def scan_proxies_gui():
    # pencere oluşturun
    window = tk.Tk()
    window.title("Proxy Tarayıcı")

    # metin kutusu oluşturun
    textbox = tk.Text(window)
    textbox.pack()

    # buton oluşturun ve fonksiyona bağlayın
    button = tk.Button(window, text="Proxy'leri Tara", command=lambda: textbox.insert(tk.END, "\n".join(str(p) for p in scan_proxies())))
    button.pack()

    # mainloop() başlatın
    window.mainloop()

scan_proxies_gui()
