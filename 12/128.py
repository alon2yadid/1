# a=int(input())
# b=int(input())
# if (a+b)%2==1:
#     print("odd")
# else:
#     print("even")


# s=int(input())
# if (s//100)>=1 and (s//1000)<1:
#     print(f"{s//100}{s//10%10}{s%10}")
# else:
#     print("error")

# age=int(input("input age: "))
# if age<121 and age>60:
#     print("senior")
# else:
#     if age>18 and age<61:
#         print("adult")
#     else:
#         if age>0 and age<19:
#             print("child")

# d=int(input())
# f=int(input())
# if (d>f):
#     print(d-f)
# else:
#     print(f-d)

# g=int(input())
# h=int(input())
# if g%2==0 and h%2==0:
#     print(g+h)
# else:
#     print(g*h)

# j=int(input())
# k=int(input())
# if k+j==10:
#     print("sum is 10")
# else:
#     print("sum is not 10")

day=int(input("input day: "))
month=int(input("input month: "))
year=int(input("input year: "))
if (day>0 and day<32) and (month<13 and month>0) and (year>1949 and year<2021):
    print(f"{day}/{month}/{year//10%10}{year%10}")
else:
    print("invalid date")

# q=int(input())
# w=int(input())
# e=int(input())
# if (q-w)>0 and (q-e)>0:
#     print(q)
# else:
#     if (w-q)>0 and (w-e)>0:
#         print(w)
#     else:
#         if (e-w)>0 and (e-q)>0:
#             print(e)

# r=input("number of computers: ")
# if r=="":
#     print(15)
# else:
#     print(r)
#     print(f"numnber of computers tomorrow:{2*int(r)}")



