import os
import sys
import fnmatch

path = sys.argv[1]

extensions = []
code_count = []
exclude = ['sample','exclude','description','png','jpg','config','HEAD','packed-refs','idx','master','pack','txt','index','gitignore']

def file_len(fname):
    i = 0
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 2

def get_extensions(path,excl):
    for root, dir, files in os.walk(path):
            for items in fnmatch.filter(files, "*"):
                temp_extensions = items.rfind(".")
                ext = items[temp_extensions+1:]

                if ext not in extensions:
                    if ext not in excl:
                        extensions.append(ext)
                        pass

def count_per_ext(path,extension):
    temp = 0
    for root, dir, files in os.walk(path):
            for items in fnmatch.filter(files, extension):
                value = root + "/" + items
                temp += file_len(value)
    code_count.append(temp)

get_extensions(path,exclude)

for run in extensions:
    count_per_ext(path,"*."+run)
    pass

for idx, val in enumerate(code_count):
    print extensions[idx] + ": " + str(code_count[idx])
    pass