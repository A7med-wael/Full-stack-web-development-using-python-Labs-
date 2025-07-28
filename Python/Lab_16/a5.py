import psycopg2
conn = psycopg2.connect(
    dbname = "student_quiz",
    user = "postgres",
    password = "ahmed12345#",
    host = "localhost",
    port = "5432"
)
cur = conn.cursor()


def register(name, pwd, email, address):
    insert = f"insert into student (name, password, email, address) values ('{name}', '{pwd}', '{email}', '{address}');"
    cur.execute(insert)
    conn.commit()
    print("Register successfully")

def login(email, pwd):
    select = f"select email, password from student where email = '{email}' and password = '{pwd}'"
    cur.execute(select)
    row = cur.fetchone()
    if row is not None:
        print("Login successfully")
        return True
    else:
        print("Invalid user")
        return False


name = input("Enter your name: ")
print(f"Welcome {name} to our website")
while True:
    print("Choose the operation you want to do: ")
    print("1.Register\n2.Login\n3.Exit")
    ch = int(input("your chooies: "))
    if ch == 1:
        uname = input("Enter your username: ")
        pwd = input("Enter your password: ")
        email = input("Enter your email: ")
        address = input("Enter your address: ")
        register(uname, pwd, email, address)
        continue
    elif ch == 2:
        for i in range(3):
            email = input("Enter your email: ")
            pwd = input("Enter your password: ")
            if login(email, pwd):
                break
        break
    elif ch == 3:
        break
    else:
        print("Please choose from the last list")


cur.close()
conn.close()
