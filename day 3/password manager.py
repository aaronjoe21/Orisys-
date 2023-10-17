import tkinter


window = tkinter.Tk()
window.title("PASSWORD MANAGER")
window.minsize(400,200)

window.configure(bg='blue')


def print_int():
    with open('passwords.txt', 'a') as file:
        text=ll1.get()
        text1=ll2.get()
        text2=ll3.get()
        file.write(f"{text} | {text1} | {text2}\n")
        label1=tkinter.Label(text='SUCCESSFULLY SAVED',font=("Times New Roman",10))
        label1.grid(row=4,column=0)

l1=tkinter.Label(text="WEBSITE : ")
l1.grid(row=0,column=0)
l2=tkinter.Label(text="USERNAME: ")
l2.grid(row=1,column=0)
l3=tkinter.Label(text="PASSWORD : ")
l3.grid(row=2,column=0)

ll1=tkinter.Entry() 
ll1.grid(row=0, column=1)
ll2=tkinter.Entry() 
ll2.grid(row=1, column=1)
ll3=tkinter.Entry() 
ll3.grid(row=2, column=1)


button1=tkinter.Button(text="SAVE",command=print_int) 
button1.grid(row=3,column=1)



window.mainloop()
