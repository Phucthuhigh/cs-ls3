user = {
    "username": "admin",
    "password": "12345"
}

username = input("Username: ")
password = input("Password: ")

if username == user["username"] and password == user["password"]:
    print("You are logged in, admin.")
else:
    print("Wrong username or password.")