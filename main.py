import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="martin2005",
    database="loginsystem"
)

cursor = db.cursor(buffered=True)


def login():
    try:
        pass
    except:
        pass

def register(uname, pswrd):

    cursor.execute(f"SELECT EXISTS(SELECT * FROM Credentials WHERE username = \'{uname}\')")
    usernamefetch = cursor.fetchone()
    usernameexists = bool(usernamefetch[0])
    cursor.execute(f"SELECT EXISTS(SELECT * FROM Credentials WHERE password = \'{pswrd}\')")
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




#cursor.execute
#("CREATE TABLE Credentials(username VARCHAR(255), password VARCHAR(255), ID int PRIMARY KEY AUTO_INCREMENT)")

if __name__ == "__main__":
    register("testusername", "testpassword")

