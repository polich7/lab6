from queue import Queue
from tkinter import *
from threading import Thread


def foo(q, n):
    while TRUE:
        item = q.get()
        if item is None:
            break
        print("count: %d/%d " % (n, item))


def click_button():
    q = Queue(5)
    th1 = Thread(target=foo, args=(q, 1))
    th2 = Thread(target=foo, args=(q, 2))
    th1.start()
    th2.start()

    for i in range(50):
        q.put(i)

    q.put(None)
    q.put(None)
    th1.join()
    th2.join()


root = Tk()
root.title("GUI на Python")
root.geometry("300x250")

btn = Button(text="start", background="#555", foreground="#ccc",
             padx="20", pady="8", font="16", command=click_button)
btn.pack()
root.mainloop()


