def digit3(a):
    if a>99 and a<1000:
        return True
    else:
        return False
# x=int(input("enter 3 digit number: "))
def digitsum(a):
    return (a%10+a//10%10+a//100)
# if digit3(x):
#     print(digitsum(x))
# num=int(input("enter number: "))
# word=input("enter word: ")
def wword(a,b):
    for i in range(b):
     print(a)
# wword(word,num)
def ssum(a):
    s=0
    for i in range(0,(a+1)):
        s+=i
    print(s)
# for i in range(5):
#     x=int(input("enter number: "))
#     ssum(x)
def between(a,b):
    for i in range(a,(b+1)):
        print(i, end=" ")
# q=int(input("enter number1: "))
# e=int(input("enter number2: "))
def bigger(a,b):
    if a<b:
        return True
    if a>b:
        return False
# if bigger(q,e):
#     between(q,e)
# if not bigger(q,e):
#     between(e,q)
# v=int(input("enter number Alon: "))
# c=int(input("enter number 2: "))
def power(a,b):
    z=1
    for i in range(b):
        z=z*a
    print(z)
# power(v,c)
def age(a):
    if a>0 and a<19:
        return "child"
    if a>18 and a<61:
        return "adult"
    if a>60 and a<121:
        return "senior"
# for i in range(5):
#     x1=int(input("enter age: "))
#     print(age(x1))
def passgrade(a):
    if 70<=a and a<=100:
        return True
    else:
        return False
# for i in range(5):
#     x2=int(input("enter grade: "))
#     if passgrade(x2):
#         print("passed")
#     if not passgrade(x2):
#         print("failed")
def l40(a:list):
    for i in range(2,41,2):
        a.append(i)
    return a
x3=[]
print(l40(x3))
def lrandom(a:list):
    import random
    for i in range(20):
        a.append(random.randint(1,100))
    return a
h=[]
# print(lrandom(h))
def ccount(a):
 d=0
 for i in h:
  if i==a:
   d=d+1
 a=d
 return a
# y=int(input("enter number: "))
# print(ccount(y))
def maxdex(a:list):
    print(a.index(max(a))+1)
# maxdex(h)
def studentgrade(a,b:list):
    for i in range(a):
        o=input("enter grade: ")
        b.append(o)
    print(b)
def gradeaverage(a:list):
    b=0
    for i in a:
        b=b+int(i)
    print(b/len(a))
# p=[]
# studentgrade(4,p)
# gradeaverage(p)




