import sqlite3
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
    print("You have entered option 3. For now the option is not available!")
    # #mstr = input("Please enter master password: \n")
    # conn = sqlite3.connect('Password_vault')
    # c = conn.cursor()
    # c.execute('''CREATE TABLE IF NOT EXISTS master(master_password VARCHAR)''')
    
    # master = c.execute("SELECT COUNT(*) FROM master")
    # #print(master)
    # #conn.commit()
    # #for master in c.execute("SELECT * FROM master"):
       

    # if master == 0:
    #     mstr = input("Please set your master password: \n")
    #     mstr1 = input("Please re-enter your master password: \n")
    #     if mstr == mstr1:
    #         conn = sqlite3.connect('Password_vault')
    #         c = conn.cursor()
    #         c.execute('''CREATE TABLE IF NOT EXISTS master(master_password VARCHAR)''')
    #         c.execute("INSERT INTO master VALUES('" + mstr + "',)")
    #         conn.commit()
    #     else:
    #         print("Passwords did not match")
    # else:

    #mster1 = input("Please enter your Password: ")
    # conn = sqlite3.connect('Password_vault')
    # c = conn.cursor()
    # c.execute('''CREATE TABLE IF NOT EXISTS master(master_password VARCHAR)''')
    # #c.execute("INSERT INTO master VALUES('" + mster1+ "',)")
    # newpassword1 = input("Please enter your new password: ")
    # newpassword2 = input("Please re-enter your new password: ")
    # if newpassword1 == newpassword2:
    #         c.execute("DROP TABLE master")
    #         c.execute('''CREATE TABLE IF NOT EXISTS master(master_password VARCHAR)''')
    #         c.execute("INSERT INTO master VALUES('" + newpassword1 + "')")
    #         master = c.execute("SELECT * from master")
    #         conn.commit()

    # if mster1 == master:
    #     newpassword1 = input("Please enter your new password: ")
    #     newpassword2 = input("Please re-enter your new password: ")
    #     if newpassword1 == newpassword2:
    #         c.execute("DROP TABLE master")
    #         c.execute('''CREATE TABLE IF NOT EXISTS master(master_password VARCHAR)''')
    #         c.execute("INSERT INTO master VALUES('" + newpassword1 + "',)")
    #         master = c.execute("SELECT * from master")
    #         conn.commit()
else:
    print("You have entered invalid input")