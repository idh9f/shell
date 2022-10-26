import ctypes
from fileinput import filename
import os

filename1 = r"\\testlib.so"

path = os.getcwd()
path = path + filename1
testlib = ctypes.CDLL(path)
print(testlib.ver())