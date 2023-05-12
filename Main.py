import os
import time
import random
import hashlib
import requests

# --- #


def Clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def Banner():
    Clear()
    print("""  _____        __      _____            
 / ____|      / _|    / ____|           
| (___   __ _| |_ ___| |  __  ___ _ __  
 \___ \ / _` |  _/ _ \ | |_ |/ _ \ '_ \ 
 ____) | (_| | ||  __/ |__| |  __/ | | |
|_____/ \__,_|_| \___|\_____|\___|_| |_|
                                        
By : Pale-Hacker\n""")


def Check_Password(Password):
    Sha1_Password = hashlib.sha1(Password.encode('utf-8')).hexdigest().upper()
    Prefix, Suffix = Sha1_Password[:5], Sha1_Password[5:]
    Url = f"https://api.pwnedpasswords.com/range/{Prefix}"
    Res = requests.get(Url)
    if Res.status_code != 200:
        raise RuntimeError(f"Error : {Res.status_code}")
    Hashes = (line.split(':') for line in Res.text.splitlines())
    Count = next((int(Count) for t, Count in Hashes if t == Suffix), 0)
    if Count:
        print(f"The Password ' {Password} ' Has Been Leaked - {Count} Times !")
    else:
        print(f"The Password ' {Password} ' Has Not Been Leaked.")

# --- #


def Main():
    Banner()

    Main_Input = input(
        "1. Generate Password \n2. Check Password \n3. Exit \n\n#$> ")

    # --- #

    if Main_Input == "1":
        Banner()
        Password_Length = int(input("Password Length : "))
        String = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
        Password = ''.join(random.choice(String)
                           for i in range(Password_Length))
        Banner()
        print("Your Password Is : "+Password)
        Banner()
        print("Your Password Is : "+Password+"\n")
        Check_Password(Password)
        input("\nPress \"Enter\" To Exit ! ")
        exit()
    elif Main_Input == "2":
        Banner()
        Password = input("Enter Password To Check : ")
        Banner()
        Check_Password(Password)
        input("\nPress \"Enter\" To Exit ! ")
    elif Main_Input == "3":
        exit()
    else:
        print("Select a Valid Selection !")
        time.sleep(1.5)
        Main()

# --- #


if __name__ == "__main__":
    Main()

# --- #
