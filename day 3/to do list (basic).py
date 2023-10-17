import tkinter


window = tkinter.Tk()
window.title("TO DO LIST")
window.minsize(400,500)


def clear_c1():
    ll2.delete(0,'end')
def clear_c2():
    ll3.delete(0,'end')
def clear_c3():
    ll4.delete(0,'end')
def clear_c4():
    ll5.delete(0,'end')
def clear_c5():
    ll6.delete(0,'end')


def print_n():
    text=ll1.get()
    text1=ll2.get()
    text2=ll3.get()
    text3=ll4.get()
    text4=ll5.get()
    text5=ll6.get()
    if text1=='':
        ll2.insert(0,text)
    elif text2=='':
        ll3.insert(0,text)
    elif text3=='':
        ll4.insert(0,text)
    elif text4=='':
        ll5.insert(0,text)
    elif text5=='':
        ll6.insert(0,text)
    else:
        l7=tkinter.Label(text="NO SPACE. REMOVE SOME LIST ")
        l7.grid(row=7,column=0)


ll1=tkinter.Entry(width=50,)
ll1.grid(padx=10,pady=10)

l1=tkinter.Label(text="TO DO LIST : ")
l1.grid(row=1,column=0)
ll2=tkinter.Entry(width=50)
ll2.grid(padx=10,pady=10)
ll3=tkinter.Entry(width=50)
ll3.grid(padx=10,pady=10)
ll4=tkinter.Entry(width=50)
ll4.grid(padx=10,pady=10)
ll5=tkinter.Entry(width=50)
ll5.grid(padx=10,pady=10)
ll6=tkinter.Entry(width=50)
ll6.grid(padx=10,pady=10)




button1=tkinter.Button(text="ADD",command=print_n) 
button1.grid(row=0,column=1)
button2=tkinter.Button(text="REMOVE",command=clear_c1) 
button2.grid(row=2,column=1)
button3=tkinter.Button(text="REMOVE",command=clear_c2) 
button3.grid(row=3,column=1)
button4=tkinter.Button(text="REMOVE",command=clear_c3) 
button4.grid(row=4,column=1)
button5=tkinter.Button(text="REMOVE",command=clear_c4) 
button5.grid(row=5,column=1)
button6=tkinter.Button(text="REMOVE",command=clear_c5) 
button6.grid(row=6,column=1)






window.mainloop()