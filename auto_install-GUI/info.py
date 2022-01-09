import tkinter as tk 
class Info_l:
    def __init__(self):
        root=tk.Tk()
        root.geometry('499x140')
        root.title('INFO')
        root.resizable(False,False)
        root.configure(bg='white')
        # label set 
        self.l_ita=tk.Label(root,text='ITA:il sorgente che hai scaricato lo trovi nella cartella auto_install-GUI')
        self.l_eng=tk.Label(root,text='ENG:the source you download can be found in the auto_install-GUI folder')
        self.l_ita.place(x=0,y=2)
        self.l_eng.place(x=0,y=50)
        self.l_eng.configure(bg='white')
        self.l_ita.configure(bg='white')
        root.mainloop()
