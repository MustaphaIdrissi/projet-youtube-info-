from tkinter import *
from tkinter import Tk
from types import FrameType
from tkinter import messagebox
import pytube
from pytube import YouTube
from pytube.__main__ import YouTube

root=Tk()
root.geometry("800x500+400+200")
root.title("Info video Youtube")
root.resizable(False,False)
root.configure(bg="#D4FC79")

link=""
def info():
    link=eb1.get()
    info1=YouTube(link)
    lb3["text"]=info1.video_id
    lb5["text"]=info1.title
    lb7["text"]=info1.thumbnail_url
    lb9["text"]=info1.keywords
def download():
    link=eb1.get()
    info1=YouTube(link)
    vedio=info1.streams.get_highest_resolution()
    vedio.download()
    messagebox.showinfo("downland","downland complet !")
   



lb1=Label(root,text="Past link here :",font=("arial",16,"bold"),pady=12)
lb1.pack(fill=X)
eb1=Entry(root,width=71,font=("arial",14,"bold"))
eb1.place(x=6,y=60)
bt1=Button(root,text="search",width=61,font=("arial",14,"bold"),fg="#FF2233",command=info)
bt1.place(x=30,y=90)


f1=Frame(root,width=800,height=150,bg="#D4FC79")
f1.place(x=0,y=140)
lb2=Label(f1,text="Id :",font=("arial",16,"bold"),justify='center',bg="#D4FC79")
lb2.place(x=6,y=12)
lb3=Label(f1,text='dd' ,font=("arial",16,"bold"),justify='center',bg="#D4FC79",wraplength=500,borderwidth=2, relief="groove")
lb3.place(x=100,y=12)

lb4=Label(f1,text="Titre :",font=("arial",16,"bold"),justify='center',bg="#D4FC79")
lb4.place(x=6,y=50)
lb5=Label(f1,text="Titre :",font=("arial",16,"bold"),justify='center',bg="#D4FC79",wraplength=500,borderwidth=2, relief="groove")
lb5.place(x=100,y=50)

lb6=Label(f1,text="Poster :",font=("arial",16,"bold"),justify='center',bg="#D4FC79")
lb6.place(x=6,y=100)
lb7=Label(f1,text="Poster :",font=("arial",16,"bold"),justify='center',bg="#D4FC79",wraplength=500,borderwidth=2, relief="groove")
lb7.place(x=100,y=100)

f2=Frame(root,width=800,height=150,bg="#D4FC79")
f2.place(x=0,y=300)
lb8=Label(f2,text="Keyword :",font=("arial",16,"bold"),justify='center',bg="#D4FC79")
lb8.place(x=6,y=10)
lb9=Label(f2,borderwidth=2, relief="groove",bg="#D4FC79",text="",font=("arial",12,"bold")
,height=7,width=60,wraplength=500,pady=2,padx=2)
lb9.place(x=150,y=10)
f3=Frame(root,width=800,height=70,bg="#D4FC79")
f3.place(x=0,y=451)
bt2=Button(f3,text="Download video ",width=61,font=("arial",14,"bold"),fg="#FF2233",command=download)
bt2.place(x=30,y=6)




















root.mainloop()







