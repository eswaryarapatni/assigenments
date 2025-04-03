#reverse a string

# def palindrom_check():
#     word=str(input("enter a number:"))
#     strn=""
#     for i in range(len(word)):
#       strn+=word[-(i+1)]
#     if strn==word:
#           print(word," is a palindrom!!")
#     else:
#           print("not a palindrom..!")
# palindrom_check()

#prime check

# a=190
# count=0
# for i in range(2,a//2):
#     if a%i==0:
#        count+=1
#        break
#     else:
#         continue
    
# if count!=0:
#     print("not a prime")
# else:
#     print("prime")

#fibonici series(0,1,1,2,3,5,8,13)


# fs=[0,1]
# for i in range (2,10):
#     next=fs[-1]+fs[-2]
#     fs.append(next)
# print(fs)


#evev_odd_check

# def even_odd(num):
#     if num%2==0:
#         print("even")
#     elif num%2!=0:
#         print("odd")

# even_odd(0)

# for i in range(0,100):
#     if i%2==0:
#         print("@")
#     else:
#         print(i)
    
    
# coll=[9,3,4,5,2]
# for i in coll:
#     print(i**2)
    
names={"s1":"eswar","s2":"uday","s3":"yuvaraj","s4":"venkat"}
for i,j in names.items():
    print(i,":",j)