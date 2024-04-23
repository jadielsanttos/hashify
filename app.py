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

def hash_generate():
    hash = ""
    try:
        while True:
            option = input("Choose an option: ")
            text = input("Enter your text: ")
            encode = text.encode("UTF-8")

            if option == "1":
                hash = hashlib.md5(encode).hexdigest()
            elif option == "2":
                hash = hashlib.sha256(encode).hexdigest()
            else:
                print("Invalid option!")
                break

            hash_length = str(len(hash))

            print(" ")
            for i in range(0, int(hash_length)):
                print("=", end="")
            print(" ")
            print(hash)
            for i in range(0, int(hash_length)):
                print("=", end="")
            print(" ")
            
    except KeyboardInterrupt:
        print("\n Bye")

hash_generate()