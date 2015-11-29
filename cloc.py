import os
import sys
import fnmatch
import StringIO
import csv

try:
    path = sys.argv[1]
except IndexError as e:
    path = input('file path: ')
try:
    exclude_file = sys.argv[2]
except IndexError as e:
    exclude_file = input('exclude file: ')

extensions = []
code_count = []
exclude = ['sample','exclude','description','png','jpg','config','HEAD','packed-refs','idx','master','pack','txt','index','gitignore']
folder_exclude = ['.git']
total = 0

try:
    exclude_file
except NameError:
    pass
else:
    with open(exclude_file, 'r+') as f:
        content = f.read().replace('\n', '')

    reader = csv.reader(content.split('\n'), delimiter=',')
    for row in reader:
        exclude += row

def file_len(fname):
    i = 0
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 2

def get_extensions(path,excl,folder_excl):
    for root, dir, files in os.walk(path): 
            for items in fnmatch.filter(files, "*"):

                temp_extensions = items.rfind(".")

                # Remove any folders that are meant to be excluded from the search
                for x in folder_excl:
                    if x in dir:
                        dir.remove(x)
                    pass

                ext = items[temp_extensions+1:]

                # If the file is not in the exclude list, add it into the array
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

get_extensions(path,exclude,folder_exclude)

for run in extensions:
    count_per_ext(path,"*."+run)
    pass

print '\n'
print '\tLines of code by extension'
print '\t---------------------------'
print ''
print '\tExtension \t\tLine Count'
print '\t--------- \t\t----------'

for idx, val in enumerate(code_count):
    count = code_count[idx]-1
    total += count
    if len(extensions[idx]) > 10:
        t = '\t'
    elif len(extensions[idx]) > 7:
        t = '\t\t'
    else:
        t = '\t\t\t'
    print '\t' + extensions[idx] + ": " + t + str(count)
    pass

print '\t\t\t'
print '\tTotal: \t\t\t' + str(total)
print '\n'