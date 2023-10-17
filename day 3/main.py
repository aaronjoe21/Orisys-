import tkinter

window = tkinter.Tk()
window.title("My first GUI application")
window.minsize(400,200) #for defining the dimensions of the window
'''
label1=tkinter.Label(text="How you doing?")
label1.pack()
'''

label2=tkinter.Label(text="How you doing?",font=("Times New Roman",10))
label2["text"]= "Hey" #method1
label2.config(text="Hey there")#method 2
label2.pack()

'''
label2.place(x=40,y=53) #To place the text
'''

def print_hello():
    label2.config(text="Hey there, the title was changed")
'''
button1=tkinter.Button(text="CLICK ME",command=print_hello)
'''
button1=tkinter.Button(text="CLICK ME",command=print_hello)
button1.pack()
window.mainloop()