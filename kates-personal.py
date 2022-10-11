name = ('jeff')
print(name)
print(type(name))

name = ('jeff',)
print(name)
print(type(name))

name = ('jeff', 'kate', 'bukky', 'kenny')
print(name[-2])

'''names = ('jeff', 'kate', 'bukky', 'kenny')
a,b,c,d = names
print(name[-2])'''

'''names = ('jeff', 'kate', 'bukky', 'kenny')
names[0] ='fraih'
print(names)'''


t2=(4,5,6)
print(t2+(7,8,9,))

emp = {3, 'Steve', 10.5, True}
print(emp)

'''myset = {[10, 13], 11, 20}
print(myset)'''

set = {10, 20, 30,40}
set.add(20)

s1 = {1,2,3,4,5,6,8,9}
s2 = {3,4,5,6,8,9,12,13}
print(s1 - s2)
print(s2 - s1)

romanNums = {'I':1, 'II':2, 'III':3, 'IV':4, 'V':5}
print(romanNums)

items={("Parker","Reynolds","Camlin"):"pen", ("LG","Whirlpool","Samsung"): "Refrigerator"} # tuple key, string value
print(items)

numNames = {1:"One", 2:"Two", 3:"Three", 2:"Two", 1:"One"}
print(numNames)

print(numNames[1])

'''numoperatr = operatior.add(5,6)
print(numoperatr)'''


price = 100

if price > 100:
 print("price is greater than 100")

if price == 100:
  print("price is 100")

if price < 100:
    print("price is less than 100")

price = 50

if price > 100:
    print("price is greater than 100")
elif price == 100:
    print("price is 100")
elif price < 100:
    print("price is less than 100")
deque = ([0, 10, 20, 30, 40])
deque.pop()
print(deque)

#print(math.radians(30))
#print(math.e)

import math
math.exp(30)
print(math)

'''import collections
student = collections.namedtuple('student', [name, age, marks])
s1 = student("Imran", 21, 98)
print(s1.name)

s1 = student("Imran", 21, 98)
student = collections.namedtuple('student', [name, age, marks])
print(s1.name)

s1 = student('kate', 21, 98)
student = ('name', 'age', 'marks')
print(s1.name)'''




 
 




















