from os import listdir
from os.path import join, isdir
import grab

my_path_dir = "~/tmp/"
only_txt = [f for f in listdir(my_path_dir) if not isdir(join(my_path_dir, f)) and str(f).__contains__(".txt")]
http_cl = grab.Grab()

for lfn in only_txt:
    my_path = my_path_dir + lfn
    print("\r\n" + my_path)
    d = {}
    with open(my_path) as fp:
        for l in fp:
            if l.__contains__("head:"):
                h = l.replace("head:", "").strip()
                d["head"] = h
            if l.__contains__("file:"):
                f = l.replace("file:", "").strip()
                d["file"] = f
            if l.__contains__("url:"):
                u = l.replace("url:", "").strip()
                d["url"] = u

    print(d)
    http_cl.go(d["url"])
    if http_cl.response.code != 200:
        continue

    tags = []
    c = len(http_cl.xpath('/html/body/div[1]/div[3]/main/div/div/div[1]').getchildren())
    for i in range(c):
        t = http_cl.xpath_text('/html/body/div[1]/div[3]/main/div/div/div[1]/div['+str(i+1)+']')
        tags.append(t)
    print(tags)

    with open(my_path, 'w') as file:
        file.write('head: {}\n'.format(d["head"]))
        file.write('file: {}\n'.format(d["file"]))
        file.write('tags: {}\n'.format(tags))
        file.write('url: {}\n'.format(d["url"]))
