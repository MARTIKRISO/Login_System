from werkzeug.security import generate_password_hash, check_password_hash
import mysql.connector

with open("passwd.txt", "r") as passwd:
    # connects to the db server
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd=passwd.read(),
        database="loginsystem"
    )

cursor = db.cursor(buffered=True)



def login(uname, pswrd):
    cursor.execute("SELECT * FROM Credentials WHERE username = %s", (uname,))
    row = cursor.fetchone()
    hashedpass = row[1]

    if check_password_hash(hashedpass, pswrd):
        print("Login Successful!")
    else:
        print("Login Unsuccessful!")


def register(uname, pswrd):
    # checks if the username is used
    pswrd = generate_password_hash(pswrd)
    cursor.execute("SELECT EXISTS(SELECT * FROM Credentials WHERE username = %s)", (uname,))
    usernamefetch = cursor.fetchone()
    usernameexists = usernamefetch[0]
    cursor.execute("SELECT EXISTS(SELECT * FROM Credentials WHERE password = %s)", (pswrd,))
    passwordfetch = cursor.fetchone()
    passwordexists = passwordfetch[0]

    if usernameexists:
        if passwordexists:
            # both are correct
            print("This combination is already used. You need to log in!")
        else:
            # just the username is correct, not the password
            print("This username is not available! Please choose another one and try again!")

    else:
        # new acc, needs to be registered
        cursor.execute("INSERT INTO Credentials (username, password) VALUES (%s, %s)", (uname, pswrd))
        db.commit()
        print("Registration Successful!")


def showdata():
    # shows the whole table
    cursor.execute("SELECT * FROM Credentials ORDER BY id")
    data = cursor.fetchall()
    print(data)

if __name__ == "__main__":

    action = int(input("What action do you want to perform? \n1 - Login \n2 - Register \n"))
    username = input("Username: ")
    password = input("Password: ")

    if action == 1:
        login(username, password)
    elif action == 2:
        register(username, password)
    elif action == 3:
        showdata()
    else:
        print("That action is not valid!")
