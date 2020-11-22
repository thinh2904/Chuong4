import random
n=int(input("Nhập n="))
list=random.sample(range(-100,100),n)
print("list=",list)
min=list[1]
for i in range(n):
    if min>= list[i]:
        min=list[i]
print("Min=",min)