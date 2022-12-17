import os
import sys
import keyboard
import psutil
import colorama
from tqdm import tqdm
from time import sleep
import threading
import time

usrpath = f"C:\\Users\\{os.getlogin()}"


def THREAD(func):
    threading.Thread(target=func).start()


def whoami():
    print(os.getlogin())


def echo(param):
    print(param)


def ls():
    global cwd
    print(cwd)
    scn = os.scandir(cwd)

    print(colorama.Back.LIGHTCYAN_EX+"\n" +
          "files at "+f"{cwd}"+colorama.Back.RESET+"\n")

    for i in scn:
        info = os.stat(i)
        
        if info.st_file_attributes == 8208  or info.st_file_attributes == 38:
            pass
        else:
            if i.is_dir:
                print(colorama.Fore.BLUE+i.name)
    
            


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
        return


def run(executable: str):
    if os.path.exists(f"{cwd}\\{executable}"):
        os.system(f"{cwd}\\{executable}")
    elif os.path.exists(executable):
        os.system(executable)


def status():

    with tqdm(total=100, desc='cpu%', position=1) as cpubar, tqdm(total=100, desc='ram%', position=0) as rambar:

        while True:
            THREAD(read_and_exit)
            rambar.n = psutil.virtual_memory().percent
            cpubar.n = psutil.cpu_percent()
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
    print(dirname)
    os.chdir(dirname)
    if os.path.exists(dirname):
        cwd = dirname

    elif os.path.exists(f"{cwd}\\{dirname}"):

        cwd = f"{cwd}\\{dirname}"
    else:
        print("error: Directory does not exists")



commands_with_param = {"echo": echo,
                       "touch": touch,
                       "cat": cat,
                       "mkdir": mkdir,
                       "rm": rm,
                       "rmdir": rmdir,
                       "cd": cd,
                       "rn": run
                       }
commands_without_param = {
    "whoami": whoami,
    "ls": ls,
    "cls": cls,
    "exit": sys.exit,
    "winver": about,
    "stat": status
}


cls()
print("""
\t\t\t\t\t\t                
\t\t\t\t\t\t ____   _____   ____  _   _ 
\t\t\t\t\t\t|  _ \ |  _  | / ___|| | | |
\t\t\t\t\t\t| |_| || | | || |__  | | | |
\t\t\t\t\t\t|    / | |_| | \__ \ | |_| |
\t\t\t\t\t\t|  _ \ |  _  |    | ||  _  |
\t\t\t\t\t\t| |_| || | | | ___| || | | |
\t\t\t\t\t\t|____/ |_| |_||____/ |_| |_|""")
time.sleep(2)
cls()

cwd = usrpath
while True:
    usr = str(input(colorama.Fore.LIGHTRED_EX+""+colorama.Fore.BLACK+colorama.Back.LIGHTRED_EX+"  "+cwd+colorama.Back.RESET+colorama.Fore.LIGHTRED_EX+""+"\n"+colorama.Fore.LIGHTRED_EX +
              colorama.Fore.LIGHTGREEN_EX+"⚡"+colorama.Fore.MAGENTA + f"{os.getlogin()} "+colorama.Back.RESET+colorama.Fore.LIGHTGREEN_EX+">"+colorama.Fore.RESET+colorama.Fore.RESET+" "))
    if usr == '':
        continue

    elif usr in commands_without_param:
        commands_without_param[usr]()
    elif usr.split()[0] in commands_with_param:
        try:
            command, args = usr.split()
            commands_with_param[command](args)
        except ValueError as e:
            print(e)
    elif usr not in commands_with_param and usr not in commands_without_param:
        print(f"{usr}:command not found!")
