# num=[10,15,20,25,30,35,40]
# for i in num:
#     if i%2==0:
#       print(i)

# no=int(input('enter the no of students:'))
# name=input('enter the name:')
# marks=int(input('enter the marks:'))
# name1=input('enter the name:')
# marks1=int(input('enter the marks:'))
# name2=input('enter the name:')
# marks2=int(input('enter the marks:'))
# d={name:marks,
# name1:marks1,
# name2:marks2
#  }
# for i,j in d.items():
#    print(i,'=',j)

# name=input('enter the name:')
# age=int(input('enter the age:'))
# location=input('enter the location:')
# class Personal_details:
#     n=name
#     a=age
#     l=location
#     def m1(self):
#         print()
# d = Personal_details()
# print(d.n)
# print(d.a)
# print(d.l)
# d.m1()

# name=input('enter the name:')
# age=int(input('enter the age:'))
# location=input('enter the location:')
# class Personal_details:
#     def m1(self,name,age,location):
#         print('name is',name)
#         print('age is',age)
#         print('location is',location)
# d = Personal_details()
# d.m1(name,age,location)

# n1=int(input('enter the n1 value:'))
# n2=int(input('enter the n2 value:'))
# class MathOperations:
#     sum=n1+n2
#     difference=n1-n2
#     product=n1*n2
#     quotient=n1/n2
#     def m1(self,sum,difference,product,quotient):
#         print('sum is',sum)
#         print('difference is',)
#         print('product is',n1*n2)
#         print('quotient is',n1/n2)
# d=MathOperations(n1,n2)
# d.m1(sum)

# z=30
# class A:
#     y=20
#     def m1(self):
#         x=10
#         print(x)
#         print(A.y)
# print(z)
# print(A.y)
# d = A()
# d.m1()

# class Training_Institute:
#     def place(self):
#         print('bgl')
#     def course(self):
#         print('python')
# class Training_Institute1:
#     def name(self):
#         print('sumanth')
#     def year(self):
#         print('2025')
# d=Training_Institute()
# d.place()
# d.course()
# p=Training_Institute1()
# p.name()
# p.year()

# class S:
#     def __init__(self):
#         print('hi')
#     def m1(self):
#         print('hello')
# d=S()
# d.m1()

# i=int(input('enter the id:'))
# n=input('enter the name:')
# c=input('enter the course:')
# class Info:
#     def __init__(self,id,name,course):
#         print('id is:',id)
#         print('name is:',name)
#         print('course is:',course)
#     def m1(self):
#         print(self.id)
#         print(self.name)
#         print(self.course)
#         # print('id is:',id)
#         # print('name is:',name)
#         # print('couirse is:',course)
#
#
# d=Info(1234,'suman','python')
# d.m1()
# e=Info(7894,'hari','java')
# e.m1()
# r=Info(4561,'nithin','vlsi')
# r.m1()
# n1=10
# n2=20
# class mathsoperation:
#     def __init__(self,n1,n2):
#         self.n1=n1
#         self.n2=n2
#     def add(self):
#         print(self.n1+self.n2)
#     def sub(self):
#         print(self.n1-self.n2)
#     def mul(self):
#         print(self.n1*self.n2)
#     def div(self):
#         print(self.n1/self.n2)
# d=mathsoperation(50,20)
# d.add()
# d.sub()
# d.mul()
# d.div()

# class Student:
#     def __init__(self,no,name,sub):
#         print('student no is:',no)
#         print('student name is:',name)
#         print('student subject is:',sub)
#         print('\n')
#     def display(self,no,name,sub):
#         print('student no is:',no)
#         print('student name is:',name)
#         print('student subject is:',sub)
# d=Student(94,'suman','python')
# d.display(96,'shivu','java')

# class Student:
#     def __init__(self,no,name,sub):
#         self.no=no
#         self.name=name
#         self.sub=sub
#     def display(self):
#         print('student no is:',self.no)
#         print('student name is:',self.name)
#         print('student sub is:',self.sub)
# d=Student(1,'hari','data scince')
# d.display()

# g_v=40
# class Test:
#     c_v=30
#     def __init__(self,l_v):
#         self.instance_v=20
#         print(l_v)
#         print(self.instance_v)
#         print(Test.c_v)
#         print(g_v)
# d=Test(10)

# class Typemethod:
#     def __init__(self):
#         self.i_v=20
#         print(self.i_v)
#     def instance(self):
#         y=50
#         print(y)
#     @classmethod
#     def class_method(cls):
#         a=10
#         print(a)
#     @staticmethod
#     def static_method(b):
#         print(b)
# d=Typemethod()
# d.instance()
# Typemethod.class_method()
# Typemethod.static_method(60)

# class Assignment:
#     x=10
#     y=20
#     def m1(self,x):
#         self.z=30
#         print(Assignment.x)
#         print(Assignment.y)
#         print(self.z)
#         print(x)
#     @classmethod
#     def method_two(cls,y):
#         print(y)
#         print(Assignment.y)
#         print(Assignment.x)
# d=Assignment()
# d.m1(40)
# Assignment.method_two(40)