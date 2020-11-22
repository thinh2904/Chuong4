import random
n=int(input("Nhập n="))
list=random.sample(range(-100,100),n)
print("list=",list)
max=list[1]
for i in range(n):
    if max<= list[i]:
        max=list[i]
print("Max=",max)