from random import shuffle, seed
import time


def encrypt(text, dictionary):
    encrypted_text = ""
    for char in text:
        if char in dictionary:
            encrypted_text += dictionary[char]
        else:
            encrypted_text += char
    return encrypted_text


def decrypt(encrypted_text, dictionary):
    decrypted_text = ""
    for char in encrypted_text:
        found = False
        for key, value in dictionary.items():
            if value == char:
                decrypted_text += key
                found = True
                break
        if not found:
            decrypted_text += char
    return decrypted_text


seed_input = input("Input Seed Number > ")
seed_str = int(seed_input)


def encryption_lib(seed_str):
    seed(seed_str)
    alphabet = [chr(i) for i in range(32, 127)]
    shuffled_alphabet = alphabet.copy()
    shuffle(shuffled_alphabet)
    dictionary = dict(zip(alphabet, shuffled_alphabet))
    return dictionary


function_input = input("What would you like to do? (1 - Encrypt / 2 - Decrypt) > ")

if function_input == "1":
    file_dir = input("Input File Directory > ")
    with open(file_dir, "r") as file:
        txt_encrypt = file.read()
    dictionary = encryption_lib(seed_str)
    encrypted_txt = encrypt(txt_encrypt, dictionary)
    with open(file_dir, "w") as file:
        file.write(encrypted_txt)
    print("File Overwritten With Encrypted Text.")

elif function_input == "2":
    file_dir = input("Input File Directory > ")
    with open(file_dir, "r") as file:
        txt_decrypt = file.read()
    dictionary = encryption_lib(seed_str)
    decrypted_txt = decrypt(txt_decrypt, dictionary)
    with open(file_dir, "w") as file:
        file.write(decrypted_txt)
    print("File Overwritten With Decrypted Text.")

print("")
print("This window will close soon...")
time.sleep(12)
