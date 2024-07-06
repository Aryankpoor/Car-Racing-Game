from cryptography.fernet import Fernet

def write_key():
    key = Fernet.generate_key()
    with open('key.key', "wb") as key_file:
        key_file.write(key)
        

def load_key():
    file = open("key.key", "rb").read()
    key = file.read()
    file.close()
    return key


master_pwd = input("What is the master password?")
key = load_key()
fer = Fernet(key)

def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = print(line.rstrip())
            user, passw = data.split("|")
            print("User:", user, ",Password:", str(fer.decrypt(passw.encode())) + "\n") 

def add():
    name = input("Account name: ")
    pwd = input("Password: ")
    
    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + str(fer.encrypt(pwd.encode())) + "\n")

while True:
      mode = input("Would you like to add a password or retrieve a password? (add/retrieve/quit) ").lower()
      if mode == 'quit':
        break
    
      if mode == 'view':
        view()
      elif mode == 'add':
        add()
      else:
        print("Invalid mode.")
        continue 
    