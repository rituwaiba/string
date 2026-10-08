'''

-----STRING----

----INDEXING----

--> retrive the elements inside the string

1. > positive indexing starts from 0
   > it starts from left side

 2.> negative indexing starts from -1
   > it starts from right side

 a  p  p  l  e 
 0  1  2  3  4 -->positive indexing
-5 -4 -3 -2 -1 -->negative indexing

----SLICING-----

-->retrive the elements from one position to another position
   start:stop:step

'''

a="apple"
print(a[1])
print(a[2])
print(a[3])
print(a[-3])

#space is also cosidered as a ....

#slicing
#<< used for printing range i.e printing more than one character

b=" stmary university"
print(b[1:7])
#prints from 1 to 7-1;n=7
print(b[3:7])
print(b[2:6])

a="apple"
print(a[:4])
#starts from 0 and ends at n-1
print(a[1:])
#starts from 0 and ends at deadend
print(a[4:])

#reverse the string
print(b(::-1))


z="computer science and engineering"
#  123456789.......
print(z(1:7:2))
#start:stop:step
print(z(2:15:5))
print(z(4:12:3))

y="python programming"
print(y[3:99])

