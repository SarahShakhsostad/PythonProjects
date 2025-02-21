from cryptography.fernet import Fernet

# pass = 1234
# key = fdthdetkurkutdfgvfkyliutyit
# key + pass => encrypted password
# encrypted password + key => pass

# def write_key():
#      key = Fernet.generate_key()
#      with open("./mykey.key", "wb") as f:
#           f.write(key)

# write_key()
def load_key():
     with open("./mykey.key", "rb") as f:
          return f.read()
     
key = load_key()

fernet = Fernet(key)  # we can use this "Ctrl + /" to comment all the code

def  add_pass(username, password):
    with open("./passwords.txt", "a") as f:  # mode "a" is for appending an item
              # string => byte (we should use encode() for doing this.)
              encrypted_pass = fernet.encrypt(password.encode()).decode()  # bytes => string (decode())
              f.write(f"{username}|{encrypted_pass}\n")
    print("ADDED!")


def view_pass():
     with open("./passwords.txt", "r") as f:
          lines = f.readlines()

     print("Your passwords are as follows: ")
     for item in lines:
               item = item.rstrip()  # rstrip() deletes "\n" at the end of any item
               if "|" not in item:  # Skip malformed lines
                    continue

               try:
                    username, encrypted_password = item.split("|", 1)  # Ensure proper split
                    password = fernet.decrypt(encrypted_password).decode()
                    print(f"Username: {username}, Password: {password}")
               except ValueError:
                    print(f"Skipping malformed entry: {item}")  # Debug message

while True:
    user_input = input ("Enter the mode (v: view, a: add, q: quit)")

    if user_input == "v":
        
        view_pass()

    elif user_input == "a":
        print("let's add a new username-password")
        username = input("Enter new username:")
        password = input("Enter new password: ")
        add_pass(username, password)

    elif user_input == "q":
        break
    else: 
        print("wrong mode!")

