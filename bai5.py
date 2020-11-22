import math
list=[1,2,3,-5,0.1,0]
#Thực hiện lặp truy xuất đến từng phần tử trong List và in giá trị của từng phần tử ra màn hình
for i in range(len(list)):
    print("List[",i,"] =",list[i])
#Thực hiện lặp truy xuất đến từng phần tử trong List và thực hiện tính logarith của từng phần tử và in giá trị đó ra màn hình
for i in range(len(list)):
    if list[i]>0:
        print("Log(",list[i],") =",math.log(list[i]))
print("Kết thúc chương trình")