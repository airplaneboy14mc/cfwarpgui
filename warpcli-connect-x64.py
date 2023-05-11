import os
import tkinter as tk
from tkinter import messagebox
import platform

if platform.processor() == 'x86_64' and platform.system() == 'Linux':
    class warp_cli():
        
        def connect(self):
            if self.status_check == True:
                os.popen('warp-cli disconnect')
                self.is_connected.set('Connect')
                self.is_connected2.set('Disconnected')
                self.status = os.popen('warp-cli status').read()
                self.status_check = 'Status update: Connected' in self.status
            else:
                os.popen('warp-cli connect')
                self.is_connected.set('Disconnect')
                self.is_connected2.set('Connected')
                self.status = os.popen('warp-cli status').read()
                self.status_check = 'Status update: Connected' in self.status
        
        def get_password(self, e):
            password = self.entry_box.get()
            os.system(f'echo {password} | sudo -S apt install cloudflare-warp -y')
            os.system(f'echo {password} | sudo -S yum install cloudflare-warp -y')
            self.install_win.destroy()
        
        def destroy_auth(self, e):
            self.install_win.destroy()
        
        def install(self):
            self.install_win = tk.Tk()
            self.install_win.geometry('200x50+550+300')
            self.install_win.resizable(False,False)
            self.install_win.title('Authentication')
            label = tk.Label(self.install_win, text='Sudo Password:', font=('Comic Sans MS', 10))
            label.pack(side='left',padx=3)
            self.entry_box = tk.Entry(self.install_win, width=20, font=('Comic Sans MS', 14), show='\u2022')
            self.entry_box.pack(side='left',padx=3)
            self.install_win.bind('<Return>', self.get_password)
            self.install_win.bind('<Escape>', self.destroy_auth)
        
        def minimize(self, e):
            self.root.iconify()
        
        def __init__(self):
            self.root = tk.Tk()
            self.root.title('Cloudflare Warp - Linux x64')
            self.root.geometry('300x125+500+250')
            self.root.resizable(False, False)
            self.root.bind('<Escape>', self.minimize)
            self.is_connected = tk.StringVar()
            self.is_connected2 = tk.StringVar()
            self.is_connected.set('Connect')
            self.status = os.popen('warp-cli status').read()
            self.status_check = 'Status update: Connected' in self.status
            
            self.top_frame = tk.Frame(self.root)
            self.bottom_frame = tk.Frame(self.root)
            self.top_frame.pack(side='top', pady=2)
            self.bottom_frame.pack(side='bottom',pady=3)
            
            self.title_label = tk.Label(self.top_frame, text='Cloudflare Warp CLI Connection', font=('Comic Sans MS', 18))
            self.title_label.pack()
            self.info_label = tk.Label(self.top_frame, text='Double click the "Connect"/"Disconnect" button \nto change your connection', font=('Comic Sans MS', 10))
            self.info_label.pack()
            self.connection_label = tk.Label(self.top_frame, textvariable=self.is_connected2, font=('Comic Sans MS', 12))
            self.connection_label.pack()
            self.connect_button = tk.Button(self.bottom_frame, textvariable=self.is_connected, command=self.connect)
            self.connect_button.pack(side='left')
            self.install_button = tk.Button(self.bottom_frame, text='Install', command=self.install)
            self.install_button.pack(side='left')
            
            self.root.mainloop()
            

    warp_cli()
    
elif platform.processor() != 'x86_64' and platform.system() == 'Linux':
    messagebox.showwarning('System Not Supported', 'Your system is not supported yet.')

else:
    messagebox.showerror('Incompatable System', 'Your system is not compatable with this software.')