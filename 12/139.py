b=[3,5,2,5,3]
def len1(a:list):
    return len(a)

# print(len1(a1))

def count1(a:list,b):
    return a.count(b)

# print(count1(a1,4))

def max1(a,b,c):
    numbers=[a,b,c]
    return max(numbers)

print(max1(8,2,76))

def sum1(a:list):
    c=1
    for i in a:
        c=i+c
    return c
print(sum1(b))

def mult(a:list):
    c = 1
    for i in a:
        c = i * c
    return c
print(mult(b))
