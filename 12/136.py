# import random

# l=[random.randint(0,100) for i in range(10)]
# print(l)
# tuple(l)
# # print(l)
# # l+=int(input("enter number: ")),
# # print(l)
# list(l)
# del l[6]
# print(l)

# o=7,4,64,3,3,6,5,4,
# print(o)
# o=list(o)
# del o[0]
# print(o)

dic1={1:10,2:20}
dic2={3:30,4:40}
dic3={5:50,6:60}
dic1.update(dic2)
dic1.update(dic3)
print(dic1)