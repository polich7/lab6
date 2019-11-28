from queue import Queue
from tkinter import *  # графический интерфейс
from threading import Thread
# чудом сдали
# кнопка 1 - вывод на консоль
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

    for i in range(500000):
        q.put(i)

    q.put(None)
    q.put(None)
    th1.join()
    th2.join()

# кнопка 2 - вывод в файл
def proc(file):
    with open(file) as f:
        for line in f:
            lst = line.split()
            print(lst)

def click_button1():
    q1 = Queue()
    p1 = Thread(target=proc, args=('f1.txt',))
    p2 = Thread(target=proc, args=('f2.txt',))
    p1.start()
    p2.start()
    p1.join()
    p2.join()

# параметры окна вывода
root = Tk()
root.title("GUI на Python")
root.geometry("300x250")

btn = Button(text="start", background="#555", foreground="#ccc",
             padx="20", pady="8", font="16", command=click_button)
btn.pack()
btn1 = Button(text="start1", background="#555", foreground="#ccc",
             padx="20", pady="8", font="16", command=click_button1)
btn1.pack(side=BOTTOM)
root.mainloop()



