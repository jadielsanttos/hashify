from colorama import Fore
import hashlib
import pyfiglet

tool_name = "HASHIFY"

print(Fore.CYAN+pyfiglet.figlet_format(tool_name))
print("Author: Jadiel Santos")
print("Version: 1.0"+"\n")

print("#=====================#")
print("|[1] -> MD5           |")
print("|[2] -> SHA256        |")
print("#=====================#"+"\n")

option = input("Choose an option: ")
text = input("Enter your text: ")

def hash_generate(text, option):
    encode = text.encode("UTF-8")

    hash = ""

    if option == "1":
        hash = hashlib.md5(encode).hexdigest()
    else:
        hash = hashlib.sha256(encode).hexdigest()

    hash_length = str(len(hash))

    print(" ")
    for i in range(0, int(hash_length)):
        print("=", end="")
    print(" ")
    print(hash)
    for i in range(0, int(hash_length)):
        print("=", end="")
    print(" ")

hash_generate(text, option)