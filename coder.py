import os
import random
import sys
import re

def baner():
    print ("'#Coder : XMrBeazD'")
    print ("'#Metode : Python'")
    print ("'\033[1;91m[~>>] Pilih yang anda mau Install :\033[1;0m'")
    print ("'\033[1;97m{\033[1;95m01\033[1;97m}\033[1;96m pkg Update && pkg Upgrade'")
    print ("'\033[1;97m{\033[1;95m02\033[1;97m}\033[1;96m Apt Update && Apt Upgrade'")
    print ("'\033[1;97m{\033[1;95m03\033[1;97m}\033[1;96m Python2'")
    print ("'\033[1;97m{\033[1;95m04\033[1;97m}\033[1;96m Python3'")
    print ("'\033[1;97m{\033[1;95m05\033[1;97m}\033[1;96m Bash'")
    print ("'\033[1;97m{\033[1;95m00\033[1;97m}\033[1;91m Exit\033[00m'")
    print ("'\033[1;94m_____________________________________'")
    
def load():
     f=input("'\033[1;97m[\033[1;91m?\033[1;97m]PILIH : \033[1;96m'")
     if f == "01" or f == "1":
        load()
        print ("'\033[91m[~>>] Tunggu System Sedang Loading\033[0m'")
        os.system("pkg update && pkg upgrade")
        kembali()
     elif f == "02" or f == "2":
        load()
        print ("'\033[91m[~>>] Tunggu System Sedang Loading\033[0m'")
        os.system("apt update && apt upgrade")
        kembali()
     elif f == "03" or f == "3":
        load()
        print ("'\033[91m[~>>] Tunggu System Sedang Loading\033[0m'")
        os.system("pkg install python2")
        kembali()
     elif f == "04" or f == "4":
        load()
        print ("'\033[91m[~>>] Tunggu System Sedang Loading\033[0m'")
        os.system("pkg install python3")
        kembali()
     elif f == "05" or f == "5":
        load()
        print ("'\033[91m[~>>] Tunggu System Sedang Loading\033[0m'")
        os.system("pkg install bash")
        kembali()
     elif f == "00" or f == "0":
          exit()
     else:
          print ("'\033[1;97m[\033[1;91m!\033[1;97m]Wrong Input\033[1;91m!!\033[00m)'")
          kembali() 

