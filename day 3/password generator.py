import random
import tkinter


window = tkinter.Tk()
window.title("PASSWORD GENERATION")
window.minsize(400,200)
window.configure(bg='blue')



label1=tkinter.Label(text='''
CONDITIONS:
1) MINIMUM 8 CHARACTERS
2) MIX OF LETTERS, SYMBOLS AND DIGITS
3) MINIMUM OF ONE OF EACH''',font=("Times New Roman",10))
label1.grid(row=0,column=0)

               
               
def print_int():
    letters= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    numbers=['0','1','2','3','4','5','6','7','8','9']

    symbols=['!','@','#','$','%','&','*','(',')','+','=','-','?']
    
    text=ll1.get()
    a=int(text)
    text=ll2.get()
    b=int(text)
    text=ll3.get()
    c=int(text)
    
    
    password=[]
    for i in range(0,a):
        password+=random.choice(letters)
    for i in range(0,b):
        password+=random.choice(numbers)
    for i in range(0,c):
        password+=random.choice(symbols)
    random.shuffle(password)
    ll4.delete(0,'end')
    ll4.insert(0,password)

l1=tkinter.Label(text="NO OF LETTERS : ")
l1.grid(row=1,column=0)
l2=tkinter.Label(text="NO OF NUMBERS: ")
l2.grid(row=2,column=0)
l3=tkinter.Label(text="NO OF SYMBOLS : ")
l3.grid(row=3,column=0)
l4=tkinter.Label(text="NEW PASSWORD:")
l4.grid(row=4,column=0)


ll1=tkinter.Entry() 
ll1.grid(row=1, column=1)
ll2=tkinter.Entry() 
ll2.grid(row=2, column=1)
ll3=tkinter.Entry() 
ll3.grid(row=3, column=1)
ll4=tkinter.Entry()
ll4.grid(row=4,column=1)
button1=tkinter.Button(text="GENERATE",command=print_int) 
button1.grid(row=5,column=1)




window.mainloop()




