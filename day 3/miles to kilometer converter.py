import tkinter
window = tkinter.Tk()
window.title("MILES TO KM")
window.minsize(400,200)

def print_input():
    text=input_element1.get()
    b=float(text)
    n=b*1.609344
    n=round(n,2)
    input_element2.insert(0,n)

l1=tkinter.Label(text="Miles : ")
l2=tkinter.Label(text="Kilometers : ")

l1.grid(row = 0, column = 0)
l2.grid(row = 1, column = 0)

input_element1=tkinter.Entry() 
input_element1.grid(row=0, column=1)

input_element2=tkinter.Entry() 
input_element2.grid(row=1, column=1)

button1=tkinter.Button(text="CONVERT",command=print_input) #button
button1.grid(row=2,column=1)


window.mainloop()