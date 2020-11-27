import random
import numpy as np
#Tạo 1 số nguyên ngẫu nhiên n trong khoảng [50, 1000] đóng vai trò là số phần tử của List
n=random.randrange(50,1001)
print(n)
#Sinh ngẫu nhiên 1 List các số nguyên trong khoảng [-1000, 1000]
a=list(np.random.randint(-1000,1000, size=n))
print(a)
#Sinh ngẫu nhiên 1 List các số thực tỏng khoảng [-1000.0, 1000.0]
b=list(np.random.uniform(-1000,1000, size=n))
print(b)
print('Ket thuc chuong trinh')