import itertools


CORRECT_PASSWORD = "anu" 

DICTIONARY_FILE = "dictionary.txt"

def dictionary_attack():

    try:
        with open(DICTIONARY_FILE, "r") as file:
            for password in file:
                password = password.strip() 
                print(f"Trying password: {password}")
                if password == CORRECT_PASSWORD:
                    print(f"Success! Password found: {password}")
                    return True
    except FileNotFoundError:
        print("Dictionary file not found. Skipping dictionary attack.")
    
    print("Dictionary attack failed.")
        print("Dictionary attack failed.")
    return False


def brute_force_attack():
   
    print("Starting brute force attack...")


    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for password_tuple in itertools.product(chars, repeat=5):  
        password = "".join(password_tuple)
        print(f"Trying password: {password}")

        if password == CORRECT_PASSWORD:
            print(f"Success! Password found: {password}")
            return True

    print("Brute force attack failed.")
    return False


if __name__ == "__main__":
    username = input("Enter username: ")
    print(f"Hello, {username}. Attempting to crack the password...")
        print(f"Hello, {username}. Attempting to crack the password...")

    if not dictionary_attack():
        
        brute_force_attack()


