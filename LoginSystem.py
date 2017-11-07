def signup():
    #userName input
    userName = input("UserName: ").lower()
    #password input
    passWord = input("Password: ")
    #create file if none exist with name username.account.txt
    #creates the file in same directory as this script
    file = open("%s.accountFile.txt" % (userName), "w+")
    #write username to first line of txt
    file.write(userName)
    #write password to second
    file.write("\n")
    file.write(passWord)

def login():
    #unamei is username input
    unamei = input("UserName: ").lower()
    #open username.account.txt for reading only and breaking lines into list
    #opens which ever file is named the username inputed
    file = open("%s.accountFile.txt" % (unamei), 'r').readlines();
    #upassi user password input
    upassi = input("Password: ")
    #checking if username input matches the first line of the file
    #and that password matches the second
    if(unamei+'\n' == file[0] and upassi == file[1]):
        print('signed in')
        #print signed in and do what ever you want
    else:
        #if username or password was invalid
        print('invalid')
        #attempt login again
        login()

#start function just simple input to choose signup or login functions
def start():
    ui = input("Signup or Login").lower()
    if(ui == 'signup'):
        signup()
    elif(ui == 'login'):
        login()

start()
