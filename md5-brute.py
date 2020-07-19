#!/usr/bin/python3

import os
import sys
import itertools
import hashlib
import time
import threading
from colorama import Fore


#============info============
def info():
    info = """
    ===========================================================
    =                                                         =
    =                   Simple MD5-BruteForce                 =
    =                                                         =
    =                    Auther : P3NT3ST0R                   =
    =                                                         =
    =                      Version : 0.1                      =
    =                                                         =
    =                                                         =
    =   github.com/pentestor                                  =
    ===========================================================

    """
    print(info)
    time.sleep(3)
    os.system("cls" if os.name in 'nt' else "clear")

#==========help============

def help(message = None):
    h = """
    Usage :
        python md5-brute.py Min Max Ruls Hash

    Example:
        python md5-brute.py 1 10 abcdefghijklmnopqrstuvwxyz0123456789 0cc175b9c0f1b6a831c399e269772661

    """
    print(Fore.RED+h+Fore.RESET)
    sys.exit(message)



#========Animate==========
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done == True:
            break        
        sys.stdout.write('\rloading ' + c)
        sys.stdout.flush()
        time.sleep(0.5)


if len(sys.argv) <= 1:
    info()
    help()

else:
    try:
        min = int(sys.argv[1])
        max = int(sys.argv[2])
        rule = str(sys.argv[3])
        input_hash = str(sys.argv[4])
    except IndexError :
        print('Bad Usage....see Help')
        help("Try again!")

done = False

for m in range(min,max+1):
    os.system("cls" if os.name in 'nt' else "clear")
    print(Fore.BLUE+f' Please wait Try For {m} character'+Fore.RESET)
    t = threading.Thread(target=animate)
    t.start()
    for ps in itertools.product(rule, repeat=m):
        passwd = "".join(ps)
        m = hashlib.md5()
        m.update(passwd.encode())
        hash_test = m.hexdigest()
        if hash_test == input_hash :
            print(Fore.GREEN+f"Found Password : {passwd}"+Fore.RESET)
            done = True
            sys.exit()