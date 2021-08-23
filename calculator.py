from tkinter import *

def click(event):
    global scvalue
    text = event.widget.cget("text")
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())
            except Exception as e:
                value = "Invalid Option"
                screen.update()

        scvalue.set(value)
        screen.update()
    elif text == "C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()
root = Tk()

root.configure(background="grey")
root.geometry("490x840")
root.title("Calculator")
root.wm_iconbitmap("calculator.ico")
scvalue = StringVar()
scvalue.set('')
screen = Entry(root, textvar=scvalue, font="lucida 40 bold", fg="grey", bg="white")
screen.pack(fill=X, ipadx=8, pady=10, padx=10)



frame = Frame(root, bg="grey")

b = Button(frame, text="9", font="lucida 35 bold", padx=28, pady=10, fg="grey")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(frame, text="8", font="lucida 35 bold", padx=28, pady=10, fg="grey")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(frame, text="7", font="lucida 35 bold", padx=28, pady=10, fg="grey")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

frame.pack()

frame = Frame(root, bg="grey")

b = Button(frame, text="6", font="lucida 35 bold", padx=28, pady=10, fg="grey")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(frame, text="5", font="lucida 35 bold", padx=28, pady=10, fg="grey")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(frame, text="4", font="lucida 35 bold", padx=28, pady=10, fg="grey")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

frame.pack()

frame = Frame(root, bg="grey")

b = Button(frame, text="3", font="lucida 35 bold", padx=28, pady=10, fg="grey")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(frame, text="2", font="lucida 35 bold", padx=28, pady=10, fg="grey")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(frame, text="1", font="lucida 35 bold", padx=28, pady=10, fg="grey")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

frame.pack()

frame = Frame(root, bg="grey")

b = Button(frame, text="0", font="lucida 35 bold", padx=31, pady=10, fg="grey")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(frame, text="-", font="lucida 35 bold", padx=31, pady=10, fg="grey")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(frame, text="*", font="lucida 35 bold", padx=31, pady=10, fg="grey")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

frame.pack()

frame = Frame(root, bg="grey")

b = Button(frame, text="/", font="lucida 35 bold", padx=32, pady=10, fg="grey")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(frame, text="%", font="lucida 35 bold", padx=21, pady=10, fg="grey")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(frame, text="=", font="lucida 35 bold", padx=29, pady=10, fg="grey",bg="powder blue")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

frame.pack()

frame = Frame(root, bg="grey")

b = Button(frame, text="+", font="lucida 35 bold", padx=50, pady=10, fg="grey")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(frame, text="AC", font="lucida 35 bold", padx=66, pady=10, fg="grey", bg="powder blue")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)



frame.pack()

root.mainloop()

