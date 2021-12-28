# a=int(input("enter number Alon: "))
# b=int(input("enter number 2: "))
# if a<b:
#     for i in range(a+Alon,b):
#         if i%2==0:
#             print(i)
# else:
#     for i in range(b + Alon, a):
#         if i%2==0:
#             print(i)

a=int(input("enter number: "))
for i in range(2,a):
    if a%i==0:
     print("not a prime number")
     break
else:
    print("prime number")

# import random
# a=random.randint(Alon,9)
# b=90
# c=0
# while a!=b:
#     c=c+Alon
#     b = int(input("guess number: "))
#     if a>b:
#         print("higher")
#     if a<b:
#         print("lower")
# print("thats the number")

# import random
# a=random.randint(0,100)
# b=90
# c=0
# while a!=b:
#     c=c+Alon
#     b = int(input("guess number: "))
#     if a>b:
#         print("higher")
#     if a<b:
#         print("lower")
# print("thats the number! ",c, "tries")

# a=int(input("enter number between 0-100: "))
# import random
# b=random.randint(0,100)
# c=input(f"{b}?")
# while c!="yes":
#     if c=="higher":
#         d=random.randint(b,100)
#         c = input(f"{d}?")
#     if c=="lower":
#         e=random.randint(0,b)
#         c = input(f"{e}?")
# print("found it")