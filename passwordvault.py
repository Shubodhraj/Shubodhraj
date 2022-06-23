import sqlite3
import re
options = int(
    input("Please select one option : \n 1) Register \n 2) Login \n "))
reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
if options == 1:
    registeroptions = int(input(
        "Please select one option : \n 1) New User Registration \n 2) Re-set your password"))
    if registeroptions == 1:
        userID = input("Please enter your user ID: ")
        password1 = input("Please enter your password: ")
        password2 = input("Please re-enter your password: ")
        if password1 == password2:
            
            if re.search(reg, password1):
                conn = sqlite3.connect("Password_vault.db")
                c = conn.cursor()
                c.execute('''
            CREATE TABLE IF NOT EXISTS loginInfo
            (username VARCHAR, password VARCHAR)
            ''')

                data = []

                c.execute("SELECT username FROM loginInfo")
                data = c.fetchall()
                # here data is a list of tuples so we need to create another list that contains the items from tuples.
                datalist = []
                for i in data:
                    datalist.append(i[0])

                if userID not in datalist:
                    c.execute("INSERT INTO loginInfo VALUES('" +
                            userID + "','" + password1 + "' )")
                    conn.commit()
                else:
                    print("user name already exists")
            else:
                print("Invalid password")

        else:

            print("Password did not match!!!")

    elif registeroptions == 2:
        print("Do you want to change your password?")
        userID = input("Enter your ID!")
        userPass = input("Enter your Password")
        conn = sqlite3.connect("Password_vault.db")
        c = conn.cursor()
        # c.execute("SELECT * FROM loginInfo")
        # userdata = c.fetchall()
        # print(userdata)

        #setuser = ("""SELECT password FROM loginInfo WHERE username = ?""")
        #c.execute(setuser, [(userID)])

        for row in (c.execute("""SELECT password FROM loginInfo WHERE username = '{}'""".format(userID))):
            if row[0] == userPass:
                newpassword1 = input("Please Enter your new password")
                newpassword2 = input("Please RE-Enter your new password")
                if newpassword1 == newpassword2 and re.search(reg, newpassword1):
                    c.execute("""UPDATE loginInfo SET password = '{}' WHERE username = '{}'""".format(
                        newpassword1, userID))
                    conn.commit()
                else:
                    print("Password did not match!!!")
            else:
                print("Invalid Password")

elif options == 2:
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")
    conn = sqlite3.connect("Password_vault.db")
    c = conn.cursor()
    for row in (c.execute("""SELECT password FROM loginInfo WHERE username = '{}'""".format(username))):
        if row[0] == password:
            loginoptions = int(
                input("Please select one option: \n 1)Save New data \n 2)Retrieve data"))
            conn.commit()
            if loginoptions == 1:
                service = input("Please enter the name of the service: ")
                email = input("Please enter the emal-id: ")
                userid = input("Please enter your userid: ")
                password = input("Please enter the password: ")
                conn = sqlite3.connect("Password_vault.db")
                c = conn.cursor()
                c.execute('''
                            CREATE TABLE IF NOT EXISTS userinfo
                                (servicename VARCHAR, email VARCHAR, username VARCHAR, password VARCHAR)
                            ''')
                c.execute("INSERT INTO userinfo VALUES ('" + service +
                          "', '" + email + "', '" + username + "','" + password + "')")
                print("Successfully added")
                conn.commit()
            elif loginoptions == 2:
                conn = sqlite3.connect("Password_vault.db")
                c = conn.cursor()
                c.execute("""SELECT * FROM userinfo""")
                infolist = []
                infolist = c.fetchall()
                for i in infolist:
                    print(i)
                conn.commit()

        else:
            print("You have inputed invalid entry")
