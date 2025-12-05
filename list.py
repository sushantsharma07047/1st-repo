'''#list
list1=[1,2,3]
print(list1[:2])#print element from first to nth element


#method

list1.append(4)
list1.sort
print(list1)
list1.sort(reverse=True)
print(list1)
list1.insert(2,'4')
print(list1)

#que

value1=input('ener your fav movie')
value2=input('enter your second fav movie')
value3=input('ener your  third fav movie')
list1=[value1,value2,value3]
print(list1)


a=[1,2,3,4,5,6]
print(a[-1:])


A=[1,2,3,4,5]
B=A.copy()
print(A is B)



c=[1,2,3,4,5,6,7]
del c[2:5]
print(c)

n=input('enter the number')
f=n.split(',')
j=list(map(int,n))
print(f)
print(j)

import copy as co
a=[[1,2],[3,4,]]
b=co.deepcopy(a)
a[0][1]=100
print(a,b)

a=[1,2,3,4,5]
n=int(input('enter'))
b=input("enter value")
if n<=(len(a)-1) and n>=-(len(a)):
    a[n]=b
    print(a)
else:
    print('invalid index')'''
a=[1,2,3,4]
