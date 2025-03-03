
#x=int(input('enter x value:'))
#y=int(input('enter y value:'))
#def arith(x,y):
 #   return x+y
#sum=arith(x,y)
#print('sum of x and y is',sum)

#def fun(place,name):
 #   return f'{place},{name}'
#r=fun('smg','sumanth')
#print(r)

#x=input('enter the name:')
#def name(x):
 #   return x[::-1]
#x=name(x)
#print(x)

#x=int(input('enter the x value:'))
#y=int(input('enter the y value:'))
#def fun(x,y):
 #   return f'sum of{x} and {y}is {x+y} sub{x,y}is {x-y} mul{x,y}is {x*y} div{x,y} is {x/y} rem{x,y} is {x%y}'
#a=fun(x,y)
#print(a)


#x=int(input('enter the x value:'))
#y=int(input('enter the y value:'))
#if x>y:
 #   print(x)
#else:
 #   print(y)
#print('thanks')

#x=int(input('enter the x value:'))
#if x%2==0:
 #   print('even')
#else:
 #   print('odd')

#x=int(input('enter the x value:'))
#y=int(input('enter the y value:'))
#z=int(input('enter the z value:'))
#if x>y:
 #   print('x is bigger')
#elif y>z:
 #   print('y is bigger')
#elif z>x:
 #   print('z is bigger')
#elif x>z:
 #   print('x is bigger')
#elif y>x:
 #   print('y is bigger')
#elif z>y:
 #   print('z is bigger')

#x=int(input('enter the x value:'))
#y=int(input('enter the y value:'))
#z=int(input('enter the z value:'))
#if x>=y and x>=z:
 #   large=x
#elif y>=z and y>=x:
 #   large=y
#else:
 #   large=z
#print('the largest no is',large)

#vowel and cosonants
#str=input('enter the char:').lower()
#if str=="a" or str=='e' or str=='i' or str=='o' or str=='u':
 #   print(str,'is a vowel')
#else:
 #   print(str,"is a consonant")

#leap year
#x=int(input('enter the no:'))
#if (x%400==0) or (x%400==0 and x%100==0):
 #   print(x,' a leap year')
#else:
 #   print(x,'not a leap year')

# str=input('enter the str name:')
# if str==str[::-1]:
#     print(str,'is a pallidrome')
# else:
#     print(str,'is not a pollindrome')

#length=int(input('enter the length value:'))
#breadth=int(input('enter the breadth value:'))
#if length==breadth:
#    print('its is a square')
#else:
 #   print('it is a rectangle')
'''
m=input('enter the gender:')
h=int(input('enter the height:'))
if m==f'male' or m==f'MALE' and h>=188:
    print(m,' is eligible for sports')
elif m==f'female'or m==f'FEMALE' and h>=175:
    print(m,' is eligible for sports')
else:
    print(m,'is not eligible for sports')
'''
'''
x=1
while x<=100:
    print(x ,end=' ')
    x=x+2
'''
'''
x=2
while x<=65536:
    print(x,end=' ')
    x=x**2
'''
'''
x=3125
while x>=5:
    print(int(x),end=' ')
    x=x//5
'''
'''
x=1
i=1
while x<=10:
    print(f'1*{x}={1*x}')
    x=x+1
'''
'''
x=1
while x<=10:
    print(f'4*{x}={4*x}')
    x=x+1
'''
'''
print(10+5*2)
print(17%4)
print(2**3)
print(9//2)
print(5==5.0)
print(10>5 and 3>1)
print('false' or 'true' or 'true')
print(not(5>10))
x=10
x+=5
print(x)
print(5&9)
print(5|4)
n=5
r=5>>2
print(r)
'''
'''
li=[10,20,30,40,50]
for i in range(0,5,2):
    print(li[i],end=' ')
'''
'''
li=[10,20,30,40,50]
for i in range(len(li)-2,0,-2):
    print(li[i],end=' ')
'''
'''
li=[10,20,13,61,50]
print('even indices are:)
for i in range(0,5,2):
    print(li[i],end=' ')
print('\n odd indices are:)
for i in range(1,4,2):
    print(li[i],end=' ')
'''
'''
li=[10,20,13,61,50]
for i in li:
    if i%2==0:
        print(i,'is a even element ')
else:
    print(i,'is odd element')
print('\n')
sum=0
for i in li:
    sum=sum+i
    print('sum of the elements is:',sum)
'''
'''
li=[10,20,13,61,50]
sum_even=0
sum_odd=0
for i in li:
    if i%2==0:
      sum_even=sum_even+i
else:
    sum_odd=sum_odd+i
print('sum of even elments is:',sum_even)
print('sum of odd elements is:',sum_odd)
'''
'''
li=[10,20,13,61,50]
sum_even=0
sum_odd=0
for i in range(0,5,2):
    sum_even=sum_even+li[i]
else:
    sum_odd=sum_odd+li[i]
print(sum_even)
print(sum_odd)
'''
'''
li=[10,20,13,1,50]
for i in range(len(li)):
    if i%2==0:
        print(i,end=' ')
'''

# li=['a','e','i','o','u']
# cha=input('enter the cha:')
# for i in li:
#     if cha==i:
#         print(cha,'is a vowel')
#         break
# else:
#     print(cha,'is not a vowel')

# s=input('enter the str:')
# space=0
# word=1
# for i in s:
#     if i==' ':
#         space=space+1
# word=space+1
# print(space,'space in the above str')
# print(word,'words in the above str')

# li=[10,20,40,60,83]
# biggest=0
# lowest=0
# for i in li:
#     if i>biggest:
#         biggest=i
# print(biggest,'is biggest in above list')

# li=[10,20,40,30,3,99]
# lowest=99
# for i in li:
#     if i<lowest:
#         lowest=i
# print(lowest)

# h_no=int(input('enter the house no:'))
# s=input('enter the street name:')
# city=input('enter the city name:')
# pincode=int(input('enter the pincode:'))
# di={
#     'house number':h_no,
#     'street ':s,
#     'city':city,
#     'pincode':pincode
# }
# for i,j in di.items():
#     print(i,'=',j)

# li=[]
# num=input('enter the elements:')
# for i in range(5):
#     li.append(num)
# print(li)

# num=int(input('enter the n value:'))
# res=num
# rev=0
# while num>0:
#     rem=num%10
#     rev=(rev*10)+rem
#     num=num//10
# if rev==res:
#    print(res,'it is a pallindrome')
# else:
#     print(res,'it is not a pallindeome')
# print(10//3)

# def fun(x,*y,z=100):
#     print(x)
#     print(y)
#     print(z)
# fun(10,20,30,40,60)
# fun(10,20,30,40)
# fun(10,20,30,z=108)

# def fun(x,y,*z,email='not provided'):
#     print(x)
#     print(y)
#     print(z)
#     print(email)
# fun('anamika','o+ve','brithing problem,cold',email='semjkfmd10293@gmail.com')
#
# def fun(name,*email,**adress):
#     print(name)
#     print(email)
#     print(adress)
# fun('sumanth','sqqsnbh@gmail.com','nejfvnjenj@gmail.com',city='shivamogga',taluk='shikaripura',village='essur')




