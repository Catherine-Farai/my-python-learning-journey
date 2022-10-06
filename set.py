set1 = {10, 20, 30, 40, 50} #int set
print(set1)

set2 = {10.2, 20.2, 30.2, 40.2, 50.2} #float set
print(set2)

set3 = {'1', '2', '3', '4', '5'} #str set
print(set3)

set4 = {True, False} #bool set
print(set4)

set5 = {True, 10.2, 10, '2'} #het set
print(set5)

set6 = set() #empty set
print(set6)

set7 = {(12,57,43),1,2.4,'great'} #set of hashable
print(set7)

#conversion
set8 = set('sabi programmers') #converting str to set
print (set8)

set9 = set(['sabi programmers']) # converting list to st
print (set9)


set10 = set(('sabi programmers')) #converting tuple to set
print (set10)

set11 = set({1: 'sabi',2 : 'programmers'}) #converting dict to set
print (set11)

#set method
set12 = set()
#add method
set12.add(20)
set12.add('christiana')
set12.add(True)
set12.add(40.123)
print('set12: ', set12)

#update method
set13 = {'vera', 'alex', 'shola', 'wumi'}
set12.update(set13)
print('set13: ',set13)
print('set12 after updating: ', set12)

#or operators
set14 = {1,2,3,4,5}
set15 = {4,5,6,7,8}
print(set14 or set15, 'using or')

#and operator
print(set14 & set15, 'using &')
print( set14 and set15, 'using and')

#- operator
print(set14 - set15, 'using set14 -set15')
print(set15 - set14, 'using set15 - set14')

#^operator
print(set14 ^ set15, 'using^')

#intersection
print(set14.intersection(set15),'using intercsection')

#differences
print(set14.difference(set15), 'using set14.difference')
print(set15.difference(set14), 'using set15.difference')

#symmetric difference
print(set14.symmetric_difference(set15), 'using symmetric difference')

#copy method
set16 = set3.copy()
print(set16)

#clear method
set3.clear()
print('set3: ',set3)
print('set16: ',set16)

#difference update
set14 = {1,2,3,4,5}
set15 = {4,5,6,7,8}
print('set14 before differencing update: ', set14)
print('set15 before differencing update: ', set15)
set14.difference_update(set15)
print('set14 after differencing update: ', set14)
print('set15 after differencing update: ', set15)

#intersection update
set14 = {1,2,3,4,5}
set15 = {4,5,6,7,8}
print('set14 before intersection update: ', set14)
print('set15 before intersection update: ', set15)
set15.intersection_update(set14)
print('set14 after intersection update: ', set14)
print('set15 after intersection update: ', set15)

#symmetric difference update
set14 = {1,2,3,4,5}
set15 = {4,5,6,7,8}
print('set14 before symmetric_difference update: ', set14)
print('set15 before symmetric_difference update: ', set15)
set15.symmetric_difference_update(set14)
print('set14 after symmetri_differencec update: ', set14)
print('set15 after symmetric_difference update: ', set15)

#discard method
print(set15.discard(4))

#remove method
print(set15.remove(6))

#issubset method
set17 = {1,2}
print(set17.issubset(set14))

#isdisjoint method
set18 = {20,30}
print(set18.isdisjoint(set14))

#pop method
print('popped value: ',set16.pop())
print('new set16: ', set16)
      

      
