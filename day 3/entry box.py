import tkinter
window = tkinter.Tk()
window.title("INPUT BOX")
window.minsize(400,200)

def print_input():
    n=input_element.get()
    label1.config(text=n)

label1=tkinter.Label(text="YOUR NAME IS")
label1.pack(side="bottom")
    
input_element=tkinter.Entry() #input box
input_element.pack()


button1=tkinter.Button(text="SUBMIT",command=print_input) #button
button1.pack()




window.mainloop()
