#PASWORD VERIFICATION CODE

# import re
# password_pattern=r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[@#$%])[a-zA-Z0-9@#$%]{8,}$"

# class passwordex(Exception):
#     pass

# def checkpassword(password):
#     if re.search(password_pattern,password):
#         print("password matched..!")
#     else:
#         raise passwordex("incorrect password..!")
# try:
#     password=str(input("enter your password:"))
#     checkpassword(password)
# except passwordex as e:
#     print(e)


#URL VERIFICATION CODE
# import re
# url_pattern=r"http://www.[a-zA-Z0-9.]+\.[a-z]{2,}/"
# url=str(input("enter url: "))
# match=re.search(url_pattern,url)
# if match:
#     print("success..!")
# else:
#     print("failed..!")

# import re
# a="ea@gmail.cou"
# p=r"^[a-zA-Z0-9.]+@[a-z]+\.[a-z]{3,}"
# m=re.search(p,a)
# if m:
#     print("success")
# else:
#     print("failed")

try:
    # a=10/0
    # print(a)
    # b={'name':'eswar','age':22}
    # print(b['nam'])
    # c=[1,2,3,4]
    # print(c[4])
    # print(a)
    file=open("file.txt",'w')
    c=file.read("hello eswar")
    print(c)
except ZeroDivisionError as e:
    print(e)
except KeyError as e:
    print("key value error")
except IndexError as e:
    print(e)  
except NameError as e:
    print(e)
except FileNotFoundError as e:
    print(e)



    

