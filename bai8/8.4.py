print('sinh vien: ho duc minh')
print('mssv:235752021610038')
print('##########')
from tkinter import *

window = Tk()
window.title("Welcome to LikeGeeks app")
window.geometry('350x200')
lbl = Label(window, text="Hello")
lbl.grid(column=0, row=0)
def clicked():
    lbl.configure(text="Button was clicked !!")
btn = Button(window, text="Click Me", command=clicked)
btn.grid(column=1, row=0)
def on_key_press(event):
    lbl.configure(text=f"Key {event.char} pressed")
window.bind("<Key>", on_key_press)
window.mainloop()
