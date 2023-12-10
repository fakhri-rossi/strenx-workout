import os

path = "./routines/"

for (root,dirs,files) in os.walk(path):
    for file in files:
        if ".txt" in file:
            print(file[:-4])
