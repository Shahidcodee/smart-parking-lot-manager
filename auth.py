def authenticate_admin():
    PASSWORD = "admin123"
    for _ in range(3):
        pwd = input("Enter admin password: ")
        if pwd == PASSWORD:
            print("Access granted.")
            return True
        else:
            print("Incorrect password.")
    print("Access denied.")
    return False
