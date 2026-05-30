import os

def load_dictionary(filename):
    with open(filename, "r", encoding='utf-8') as f:
        text = f.read()
        print(text)


base = input()
def listAll(path):
    if (os.path.isfile(path)):
        load_dictionary(path)
        return
    dirfiles = os.listdir(path)
    #print(dirfiles)
    subdirs = [path + "\\" + x for x in dirfiles]
    print(path)
    print(subdirs)
    for subdir in subdirs:
        listAll(subdir)

listAll(base)