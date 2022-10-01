num1 = 100 #assigning 100 to num1
print(num1)

num2 = -10 #assigning -ve integar to num2
print(num2)

num3 = 1_000_000 #seperating with underscore
print(num3)

print(type(num1), type(num2), type(num3)) #seperating type num1, num2, num3


num4 = int(5.0567) #Cconverting flot to integar
num5 = int('567484') #converting string to integar
print(num4)
print(num5)

num6 = int('100', 2) # converting string 100 to int base 2
print(num6)

num7 = int('3236', 8) #converting sring to base 2s
print(num7)

#binary
num8 = 0b1110111101 #assigning binary number to num8
print(num8)
print(type(num8)) #printing out type of var number

num9 = 0b_100_010_101 #seperating binary with underscore
print(num9)

num10 = 0o12 # assigning octal number to num10
print(num10) #printing num10 in base 10
print(type(num10)) #type num10

num11 = 0o12344567 #assigning 0ct to 11
print(num11) #printing num11 in base 10

#Hexadecimal
num12 = 0x123Afde #assigning hex to num12
print(num12)

num13 = 0x1234567adefbcb #assigning hex to num13
print(num13)

num14 =1.23356734 #assigning a +ve float to num14
print(num14)
num15 = -1234542.12456 #assigning -ve to float to num
print(num15)

num16 = 123_234.732_357 #seperating with float_
print(num16)

num17 = 2e400 #exceeding memory size
print(num17)

num18 = 1e3 # using scientific notation
print(num18)

num19 = 3.14234232e3 # using scientific notataion
print(num19)

#float conversion
num20 = float('-5.5') #converting -ve to string
print(num20)

num21 = float ('5') #converting strings to float
print(num21)

num22 = float('      -5') #converting srtings with space with int to float
print(num22)

num23 = float('-1e3') #converting scientific notation
print(num23)

num24 = float('-infinity') #converting -infinity to float
print(num24)

num25 = float('inf') #converting inf to float
print(num25)

#ARITHMETIC OPERATOR
num26 = 1500
num27 = 20
print( num26+num27) #addition
print( num26-num27) #subtraction
print( num2*num27) # multiplication
print( num2/+num27) #division
print( num26%num27) #modulus print out reminder
print( num26**num27)#exponent or power
print( num26//num27) #floor division
print(f'{hex(num26)}') #converting num26 to hex
print(f'{oct(num26)}') #converting num26 to oct
print(f'{bin(num26)}') #converting num26 to bin
print(pow(num27,3)) #num27 raise to power 3
print(abs(-12345432)) #absolute
print(round(123.345678)) #round to nearest whole number



