import tkinter


def add_com():
    a=ll1.get()
    listbox.insert(0,a)
    button
def delete_com():
    index = listbox.curselection()
    listbox.delete(index)
    
    
    
window = tkinter.Tk()
window.title("TO DO LIST")
window.minsize(400,500)

ll1=tkinter.Entry()
ll1.grid(padx=10,pady=10)

l1=tkinter.Label(text="TO DO LIST : ")
l1.grid(row=1,column=0)

listbox = tkinter.Listbox()
listbox.grid(row=2,column=0)




button1=tkinter.Button(text="ADD",command=add_com) 
button1.grid(row=0,column=1)
button2=tkinter.Button(text="DELETE",command=delete_com) 
button2.grid(row=3,column=0)


window.mainloop()