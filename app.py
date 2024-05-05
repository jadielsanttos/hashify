from colorama import Fore
from time import sleep
import hashlib
import pyfiglet
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-H", "--Hash", help="Enter your hash")
parser.add_argument("-W", "--Wordlist", help="Enter your wordlist")
parser.add_argument("-G", "--Generate", help="You can generate your hash")
args = parser.parse_args()

hash = args.Hash
wordlist = args.Wordlist
text = args.Generate

print(Fore.CYAN+pyfiglet.figlet_format("HASHIFY"))
print(Fore.LIGHTWHITE_EX+"------------------")
print(Fore.LIGHTWHITE_EX+"Author: Th3 Want3d")
print(Fore.LIGHTWHITE_EX+"Version: 1.1")
print(Fore.LIGHTWHITE_EX+"------------------\n")

def hash_crack(hash, file):
    wordlist = open(file, "r")
    word_count = 1
    final_wordlist = wordlist.read().split()

    print("[!] hash ==> "+hash)
    print("[!] wordlist ==> "+file+"\n")

    try:
        for word in final_wordlist:
            new_word = word.replace("\n", "")

            encode = new_word.encode("UTF-8")
            
            print("--- attempt ["+str(word_count)+"] ==> "+new_word)
            sleep(0.5)
            
            if hash == hashlib.md5(encode).hexdigest():
                print("[+] 1 of 1 target successfully completed, valid text found: "+Fore.LIGHTGREEN_EX+new_word)
                break

            if len(final_wordlist) == word_count:
                print("[!] 1 of 1 target successfully completed, no valid text found")
                break
            word_count += 1

    except KeyboardInterrupt:
        print("\n Bye!")

def hash_generate(text):
    encode = text.encode("UTF-8")
    hash = hashlib.md5(encode).hexdigest()

    print("[+] hash generated ==> "+Fore.LIGHTGREEN_EX+hash)

if text:
    hash_generate(text)

if hash and wordlist:
    hash_crack(hash, wordlist)