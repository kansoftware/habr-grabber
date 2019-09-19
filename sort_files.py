from os import listdir
from os.path import isfile, join, isdir
import shutil


my_path_dir = "~/Документы/"
only_dirs = [f for f in listdir(my_path_dir) if isdir(join(my_path_dir, f)) and not str(f).__contains__("!")]

dir_raw_files = my_path_dir + "!unsorted/"

with open('tags_addons.txt', 'r') as file:
    lines = file.readlines()

add_tags=dict()
for l in lines:
    main,raw_tags = l.upper().strip().split("=")
    tags = raw_tags.split(",")
    add_tags[main]=tags
    #print(main +'=>'+ tags)

my_path = dir_raw_files
print("\r\n" + my_path)
only_files = [f for f in listdir(my_path) if isfile(join(my_path, f)) and str(f).__contains__(".txt")]

for fn in only_files:
    # print(fn)
    lnfn = str(my_path + fn)
    tags = None
    with open(lnfn, 'r') as file:
        while True:
            l = file.readline()
            if l.__contains__("tags:"):
                t = l.replace("tags:", "").strip().strip("[]").split(",")
                tags = [j.strip().upper().strip("'").strip("*").strip() for j in t]
                # print(tags)

                break

    home_folder = set(tags) & set(only_dirs)
    if len(home_folder) >= 1:
        shutil.move(lnfn, my_path_dir + list(home_folder)[0]+"/")
        shutil.move(lnfn.replace(".txt", ".pdf"), my_path_dir + list(home_folder)[0] + "/")
    else:
        catched = False
        for k in add_tags.keys():
            v = add_tags[k]
            folders = set(tags) & set(v)
            if len(folders) >= 1:
                shutil.move(lnfn, my_path_dir + k + "/")
                shutil.move(lnfn.replace(".txt", ".pdf"), my_path_dir + k + "/")
                print(lnfn + "=>" + my_path_dir + k + "/")
                catched = True
                break

        if not catched:
            print(lnfn)
            #print(home_folder)
