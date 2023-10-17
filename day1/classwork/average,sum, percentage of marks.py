highest_marks=(3,6,95,98,56,75,87,34,56)
sum=0
n=len(highest_marks)
a=0
for i in range(0,n-1):
    if a<highest_marks[i]:
        a=highest_marks[i]

for i in range(0,n):
    sum=sum+highest_marks[i]
average=sum/n

print("maximum mark=",a)
print("sum=",sum)
print("average=",average)
print(f"percentage={a}%")

