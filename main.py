import os
import sys
import ctypes
import psutil

fname = r"\\testlib.so"

path = os.getcwd()
path = path + fname
funcs = ctypes.CDLL(path)

def whoami():
    print( os.getlogin())

def echo(param):
    print(param) 
def ls():
    scn = os.scandir(cwd)
    print("\n"+"files at "+f"{cwd}"+"\n")
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
def status():
    print(psutil.version_info)

database_with_param = {"echo":echo,
                        "touch" : touch,
                        "cat" :cat,
                        "mkdir" : mkdir,
                        "rm" :rm,
                        "rmdir":rmdir 
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
cwd = fr"C:\\Users\\{os.getlogin()}"
os.chdir(cwd)


while True:
    usr = str(input("$ "))
    if usr in database_without_param:
        database_without_param[usr]()
    elif usr.split()[0] in database_with_param:
        command,args = usr.split()
        database_with_param[command](args)