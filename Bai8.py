import smtplib
import getpass
print("Đăng nhập vào email của bạn")
email=input("Tài khoản:")
password=getpass.getpass("Mật khẩu:")
address=input("Địa chỉ email muốn gửi:")
mess=input("Nội dung:")
spam=smtplib.SMTP("smtp.gmail.com", 587)
spam.starttls()
spam.login(email,password)
n=int(input("Số lần gửi:"))
for i in range(n):
    spam.sendmail(email,address,mess)
print("Hoàn thành nhiệm vụ")