import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="martin2005",
    database="loginsystem"
)

cursor = db.cursor(buffered=True)


def login(uname, pswrd):
    cursor.execute("SELECT * FROM Credentials WHERE username = %s", (uname, ))
    row = cursor.fetchone()
    passwordcorrect = False
    try:
        passwordcorrect = pswrd == row[1]
    except:
        print("Username does not exist in database!")
        quit()
    finally:
        if passwordcorrect:
            print("Login Successful!")
        else:
            print("Login Unsuccessful!")


def register(uname, pswrd):

    cursor.execute("SELECT EXISTS(SELECT * FROM Credentials WHERE username = %s)", (uname, ))
    usernamefetch = cursor.fetchone()
    usernameexists = bool(usernamefetch[0])
    cursor.execute("SELECT EXISTS(SELECT * FROM Credentials WHERE password = %s)", (pswrd, ))
    passwordfetch = cursor.fetchone()
    passwordexists = bool(passwordfetch[0])

    if usernameexists:
        if passwordexists:
            #both are correct
            print("This combination is already used. You need to log in!")
        else:
            #just the username is correct, not the password
            print("This username is not available! Please choose another one and try again!")

    else:
        #new acc, needs to be registered
        cursor.execute("INSERT INTO Credentials (username, password) VALUES (%s, %s)", (uname, pswrd))
        db.commit()
        print("Registration Successful!")

def showdata():
    cursor.execute("SELECT * FROM Credentials ORDER BY id")
    data = cursor.fetchall()
    print(data)


#cursor.execute
#("CREATE TABLE Credentials(username VARCHAR(255), password VARCHAR(255), ID int PRIMARY KEY AUTO_INCREMENT)")

if __name__ == "__main__":
    action = input("What action do you want to perform? \n1 - Login \n2 - Register \n")
    username = input("Username: ")
    password = input("Password: ")

    if action == 1:
        login(username, password)
    elif action == 2:
        register(username, password)
    elif action == "admin":
        showdata()
    else:
        print("That action is not valid!")



