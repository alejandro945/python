from User import User
users = []

#Messages Format
successMsg = 'AWESOME YOU HAVE ALREADY IN OUR APP'
minorErorMsg = 'OPPS, YOU ARE MINOR'
errorMsg = 'Password or user incorret'
welcomeMsg='<<<<Welcome to our login form made with python>>>>'
option1Msg = '1- Create a User from Scratch'
option2Msg = '2- Login using JWT'
exitMsg = '3- Exit'

#Bussiness Logic
def signIn(userName,password):
    for user in users:
        if(user.getUserName() == userName and user.getPassword() == password):
            return(userName + " have login Succesfully")
    return(errorMsg)

def signUp(username,password,age,career):
    if validateAge(age):
        newUser = User(username,password,age,career)
        users.append(newUser)
        return(successMsg)
    else :
        return(minorErorMsg)

def validateAge(age):
    render = True
    if(age < 18):
        render = False
    return render

def menu():
    print(welcomeMsg)
    print(option1Msg)
    print(option2Msg)
    print(exitMsg)
    return int(input("Please select an option: "))

#App Starting 
option = menu()
while(option != 3):
    if(option==1):
        username = input('Enter your UserName: ')
        password = input('Enter your Password: ')
        age = int(input('Enter your age: '))
        career = input('Enter your professional career: ')
        print(signUp(username,password,age,career))
    elif(option==2):
        username = input('Enter your UserName: ')
        password = input('Enter your Password: ')
        print(signIn(username,password))
    option = menu()
print('Good Bye')