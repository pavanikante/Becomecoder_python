a,b = map(int,input().split())
print(a%b)
"""
a=input()
b=input()
print(num('a')+num('b'))
"""
"""
n=int(input())
for i in range(0,n+1):
        print(i,end=" ")
"""
"""
n=int(input())
i=n
while i>=1:
    print(i,end=" ")
    i-=1
"""
"""
num=int(input())
while num>0:##/num!=0/num
        print(num,end=" ")
        num-=1
"""
"""
num=int(input())
i=1
while i<=num:
    if i%3==0:
        i+=1
        continue
  print(i,end=" ")
   i+=1

n=int(input())
i=1
while i<num:
    print(i,end=" ")
    i+=1
    if

n=int(input())
while num:
  r=num%10
  num=num//10
  print(r,num)
"""
"""
r=int(input())
perimeter =3.14*r*2
area=3.14*r*r
diameter=r*2
print('perimeter:',perimeter,'area:',area,'diameter:',diameter)
"""
"""
l=int(input())
b=int(input())
a=l*l+b*b
print('area:',l*b)
print('perimeter:',2*(l+b))
print('diagnol:',a**(1/2))
"""
"""
l=int(input())
b=int(input())
a=l*l+b*b
print('area:',l*b)
print('perimeter:',2*(l+b))
print('diagnol:',a**(1/2))
"""
"""
a=int(input())
if a>0:
                print('positive')
elif a==0:
                print('zero')
else:
                print('negative')
"""
"""
num=int(input())
for i in range(num,-1,-1):
                print(i,end=' ')
"""
"""
num=int(input())
while True:
               if num==0:
               break
               print(num,end=' ')
              num-=1
"""
"""
num=int(input())
s=0
def value(num):
                while num:
                                
                   r=num%10
                   num=num//10
                   s+=r
                   if s==0:
                                   break
print(s)
""""
"""
a,b,c=map(int,input().split())
if b<c:
                x=b
                y=c+1
                d=1
elif b>c:
                x=c
                y=b-1
                d=-1
for i in range(1,c+1):
                if (a*i)%3==0:
                                continue
                print(a,'X',i,'=',a*i)
"""
"""
num=int(input())
ecount=0
ocount=0
x=0
y=0
while num:
    r=num%10
    num=num//10
     if r%2==0:
          x=x*10+r
     else:
          y=y*10+r
print(x,'',y)          
if ecount%2==0 and ocount%2!=0:
     print('even   odd')
elif ecount%2==0 and ocount%2==0:
     print('even')
elif ecount%2!=0 and ocount%2!=0:
     print('odd')
else:
     print('mixed')
"""
"""
num,s,re=map(int,input().split())
count=0
x=0
while num:
     r=num%10
     num=num//10
     if r==s:
          r=re
     elif r%s==0:
          r=(r//s)
     x=x+r*pow(10,count)
     count+=1
print(x)
"""
"""
a,b,c,d=map(int,input().split())
d=int(input())
a=0
b=1
print(a)
for i in range (1,d+1):
   c=a+b
    a=b
    b=c
    print(c)
"""
"""










