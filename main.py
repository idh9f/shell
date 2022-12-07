import os
import sys
import keyboard
import psutil
import time
from tqdm import tqdm
from time import sleep
import psutil
import threading


usrpath = f"C:\\Users\\{os.getlogin()}"

def THREAD(func):
    threading.Thread(target=func).start()

def whoami():
    print(os.getlogin())


def echo(param):
    print(param)


def ls():
    print(cwd)
    scn = os.scandir(cwd)
    print("\n"+"files at "+f"{cwd}"+"\n")
    for i in scn:
        print("\t|\n\t|___>"+i.name)


def touch(fname):
    f = open(fname, "w+")
    f.close()


def cat(fname):
    with open(fname, 'r') as file:
        cont = file.readline()
        if cont == "" or cont == " ":
            print("file is empty!")
        else:
            print(cont)


def mkdir(fname):
    print(f"created directory at {cwd}")
    os.makedirs(fname)


def rm(fname):
    os.remove(fname)


def rmdir(fname):
    os.removedirs(fname)


def cls():
    os.system("cls")


def about():
    os.system("winver")
ext = None
def read_and_exit():
    global ext
    ext = keyboard.read_key()
    if ext == 'q':
        return ext
        

def status():

    with tqdm(total=100, desc='cpu%', position=1) as cpubar, tqdm(total=100, desc='ram%', position=0) as rambar:

        while True:
            THREAD(read_and_exit)
            rambar.n=psutil.virtual_memory().percent
            cpubar.n=psutil.cpu_percent()
            rambar.refresh()
            cpubar.refresh()
            sleep(0.5)
            global ext
            if ext == 'q':
                break
            else:
                pass
    




def cd(dirname: str):
    global cwd
    cwd = f"{cwd}\\{dirname}"


database_with_param = {"echo": echo,
                       "touch": touch,
                       "cat": cat,
                       "mkdir": mkdir,
                       "rm": rm,
                       "rmdir": rmdir,
                       "cd": cd
                       }
database_without_param = {
    "whoami": whoami,
    "ls": ls,
    "cls": cls,
    "exit": sys.exit,
    "winver": about,
    "stat": status
}


os.chdir(usrpath)

print("""
\t\t\t\t\t\t                
\t\t\t\t\t\t ____   _____   ____  _   _ 
\t\t\t\t\t\t|  _ \ |  _  | / ___|| | | |
\t\t\t\t\t\t| |_| || | | || |__  | | | |
\t\t\t\t\t\t|    / | |_| | \__ \ | |_| |
\t\t\t\t\t\t|  _ \ |  _  |    | ||  _  |
\t\t\t\t\t\t| |_| || | | | ___| || | | |
\t\t\t\t\t\t|____/ |_| |_||____/ |_| |_|""")
time.sleep(3)

global cwd
cwd = usrpath
while True:
    usr = str(input(f"{cwd} $ "))
    if usr == '':
        continue

    elif usr in database_without_param:
        database_without_param[usr]()
    elif usr.split()[0] in database_with_param:
        command, args = usr.split()
        database_with_param[command](args)
    elif usr not in database_with_param and usr not in database_without_param:
        print(f"command:{usr} :not found!")
