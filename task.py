from tkinter import *

def show_message():
    x = int(txt.get())
    x = x * 74
    lab2["text"] = str(x) + " RUB"


root = Tk()
root.title("converter")
root.geometry("250x250+200+150")
root.minsize(200, 200)

lab = Label(text="Usd to RUB")
lab.pack(anchor=CENTER)

txt = Entry(justify=RIGHT)
txt.pack(pady= 20)

lab2 = Label(text="")
lab2.pack(anchor=CENTER)

btn = Button(text ="Convert",command=show_message)
btn.pack(anchor=CENTER, pady=50)




root.mainloop()