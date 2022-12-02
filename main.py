import os
import sys
import colorama
import psutil
import time

fname = r"\\testlib.so"

path = os.getcwd()
usrpath = f"C:\\Users\\{os.getlogin()}"
dllpath = path + fname

def whoami():
    print( os.getlogin())

def echo(param):
    print(param) 
def ls():
    scn = os.scandir(usrpath)
    print("\n"+"files at "+f"{usrpath}"+"\n")
    for i in scn:
        print("\t"+i.name)
def touch(fname):
    f = open(fname,"w+")
    f.close()
def cat(fname):
    with open(fname,'r') as file:
        cont = file.readline()
        if cont == "" or cont == " ":
            print("file is empty!")
        else:
            print(cont)
def mkdir(fname):
    print(f"created directory at {path}")
    os.makedirs(fname)

def rm(fname):
    os.remove(fname)

def rmdir(fname):
    os.removedirs(fname)
def cls():
    os.system("cls")

def about():
    os.system("winver")
def status():
    print(psutil.version_info)

def cd(dirname:str):
    global cwd
    cwd = os.chdir(f"{cwd}\\{dirname}")
    print(f"{cwd}\\{dirname}")


database_with_param = {"echo":echo,
                        "touch" : touch,
                        "cat" :cat,
                        "mkdir" : mkdir,
                        "rm" :rm,
                        "rmdir":rmdir,
                        "cd" : cd
                            }
database_without_param = {
            "whoami":whoami,
            "ls" : ls,
            "cls":cls,
            "exit":sys.exit,
            "winver":about,
            "stat" : status
                }

os.system("cls")
os.chdir(usrpath)

print("""
\t\t\t\t\t\t _               _
\t\t\t\t\t\t ____   _____   ____  _   _ 
\t\t\t\t\t\t|  _ \ |  _  | / ___|| | | |
\t\t\t\t\t\t| |_| || | | || |__  | | | |
\t\t\t\t\t\t|    / | |_| | \__ \ | |_| |
\t\t\t\t\t\t|  _ \ |  _  |    | ||  _  |
\t\t\t\t\t\t| |_| || | | | ___| || | | |
\t\t\t\t\t\t|____/ |_| |_||____/ |_| |_|""")
time.sleep(3)
os.system("cls")
global cwd
cwd = usrpath
while True:
    usr = str(input(f"{usrpath} $ "))
    if usr == '':
        continue
        

    elif usr in database_without_param:
        database_without_param[usr]()
    elif usr.split()[0] in database_with_param:
        command,args = usr.split()
        database_with_param[command](args)
    elif usr not in database_with_param and usr not in database_without_param:
        print(f"command:{usr} :not found!")