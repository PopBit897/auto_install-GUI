import tkinter as tk
import os 
import webbrowser
class windows:
    def __init__(self):
        root=tk.Tk()
        root.geometry('300x140')
        root.title('Auto_install')
        root.resizable(False,False)
        root.configure(bg='white')
        #comandi per i bottoni
        def new_w():
             root=tk.Tk()
             root.geometry('300x140')
             root.title('Ip_Tools_For_terminal')
       
             root.resizable(False,False)
             root.configure(bg='white')
             #-------------------------
             def d_0():
                 url='https://github.com/RedAnonymusITA/ip-tools/releases/tag/v0.0.1'
                 webbrowser.open(url)
             def new_v():
                 from info import Info_l
                 terminal=os.system('git clone https://github.com/RedAnonymusITA/ip-tools.git')
               
                 Info_l()
                 exit()
                 pass
            #-------------------------
             self.bt_ipto=tk.Button(root,text='Ip_Tools_For_terminal_v0.0.1',command=d_0)
             self.bt_iptn=tk.Button(root,text='Ip_Tools_For_terminal_new_version',command=new_v)
             self.bt_ipto.place(x=1,y=2)
             self.bt_iptn.place(x=1,y=50)
             root.mainloop()
        def GUI_ip():
            terminal=os.system('git clone https://github.com/RedAnonymusITA/ip_tools_GUI.git')
            
            from info import Info_l
            Info_l()
            exit()

        def psg():
            terminal=os.system('git clone https://github.com/RedAnonymusITA/Generatore_Password.git')
            terminal=os.system('cd  Generatore_Password')
            terminal=os.system('chmod +x start.sh')
            from info import Info_l
            Info_l()
            exit()

        # creazione dei bottoni 
        self.bt_ipt=tk.Button(root,text='Ip_Tools_For_terminal',command=new_w)
        self.bt_iptg=tk.Button(root,text='Ip_Tools-GUI',command=GUI_ip)
        self.bt_pg=tk.Button(root,text='Password_Generatore',command=psg)
        # asse x e y dei bottoni 
        self.bt_ipt.place(x=1,y=2)
        self.bt_iptg.place(x=179,y=2)
        self.bt_pg.place(x=1,y=50)
        root.mainloop()

windows()