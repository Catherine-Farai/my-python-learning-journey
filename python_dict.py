num1 = {'kate': 'one' , 'bukky': 'two', 'kenny': 'three'} #DICT SRTING
num2 = {(1,2,3) : 'one two three', (4,5,6): 'four five six'} #dict tuple
num3 = {1 : 'one', 2:'two', 3:'three'} #dict num
print(num1)
print(num2)
print(num3)

num4 = {10:['one', 'two', 'three'], 5:['four', 'five', 'six']}
print(num4)
print(type(num4))

num5 = dict() #emptydict
num6 = {} #empty dict

num7 = dict(I= 'one', II = 'two', III = 'three')
print(num7)

num8 = {'I':  'one', 'II':'two', 'III':'THREE'}
print(num8)
print(num8['I'])
print(num8['II'])
print(num8['III'])
print(num8.get('I'))
print(num8.get('II'))
print(num8.get('III'))

for key in num8:
    print('Key = ' + key +', Value = '+ num8[key])
num8['I'] =11
num8['II'] = 22
num8['III'] = 33
print(num8)

num8['IV'] =4
num8['v'] =5
print(num8)

del num8['v']
print(num8)
del num2

print(num8.keys())
print(num8.values())

print('IV' in num8)
print('v' not in num8)

num9 = {'name':  'steve', 'age':25, 'III':'60'}
num10 = {'name':  'amil', 'age':23, 'III':'75'}
num11 = {'name':  'asha', 'age':20, 'III':'70'}

num12 = {'1' : num9 , '2':num10, '3':num11}
print(num12)

print(num12['1']['age'])
num1.clear()
print(num1)

      

keys = {'Mumbai', 'Bangalore','Chicago', 'New york'}
value = 'city'
num13 = dict.fromkeys(keys, value)
print(num13)
print(num12.items())

print(num3.pop(1))
print(num3)

print(num3.popitem())
print(num3)

print(num3.pop(4, 'Error'))
print(num3)

num14 = {'I': 1, 'III':3, 'IV':4}
num15 = {'II':2, 'V':5}
num14.update(num15)
print('Update Dictionary: ', num14)
print('Dictionary: ',num14)
