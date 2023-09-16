from tkinter import *
import pyshorteners
def convert():
    s=pyshorteners.Shortener().tinyurl.short(url.get())
    shorturl.set(s)
root=Tk()
root.geometry("600x400")
root.title("Generate Short URL")

url=StringVar()
shorturl=StringVar()
Label(root,text="Enter URL",font="calibre,10,bold").grid(row=0,column=0)
Entry(root,textvariable=url,font="calibre,10,bold",width=30).grid(row=0,column=1)
Button(root,text="Convert",command=convert,relief=GROOVE).grid(row=2,column=0)
Label(root,text="Your Short URL",font="calibre,10,bold").grid(row=3,column=0)
Entry(root,textvariable=shorturl,font="calibre,10,bold").grid(row=3,column=1)

var = StringVar()
var.set("Kshitiz Verma")
Label(root, textvariable=var, relief=GROOVE,  bg="#ffffe0"
            , fg="#2C3E50", width=10).grid(row=5,column=1)
root.mainloop()
