import random
import string
import json 

#TODO's check if 2fa codes are alread pre existing, if they are generate again
#Create a login method


def generateFAkeys(length=4):
        characters = "" + string.punctuation + string.ascii_letters + string.digits
        twoFAkey = [] #List for the keys)
        while len(twoFAkey) < 3:
            key = (
                "".join(random.choice(characters) for i in range(length)) + "-" +
              "".join(random.choice(characters) for i in range(length)) + "-" +
              "".join(random.choice(characters) for i in range(length)) + "-" +
              "".join(random.choice(characters) for i in range(length))
            )
            if key not in twoFAkey:
                twoFAkey.append(key)
        return twoFAkey


print("Create an account = 2")


while True:
    choice = int(input("What would you like to do today? "))
    if choice == 2:
        username = input("What will you want your username to be? ")
        password = input("Please input your password you would like to use? ")
        account_keys = generateFAkeys()
        print("********************")
        print(f"Welcome {username}")
        print(f"Here are your 2 Factor Authentication tokens, please store them safe;")
        print(f"First key:  {account_keys[0]}")
        print(f"Secoond key:    {account_keys[1]}")
        print(f"Third Key:  {account_keys[-1]}")        
        break
    else:
        print("Create an account = 2")
        continue