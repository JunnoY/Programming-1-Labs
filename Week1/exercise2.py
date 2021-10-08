def printState():
    print('Red Light is ' + redLight)
    print('Yellow Light is ' + yellowLight)
    print('Green Light is ' + greenLight)

redLight = 'on'
yellowLight = 'off'
greenLight = 'off'

printState()


import math


def printState():
    print('Red Light is ' + redLight)
    print('Yellow Light is ' + yellowLight)
    print('Green Light is ' + greenLight)

redLight = 'on'
yellowLight = 'off'
greenLight = 'off'

printState() #Question 2

print(type(redLight)) #Question 5


redLight = '1'
yellowLight = '0'
greenLight = '0'
#Question 6

print(3+5)#Question 7

print ("3" + "5")#Question 8

#print ("3" + 5) #Question 9

print(int("3")+int("5")) #Question 10

redLight = 'True'
yellowLight = 'False'
greenLight = 'False' #Question 11

x=10
y=20.0
z=1j
print(type(x))
print(type(y))
print(type(z)) #Question 12

day = "Beautiful"
print(day[1])
print(day[0:5])
print(day[-3])
print(day[-3:])
print(day[-5:3])
print(day[-5:-3])
print("Today is "+day)
print(str(day == "Beautiful") + ": Today is " + day)# Question 14-18

operand1 = input("Input a number: ")
print ("You entered " + operand1) #Question 19


#Question 20
#a)
number1 = int(input("Give me a number: "))
number2 = int(input("Give me another number: "))
sum = number1+number2
print("The sum is: "+ str(sum))
product = number1*number2
print("The product is: "+ str(product))
ratio = number1/number2
print("The ratio is: "+ str(ratio))
modulus = number1%number2
print("The modulus is: "+ str(modulus))
exponentiation = number1**number2
print("The exponentiation is: "+ str(exponentiation))

#b)
temp = int(input("Please input a temperature: "))
Fahrenheit = (temp * 9/5) + 32
print ('The temperature in Fahrenheit is:'+ str(Fahrenheit) + ' Fahrenheit')

#c)
radius = input('Input the radius of a circle in m: ')
circumference = 2*math.pi*int(radius)
print('The circumference of the circle is: '+str(circumference)+'m')

#d)
radius = input('Input the radius of a circle in m: ')
surface_area = 4*math.pi*((int(radius))**2)
print('The surfae area of the sphere is: '+ str(surface_area)+'m^2')

#e)
r= int(input('Input the radius of the base of a cylinder: '))
h= int(input('Input the height of a cylinder: '))
area = 2*math.pi*r*h+2*math.pi*(r^2)
print('The surface area of the cylinder is: '+str(area))

#f)
first_name = input('Input your first name: ')
surname = input('Input your surname: ')
initials = (first_name[0]+surname[0])
print('Your initials are: '+str(initials))

#g)
age= int(input('What is your age:'))
print(age<18)
print(age>17)




