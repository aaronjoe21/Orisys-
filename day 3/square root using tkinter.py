import tkinter
window = tkinter.Tk()
window.title("SQUARE")
window.minsize(400,200)

def print_input():
    text=input_element.get()
    n=int(text)
    b=n**2
    print(b)
    label1.config(text=b)
    
label1=tkinter.Label(text="THE SQUARE IS",font=("Times New Roman",10))
label1.pack(side="bottom")

label2=tkinter.Label(text="ENTER A NUMBER",font=("Times New Roman",10))
label2.pack()

input_element=tkinter.Entry() #input box
input_element.pack()

button1=tkinter.Button(text="SUBMIT",command=print_input) #button
button1.pack()




window.mainloop()