import sqlite3
import re

reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"


def register():
            userid = input("Please enter your ID: ")
            pass1 = input("Please enter your Password: ")
            pass2 = input("Please re-enter your Password: ")

            if pass1 == pass2 and re.search(reg, pass1):
                conn = sqlite3.connect("passwords_database.db")
                c = conn.cursor()
                c.execute("CREATE TABLE IF NOT EXISTS LoginTable(userid VARCHAR, pass1 VARCHAR)")
                data = []
                for record in(c.execute('''SELECT userid FROM LoginTable''')):
                #records = c.fetchall()
                    data.append(record[0])
                #for record in records:
                print(data)    
                if userid not in data:    

                    c.execute("INSERT INTO LoginTable VALUES('" +
                                    userid + "','" + pass1 + "')")
                    conn.commit()
                    c.close()
                else:
                    print("User already exists!!")
            else:
                print("Password did not match!!!")
            
def chagepassword():
            print("you are about to change your password!!")
            userid = input("Please enter your user ID: ")
            password = input("Please enter your password: ")
            
            conn = sqlite3.connect("passwords_database.db")
            c = conn.cursor()
            
            for row in(c.execute("SELECT pass1 from LoginTable WHERE userid = '{}'".format(userid))):
                
                if row[0] == password:
                    newpass1 = input("Please enter your new password: ")
                    newpass2 = input("Please re-enter your new password: ")
                    if newpass1 == newpass2 and re.search(reg, newpass1):
                        c.execute("""UPDATE LoginTable SET pass1 = '{}' where userid = '{}'""".format(newpass1, userid))
                        conn.commit()
                        
                        print("Successfully updated!!!")
                    else:
                        print("Password did not match!!!")
                else:
                    print("Incorrect Username or Password!!!")

def login():
    userid = input("Please enter your user name: ")
    pass1 = input("please enter your password: ")
    conn = sqlite3.connect("passwords_database.db")
    c = conn.cursor()
    for row in(c.execute("""SELECT pass1 from LoginTable WHERE userid = '{}'""".format(userid))):
        if row[0] == pass1:
            print("Login Success!!!")
            
    
            loginoptions = int(input("Please select one option: \n 1) New Entry \n 2) View Entries \n"))
            if loginoptions == 1:
                newentry()
            elif loginoptions == 2:
                viewentry()
            else:
                print("Invalid option")
            
def newentry():
    #s = service 
    s_name = input("Please enter the name of service: ")
    s_email = input("Please enter the email used for the service: ")
    s_userid = input("Please enter your user name of the service: ")
    s_pass = input("Please enter the password of the service:  ")
    conn = sqlite3.connect("passwords_database.db")
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS userinfo(s_name VARCHAR, s_email VARCHAR, s_userid VARCHAR, s_pass VARCHAR)")
    c.execute("INSERT INTO userinfo VALUES('"+s_name+"', '"+s_email+"','"+s_userid+"', '"+s_pass+"')")
    conn.commit()
    print("Successfully Added")
    
def viewentry():
    conn = sqlite3.connect("passwords_database.db")
    c = conn.cursor()
    c.execute("SELECT * FROM userinfo")
    data = c.fetchall()
    for d in data:
        print("Service name: ", d[0])
        print("Email: ", d[1])
        print("User name: ", d[2])
        print("Password: ", d[3])
        print("\n")
    conn.commit()



if __name__ == "__main__":
    def starting():
        options = int(
        input("Please select your option : \n 1) Register \n 2) Login \n "))
        if options == 1:
            registeroptions = int(input(
                "Please select one option : \n 1) New User Registration \n 2) Re-set your password"))
            if registeroptions == 1:
                register()
            
            elif registeroptions == 2:
                chagepassword()
            else:
                print("Invalid option")

        elif options == 2:
            login()
        else:
            print("Invalid option")
    starting()