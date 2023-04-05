import socket
import os
import time
import tkinter as tk

def scan_devices():
    subnet = subnet_entry.get()
    startIP = int(startIP_entry.get())
    endIP = int(endIP_entry.get())

    devices = []

    try:
        for i in range(startIP, endIP+1):
            ip = subnet + str(i)
            response = os.system("ping -n 1 -w 1000 " + ip)
            if response == 0:
                try:
                    host = socket.gethostbyaddr(ip)
                    devices.append((host[0], ip))
                except socket.herror:
                    devices.append((ip,))
            else:
                pass

    except KeyboardInterrupt:
        results_text.insert(tk.END, "\nTarama durduruldu.")
        return
    
    results_text.insert(tk.END, "\nTarama tamamlandı. Bulunan cihazlar:\n")
    for device in devices:
        if len(device) == 2:
            results_text.insert(tk.END, "{} ({})\n".format(device[0], device[1]))
        else:
            results_text.insert(tk.END, "{}\n".format(device[0]))
    
root = tk.Tk()
root.title("IP Adresi Tarama")

subnet_label = tk.Label(root, text="Alt ağ adresi (örn. 192.168.1.):")
subnet_label.pack()
subnet_entry = tk.Entry(root)
subnet_entry.pack()

startIP_label = tk.Label(root, text="Başlangıç IP'si:")
startIP_label.pack()
startIP_entry = tk.Entry(root)
startIP_entry.pack()

endIP_label = tk.Label(root, text="Bitiş IP'si:")
endIP_label.pack()
endIP_entry = tk.Entry(root)
endIP_entry.pack()

scan_button = tk.Button(root, text="Tara", command=scan_devices)
scan_button.pack()

results_text = tk.Text(root)
results_text.pack()

root.mainloop()
