'''
-----STRING-----

-->A string is a sequence of characters
-->String is a set of characters
eg:apple


string can be mentioned in :
1.Double quotes - ""
2.Single Quotes - ''
3.Triple quotes - ''''''

'''

a="apple"
b='banana'
c='''mango'''

print(a)
print(b)
print(c)

m="abc"
n="123"
o="!@#"

z="apple"
print(z*3) #repetiton --> it will print z three times

x="apple"
y="banana"
print(x+y) #concatation --> linling things together

a="welcome to class"



'''
----INDEXING----

-->retrive the elements inside the string

>positive indexing starts from 0
>it starts from left side

>negative indexing starts from -1
>it starts from right side

 a  p  p  l  e 
 0  1  2  3  4 -->positive indexing
-5 -4 -3 -2 -1 -->negative indexing

----SLICING-----

-->retrive the elements from one position to another position
   start:stop:step

'''

#indexing
#<<prints only one character

a="apple"
#  01234
print(a[2])
print(a[3])
print(a[-3])

b=" stmary university"
#  0123456789
#space is also cosidered as a ....

#slicing
#<< used for printing range i.e printing more than one character

b=" stmary university"
print(b[2])
print(b[3:7])
print(b[2:6])

a="apple"
print(a[:4])
print(a[1:])
print(a[4:])

#reverse the string
print(b(::-1))


z="computer science and engineering"
#  123456789.......
print(z(1:7:2))
#start:stop:step
print(z(2:15:5))