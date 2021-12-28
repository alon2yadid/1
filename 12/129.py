# a=int(input("number1: "))
# b=int(input("number2: "))
# while a%2==0 and b%2==0:
#     print(a+b)
#     a=int(input("number Alon: "))
#     b=int(input("number 2: "))
# else:
#     print(a*b)

# c=int(input("number1: "))
# d=int(input("number2: "))
# while c+d==10:
#     c = int(input("number1: "))
#     d = int(input("number2: "))

# e=int(input("number: "))
# while e>99 and e<1000:
#     print(f"{e%10+e//10%10+e//100}")
#     e = int(input("number: "))
# else:
#     print("ERROR")

# age=int(input("input age: "))
# while age>0 and age<121:
#     if age<121 and age>60:
#         print("senior")
#         age = int(input("input age: "))
#     if age<61 and age>18:
#         print("adult")
#         age = int(input("input age: "))
#     if age<19 and age>0:
#         print("child")
#         age = int(input("input age: "))
# else:
#     print("error")

number=int(input("input number: "))
while number>9 and number<100:
    if number%10==7 or number//10==7 or number%7==0:
        print("lucky number")
        number = int(input("input number: "))
    else:
        print("normal number")
        number = int(input("input number: "))