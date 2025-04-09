import tkinter.messagebox
import customtkinter as ctk
from PIL import Image
import webbrowser
import threading
import tkinter
import main 
import os 




compression_image = Image.open('com.png')
compression_logo = ctk.CTkImage(compression_image , size=(30,30) )
decompression_image = Image.open('decom.png')
decompression_logo = ctk.CTkImage(decompression_image , size=(30,30) )
github = Image.open('github.png')
github_logo = ctk.CTkImage(github , size=(30,30) )

class Main(ctk.CTk):
    def __init__(self, fg_color = '#ffffff'):
        super().__init__(fg_color=fg_color)
        title = ctk.CTkLabel(self , fg_color='white' , text_color='black' , text='Data compression with Python and the LZW algorithm ').pack()
        space = ctk.CTkLabel(self , text='').pack()

        self.compress_btn = ctk.CTkButton(self , fg_color='white' , border_color='black' , 
                                         border_width=3 , text_color='black' , text='  Compressing',
                                         width=500 , hover_color='#003d73' , image=compression_logo ,
                                         command=self.get_file)
        self.compress_btn.pack( pady=4 ,ipady=8)
        
        self.decompress_btn = ctk.CTkButton(self , fg_color='white' , border_color='black' , 
                                         border_width=3 , text_color='black' , text='decompressing',
                                         width=500 , hover_color='#003d73',image=decompression_logo )
        self.decompress_btn.pack( pady=4 , ipady=8 )

        self.github_btn = ctk.CTkButton(self , fg_color='white' , border_color='black' , 
                                         border_width=3 , text_color='black' , text='    sourc code',
                                         width=500 , hover_color='#003d73' ,image=github_logo , command=self.open_url )
        self.github_btn.pack( pady=4 , ipady=8 )
        
    def open_url(self):
        webbrowser.open_new_tab('https://github.com/itsMajid-dev/compression')


    def get_file(self):
        self.i=ctk.filedialog.askopenfilename(title='select text file' ,filetypes=[("text files","*.txt" ) , ("xml files","*.xml" ),("json file","*.json" )])
        if self.i:
            self.show_window_for_comperss()
        else:
            pass
    def show_window_for_comperss(self):
        self.f = ctk.CTkFrame(self , fg_color='white' , corner_radius=0 , )
        self.f.place(relx=0 , rely=0 , relwidth=1 , relheight=1)

        back =ctk.CTkButton(self.f , fg_color='white' , border_color='black' , 
                                         border_width=2 , text_color='black' , text='  back',
                                         width=80 , hover_color='#003d73' ,
                                         command=lambda : self.f.destroy())
        back.place(relx=0.01 , rely=0.01 )
        self.title_ = ctk.CTkLabel(self.f, fg_color='white' , text_color='black' , text='compresing...')
        self.title_.pack()
        space = ctk.CTkLabel(self.f , text='').pack()
        path = ctk.CTkEntry(self.f, fg_color='white' , corner_radius=1 , border_color='black' , border_width=2,text_color='black')
        path.insert(ctk.END , self.i)
        path.place(relx=0.1 , rely=0.2 , relwidth=0.8)

        size = ctk.CTkEntry(self.f , fg_color='white' , corner_radius=1 , border_color='black' , border_width=2,text_color='black')
        self.file_size = os.path.getsize(self.i)
        
        
        if self.file_size>150000: 
            size.configure(text_color='red')
        size.insert(ctk.END ,f'{self.file_size} B')
        size.place(relx=0.1 , rely=0.31 , relwidth=0.8)

        run = ctk.CTkButton(self.f , text='RUN' , text_color='black' , fg_color='#0099ff' , command=self.run)
        run.place(relx=0.4 , rely=0.47 ,)
        
        self.ex = ctk.CTkTextbox(self.f , fg_color='white' , text_color='red' , border_color='black' , border_width=2)
        self.ex.place(relx=0.1 , rely=0.556, relheight=0.3 , relwidth=0.8)

        

    def run(self):
        
        if self.file_size>150000:
            tkinter.messagebox.showerror("خطا" , 'درحال حاظر فایل های بیش از 1.2 مگابایتی را نمیتوان فشرده کرد احتمالا در نسخه های بعدی محدودیت ها رفع شود ')
            return
        def kernel():
            C = main.Encoding()
            C.load(self.i)
            try:
                name = self.i.split('/')[-1].split('.')[0]
            except:
                name = 'unknow'
            C.save(name)
            self.info_dict = C.compressing_informations()
            tkinter.messagebox.showinfo("تمام" , 'فایل با موفقیت فشرده شد')
            if len(C.excepts)>0:
                for i in C.excepts:
                    self.ex.insert('0.0' ,  f'\ncharacter {i} is not supported!\n')
        threading.Thread(target=kernel).start()

        info = ctk.CTkButton(self.f , text='INFO' , text_color='black' , fg_color='#0099ff' , command=self.info)
        info.place(relx=0.4 , rely=0.86,)
        self.title_.configure(text='finish')

    def info(self):
        i = self.info_dict
        tkinter.messagebox.showinfo('اطلاعات' ,f"normal size : {i['normal_size']}\ncompressedsize : {i['compressed_size']}\ncompression_percent : {i['compression_percent']}\nElapsed_time : {i['Elapsed_time']}")




        
a = Main()
a.geometry("700x340+100+100")
a.resizable(False , False)
a.title('compression')
a.mainloop()
        