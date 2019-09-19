from os import listdir
from os.path import isfile, join, isdir
import operator
import json

'''
mkdir DELPHI 
mkdir PYTHON
mkdir ПАРАЛЛЕЛЬНОЕ\ ПРОГРАММИРОВАНИЕ
mkdir C++ 
mkdir DEVOPS 
mkdir R 
mkdir \!unsorted 
mkdir Технотрек
mkdir FPGA 
mkdir RUST 
mkdir VIM 
mkdir УПРАВЛЕНИЕ\ РАЗРАБОТКОЙ
mkdir \!cloud 
mkdir JAVA 
mkdir \!theory 
mkdir МАШИННОЕ\ ОБУЧЕНИЕ 
mkdir ЧИТАЛЬНЫЙ\ ЗАЛ
mkdir \!db 
mkdir \!mining 
mkdir \!trading 
mkdir НАСТРОЙКА\ LINUX
'''

my_path_dir = "~/Документы/"
only_dirs = [f for f in listdir(my_path_dir) if isdir(join(my_path_dir, f)) and not str(f).__contains__("!")]


for d in only_dirs:
    my_path = my_path_dir + d + "/"
    print("\r\n" + my_path)
    only_files = [f for f in listdir(my_path) if isfile(join(my_path, f)) and str(f).__contains__(".txt")]

    tags = []
    for fn in only_files:
        # print(fn)
        lnfn = str(my_path + fn)
        with open(lnfn, 'r') as file:
            while True:
                l = file.readline()
                if l.__contains__("tags:"):
                    t = l.replace("tags:", "").strip().strip("[]").split(",")
                    tags += [j.strip().strip("'").strip("*").strip() for j in t]
                    break

    # print(set(tags))
    m = {i: 0 for i in set(tags)}

    for i in tags:
        m[i] += 1

    sorted_x = sorted(m.items(), key=operator.itemgetter(1))
    sorted_x.reverse()

    print( sorted_x )

    with open(my_path + "folder.info", 'w') as file:
        file.write(json.dumps(m, ensure_ascii=False))
