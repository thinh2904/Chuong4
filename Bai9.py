import os
import time
q=False
while not q:
    a=input("Bạn có muốn tắt máy tính không?(Y/N):  ")
    if a=="Y" or a=="y":
        q=False
        os.system("Shutdown -s")
    time.sleep(30)
print("Kết thúc")
    
    