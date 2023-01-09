from tkinter import *
from PIL import ImageTk,Image
import pyqrcode


root = Tk()
canvas = Canvas(root,width=400,height=600)
canvas.pack()

def generate():
    link_name = name_entry.get()
    link = link_entry.get()
    file_name = link_name + ".png"
    url = pyqrcode.create(link)
    url.png(file_name,scale=8)
    image = ImageTk.PhotoImage(Image.open(file_name))
    image_label = Label(image=image)
    image_label.image = image
    canvas.create_window(200,450,window=image_label)

label1 = Label(root,text="QR CODE Generator",fg="blue",font=('Arial',30))
label2 = Label(root,text="Name")
label3 = Label(root,text="Link")

name_entry = Entry(root)
link_entry = Entry(root)

button = Button(text="Generate" ,command=generate)

canvas.create_window(200,90,window=label1)
canvas.create_window(200,140,window=label2)
canvas.create_window(200,190,window=label3)
canvas.create_window(200,210,window=link_entry)
canvas.create_window(200,160,window=name_entry)
canvas.create_window(200,250,window=button)
root.mainloop()