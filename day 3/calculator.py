import tkinter as tk

def f_string(s):
    global e
    e += s
def c_string():
    global e
    e = ""
    entry.delete(0,"end")   
def calculate(e):
    b = 0
    r = 0
    op =0
    for ch in e:
        if(ch=='+' or ch=='-' or ch=='*' or ch=='/'):
            op = e.find(ch,b)
            n = int(e[b:op])
            if(b==0):
                r = n
            else:
                if(e[b-1]=='+'):
                    r += n
                elif(e[b-1]=='-'):
                    r -= n
                elif(e[b-1]=='*'):
                    r *= n
                elif(e[b-1]=='/'):
                    r /= n
            b = op+1
    n = int(e[b::])
    if(e[op]=='+'):
        r += n
    elif(e[op]=='-'):
        r -= n
    elif(e[op]=='*'):
        r *= n
    elif(e[op]=='/'):
        r /= n
    entry.insert(0,r)

window = tk.Tk()
window.title("Calculator")
window.geometry("500x600")

e = ""
entry = tk.Entry()
entry.grid(row=0,columnspan=4,sticky="ew")

b1 = tk.Button(text="7", command=lambda: f_string("7"))
b1.grid(row=1,column=0,sticky="nsew")
b2 = tk.Button(text="8", command=lambda: f_string("8"))
b2.grid(row=1,column=1,sticky="nsew")
b3 = tk.Button(text="9", command=lambda: f_string("9"))
b3.grid(row=1,column=2,sticky="nsew")
b4 = tk.Button(text="/", command=lambda: f_string("/"))
b4.grid(row=1,column=3,sticky="nsew")

b5 = tk.Button(text="4", command=lambda: f_string("4"))
b5.grid(row=2,column=0,sticky="nsew")
b6 = tk.Button(text="5", command=lambda: f_string("5"))
b6.grid(row=2,column=1,sticky="nsew")
b7 = tk.Button(text="6", command=lambda: f_string("6"))
b7.grid(row=2,column=2,sticky="nsew")
b8 = tk.Button(text="*", command=lambda: f_string("*"))
b8.grid(row=2,column=3,sticky="nsew")

b9 = tk.Button(text="1", command=lambda: f_string("1"))
b9.grid(row=3,column=0,sticky="nsew")
b10 = tk.Button(text="2", command=lambda: f_string("2"))
b10.grid(row=3,column=1,sticky="nsew")
b11 = tk.Button(text="3", command=lambda: f_string("3"))
b11.grid(row=3,column=2,sticky="nsew")
b12 = tk.Button(text="-", command=lambda: f_string("-"))
b12.grid(row=3,column=3,sticky="nsew")

b13 = tk.Button(text="C", command=c_string)
b13.grid(row=4,column=0,sticky="nsew")
b14 = tk.Button(text="0", command=lambda: f_string("0"))
b14.grid(row=4,column=1,sticky="nsew")
b15 = tk.Button(text="=", command=lambda: calculate(e))
b15.grid(row=4,column=2,sticky="nsew")
b16 = tk.Button(text="+", command=lambda: f_string("+"))
b16.grid(row=4,column=3,sticky="nsew")



window.mainloop()