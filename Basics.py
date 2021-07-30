from User import User
#Variables
msg = 'Render props'
boolean = True
number = 4
double = 4.5
names = ["Alejandro","Maria"]
# List with diferents data types
list = [1, 3.1416, 'j', 'jarroba.com',  True]
# Lenght
len(names)
# Adding a new list Value
list.append('Rodrigo')
# Inserting in a specific index
list.insert(2,45)
#Print
print(msg)
#Bucles  => ForEach
for name in names:
    print (name)
#Functions
#Return Values
def sum(a,b):
    return a+b
print(sum(5,8))
#Objects
user = User(input('Provide us your Username: '),input('Hey, and your Password too: '))
user.showUser()