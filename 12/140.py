class Bank_Account:
    def __init__(self,name,acc_num,balance=0):
        self.name=name
        self.acc_num=acc_num
        self.balance=balance

    def statement(self):
        print(self.name)
        print(self.acc_num)
        print(self.balance)

    def withdraw(self,b):
        self.balance-=b


# acc1=Bank_Account("alon",12233,10000)
# acc1.statement()

class Student:
    def __init__(self,name,id,grade):
        self.name=name
        self.id=id
        self.grade=grade

    def gradecheck(self):
        if self.grade>70 and self.grade<101:
            return True
        if 0<=self.grade<70:
            return False

    def updategrade(self,a):
        self.grade=self.grade*(a/100+1)
        if self.grade>=100:
            self.grade=100
        return self.grade

    def show(self):
        print(self.name)
        print(self.id)
        print(self.grade)

# s1=Student("alon",5393,90)
# s1.gradecheck()
# s1.updategrade(30)
# s1.show()

class Person:
    def __init__(self,name,age,numkids):
        self.name=name
        self.age=age
        self.numkids=numkids

    def show1(self):
        print(self.name)
        print(self.age)
        print(self.numkids)

    def haschildren(self):
        if self.numkids>0:
            return True
        if self.numkids==0:
            return False
    def agegroup(self):
        if 0<self.age<19:
            return "Child"
        if 18<self.age<61:
            return "Adult"
        if 60<self.age<121:
            return "Senior"
# pers1=Person("alon",22,0)
# pers1.show1()
# print(pers1.haschildren())
# print(pers1.agegroup())

class Circle:
    def __init__(self,radius):
        self.radius=radius
        self.pi=3.14

    def area(self):
       ar=self.radius*self.radius*self.pi
       return ar

    def circumf(self):
        ci=self.radius*2*self.pi
        return ci
# c1=Circle(4)
# print("area:",c1.area())
# print("circumfrence:",c1.circumf())

class Hardisk:
    def __init__(self,space,usedspace=0,numfiles=0):
        self.usedspace=usedspace
        self.numfiles=numfiles
        self.space=space
        self.v=space
        self.space=(self.space-self.usedspace)

    def __repr__(self):
        return (f"Space:{self.v}GB   Used Space:{self.usedspace}GB   Space left:{self.space}GB   Number of files:{self.numfiles}")

    def show2(self):
        print("GB of Empty Space:",self.space)
        print("GB of Used Space:",self.usedspace)
        print("Number of Files:", self.numfiles)

    def freespace(self):
        print(self.space)

    def addflile(self,a):
        if (self.space-a)>0:
             self.numfiles+=1
             self.usedspace+=a
             self.space-=a
        else:
            print("cant add file, not enough space")

    def delfile(self,a):
        self.numfiles-=1
        self.usedspace-=a
        self.space+=a
        if self.usedspace<0:
            self.usedspace=0
            self.space=self.v

# h1=Hardisk(250,40,3)
# print(h1)
# h1.addflile(2)
# h1.addflile(5)
# h1.addflile(8)
# h1.addflile(90)
# h1.addflile(24)
# h1.delfile(30)
# print(h1)

class Course:
    def __init__(self,cname,cnum,studnum,studmax):
        self.cname=cname
        self.cnum=cnum
        self.studnum=studnum
        self.studmax=studmax

    def __str__(self):
       return (f"course name:{self.cname}   course number:{self.cnum}   number of students in course:{self.studnum}   max number of students in course:{self.studmax}")

    def studnumleft(self):
        return (self.studmax-self.studnum)

    def addstud(self,a):
        if ((self.studnum+a)<self.studmax):
            self.studnum+=a
        else:
            print("cant add more students")

# clas1=Course("A1",12,23,32)
# print(clas1)
# clas1.addstud(5)
# print(clas1.studnumleft())
# print(clas1)

class Animal:
    def __init__(self):
        self.hung=5
        self.energ=5

    def __str__(self):
        return (f"Hunger:{self.hung}   Energy:{self.energ}")

    def eat(self,a):
        b=self.hung
        self.hung=(self.hung-(a/50))
        if self.hung<0:
            self.energ=(self.energ-b/2)
            if self.energ<0:
                self.energ=0
            print("The animal is full and did not finish eating")
            self.hung=0
        else:
            self.energ=(self.energ-(a/100))

    def play(self,a):
        b=self.energ
        c=self.hung
        self.energ=(self.energ-a/5)
        if self.energ<0:
            print("game ended because the animal ran out of energy")
            self.hung=(self.hung+b)
            self.energ=0
        else:
            self.hung=self.hung+a/5
        if self.hung>10:
            self.energ=-(self.energ-c)
            self.hung=10

    def rest(self,a):
        b=self.hung
        c=self.energ
        self.energ=(self.energ+a/20)
        if self.energ>10:
            self.hung=(self.hung+c/1.5)
            self.energ=10
            print("Animal finished resting and wants to play")
        else:
            self.hung=(self.hung+a/30)

# tiger=Animal()
# print(tiger)
# tiger.rest(1200)
# print(tiger)
# tiger.play(50)
# print(tiger)
# tiger.eat(4900)
# print(tiger)
# x=input("enter Animal: ")
# x=Animal()
# b=int(input("enter 0or1or2or3. Alon=eat 2=play 3=rest 0=end:"))
# if b == Alon:
#     c=int(input("number of grams to eat:"))
#     x.eat(c)
# if b == 2:
#     d=int(input("number of minutes to play: "))
#     x.play(d)
# if b == 3:
#     e=int(input("number of minutes to rest: "))
#     x.rest(e)
# while b!=0:
#     b=int(input("enter 0or1or2or3. Alon=eat 2=play 3=rest 0=end:"))
#     if b==Alon:
#         c=int(input("number of grams to eat:"))
#         x.eat(c)
#     if b==2:
#         d=int(input("number of minutes to play: "))
#         x.play(d)
#     if b==3:
#         e=int(input("number of minutes to rest: "))
#         x.rest(e)
# print(x)

class Loto:
    def __init__(self):
        self.l=1
        self.u=45
        self.lis=[]
        self.max=self.maxwinsum()
        self.win=0

    def rando(self):
        for i in range(6):
            import random
            b=random.randint(self.l,self.u)
            self.lis.append(b)
        return self.lis

    def maxwinsum(self):
        a=int(input("Enter max winning sum: "))
        self.max=a
        return a

    def see(self):
        print(self.lis)

    def guess(self,a):
        b=self.lis.copy()
        if a in b:
            self.win+=1
            b.remove(a)

    def check(self):
        if self.win<=1:
            print("U lost")
        if 1<self.win<=5:
            print("U won",(self.win*self.max)/6,"$")
        if self.win==6:
            print("U won",self.max,"$")

# alon=Loto()
# alon.rando()
# for i in range(6):
#     q=int(input("Guess a number between Alon and 45: "))
#     if q<Alon or q>45:
#         print("illegal number")
#         break
#     alon.guess(q)
# alon.see()
# alon.check()

class Bus:
    def __init__(self,n):
        self.sits=[]
        self.n=n

    def constructor(self):
        for i in range(self.n):
            self.sits.append("free")

    def geton(self,a):
        if "free" in self.sits:
           b=self.sits.index("free")
           self.sits[b]=a
        else:
            print("Bus is full, passenger",a,"cant get on bus")
    def getoff(self,a):
        if a in self.sits:
            c=self.sits.index(a)
            self.sits[c]="free"
        else:
            print("passenger",a,"is not on the bus")

bus1=Bus(5)
bus1.constructor()
print(bus1.sits)
print(bus1.n)
r=1
while r==1 or r==2:
    r=int(input("press Alon to get a passenger on or press 2 to remove passenger: "))
    if r==1:
        p1=input("Enter passenger name: ")
        bus1.geton(p1)
    if r==2:
        p2=input("Enter passenger name: ")
        bus1.getoff(p2)
print(bus1.sits)
print(bus1.n)




