from pytube import YouTube
import os.path
from tkinter import *


ui = Tk()
ui.geometry("700x180")
ui.title("YouTube Video Downloader")
t1 = Label(ui, text="Paste the Youtube video url here", font=('bold', 20))
t1.place(x=120, y=20)
myLink=StringVar()
me = Entry(ui, width=60, textvariable=myLink)
me.place(x=140, y=80)
def downloadVideo():
    try:
        x = str(myLink.get())
        ytv = YouTube(x).streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        ytv.download('.')
        t2 = Label(ui, text=YouTube(x).title + "  Downloaded 👍👍👍")
        t2.place(x=200, y=150)
    except:
       t2 = Label(ui, text="Unable to download 😐😐😐")
       t2.place(x=200, y=150)

Button(ui, text="Download", width=20, bg="green", fg="white", command=downloadVideo).place(x=220, y=110)

ui.mainloop()