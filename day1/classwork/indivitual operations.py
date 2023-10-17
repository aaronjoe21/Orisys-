def add(num1,num2):
    print(num1+num2)

def sub(num1,num2):
    print(num1-num2)

def mul(num1,num2):
    print(num1*num2)
    
def div(num1,num2):
    print(num1/num2)


num1=int(input("Enter a number:"))
num2=int(input("Enter 2nd number:"))
print("CHOOSE OPTION: \n1)add \n2)subtract \n3)multiply \n4)divide \n5)exit")
while True:
    
    fun=input("Enter operations:")
    if fun=="1":
        add(num1,num2)
        
    elif fun=="2":
        sub(num1,num2)
    elif fun=="3":
        mul(num1,num2)
    elif fun=="4":
        div(num1,num2)
    elif fun=="5":
        break
    else:
        print("invalid")
        
        
