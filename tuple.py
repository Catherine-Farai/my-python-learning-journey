tpl1 = (10.2, 11.3, 12.5, 16.2) #float tuple
print(tpl1)

tpl2 = (10, 12, 13, 14, 16, 17) #int tuple
print(tpl2)

tpl3 = ('hello', 'food', 'cat',) #str tuple
print(tpl3)

tpl4 = (True, False) #bool tuple
print(tpl4)

tpl5 = (10.2, 10, False, 'str',) #heterogenous tuple
print(tpl5)

tpl6 = ( ) # empty tuple
print(tpl6)
print(type(tpl6))

tpl7 = 10.2, 11.3, 12.5, 16.2 #float tuple
print(tpl1)

tpl8 = 10, 12, 13, 14, 16, 17 #int tuple
print(tpl2)

tpl9 = 'hello', 'food', 'cat', #str tuple
print(tpl3)

tpl10 = True, False #bool tuple
print(tpl4)

tpl11 = 10.2, 10, False, 'str', # heterogenous tuple
print(tpl5)

print(tpl1[0]) #first using positive indexing
print(tpl1[3]) #last using positive indexing

print(tpl1[-1]) #first using negative indexing
print(tpl1[-4]) #last using negative indexing

#deleting tuple
del tpl10 #delete tpl10

#conversion
tpl12 = tuple('sabi programmers') #string to tuple
print(tpl12)

tpl13 = tuple(['sabi', 'programmers']) #list to tuples
print(tpl13)

tpl14 = tuple({1,2,3,4,5}) #set to tuple
print(tpl14)

tpl15 = tuple({1:'one', 2:'two'}) #dict to tuple
print(tpl15)

#operators
print(tpl1 + tpl3) #+ve operator
print(tpl4 *4) #*operator
print(tpl2[1:3]) #slicing
print(2.4 in tpl3) #in operator
print(2.4 not in tpl3) #not in operator




