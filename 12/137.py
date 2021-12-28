# import random
# s1=[]
# s2=[]
# s1=set(s1)
# s2=set(s2)
# for i in range(5):
#     a=random.randint(0,100)
#     s1.add(a)
#     s2.add(a)
#     s1.add(random.randint(0,100))
#     s2.add(random.randint(0,100))
# print(s1)
# print(s2)
# s3=[]
# for i in s1:
#     s3.append(i)
# for i in s2:
#     s3.append(i)
# print(set(s3))
# s3=set(s3)
# s3.discard(4)
# print(s3)
# print(max(s3))
# print(min(s3))
# print(len(s3))
# s4=[]
# s4=set(s4)
# for i in s3:
#     s4.add(i)
#     s4.add(random.randint(0,100))
# print(s4)
# s1.clear()
# print(id(s1))

def digit3(a):
    if a>99 and a<1000:
        return True
    else:
        return False
x=int(input("enter 3 digit number: "))
print(digit3(x))


