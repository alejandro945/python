from User import User
#Variables
msg = 'Render props'
boolean = True
number = 4
double = 4.5
names = ["Alejandro","Maria"]
# List with diferents data types
listA = [1, 3.1416, 'j', 'jarroba.com',  True]
# Lenght
len(names)
# Adding a new list Value
listA.append('Rodrigo')
# Inserting in a specific index
listA.insert(2,45)
#Print
print(msg)
#Bucles  => ForEach
for name in names:
    print  (name)
#Functions
#Return Values
def sum(a,b):
    return a+b
print(sum(5,8))
#Objects and inputs
user = User('ALEJO','12345',18,'Sistemas')
user.showUser()
#Pure Functions: Thse that always return the same result dont use global variables
def squared(number):
    return number * number

def squaredsum(a,b):
    return squared(a) + squared(b)

print('This is a Square Sum: ',squaredsum(5,4))

# Mapping objects

numberList = [1,2,3,4,5,6,7]

squaredList = list(map(squared,numberList))
print('This is a Square List: ',squaredList)

# Filter
def onlyAdults(age):
    return age > 3

print('This is a Filter List: ',tuple(filter(onlyAdults,numberList)))

# Reverse
result = list(reversed(numberList))
print('This is a Reverse List: ',result)
