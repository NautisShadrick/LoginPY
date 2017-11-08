import tkinter as tk

def signup():
    #userName input
    userName = nameEntry.get()
    #password input
    passWord = passEntry.get()
    #create file if none exist with name username.account.txt
    #creates the file in same directory as this script
    file = open("%s.accountFile.txt" % (userName), "w+")
    #write username to first line of txt
    file.write(userName)
    #write password to second
    file.write("\n")
    file.write(passWord)
    label.config(text='Account Created')

def login():
    #unamei is username input
    unamei = nameEntry.get()
    #open username.account.txt for reading only and breaking lines into list
    #opens which ever file is named the username inputed
    try:
        file = open("%s.accountFile.txt" % (unamei), 'r').readlines()
    except:
        label.config(text='Unkown username try signing up!')
    #upassi user password input
    upassi = passEntry.get()
    #checking if username input matches the first line of the file
    #and that password matches the second
    try:
        if(unamei+'\n' == file[0] and upassi == file[1]):
            label.config(text='Signed in')
        else:
            #if username or password was invalid
            label.config(text='Invalid Login try again')
    except:
        label.config(text='Unkown username try signing up!')

root = tk.Tk()

root.geometry("400x150")
root.resizable(0,0)

label = tk.Label(root, text='Please sign in')

nameEntry = tk.Entry()
passEntry = tk.Entry()
signupb = tk.Button(root, text='Signup', command=signup)
loginb = tk.Button(root, text='Login', command=login)

nameEntry.grid(row = 0,column = 0)
passEntry.grid(row = 1,column = 0)

label.grid(row = 0, column = 1)

signupb.grid(row=2,column=0)
loginb.grid(row=3,column=0)

root.mainloop()
