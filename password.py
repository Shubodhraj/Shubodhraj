import sqlite3
import sys
option = int(input("Please enter your option: \n 1: New Entry \n 2: Retrieve Data \n 3: Set Master Password \n"))
master = "ABCD"
if option == 1:
    servicename = input("Please enter your servicename:")
    email = input("Please enter your email:")
    username = input("Please enter your username:")
    password = input("Please enter your password:")
    conn = sqlite3.connect('Password_vault')
    c = conn.cursor()
    #c.execute("DROP TABLE userinfo")
    c.execute('''
          CREATE TABLE IF NOT EXISTS userinfo
          (servicename VARCHAR, email VARCHAR, username VARCHAR, password VARCHAR)
          ''')
    c.execute("INSERT INTO userinfo VALUES ('" + servicename + "', '" + email + "', '" + username + "','" + password + "')")
    print("Successfully added")
    conn.commit()
    conn.close
elif option == 2:
    mstr = input("Please enter master password: \n")
    #conn = sqlite3.connect('Password_vault')
    #c = conn.cursor()
    #master = c.execute("SELECT * FROM master")
    #conn.commit()
    if master == mstr:
        conn = sqlite3.connect('Password_vault')
        c = conn.cursor()
        for row in (c.execute("SELECT * from userinfo")):
            print((row))
        conn.commit()
    else:
        print("Invalid Credential")
elif option == 3:
    pass

   
else:
    print("You have entered invalid input")