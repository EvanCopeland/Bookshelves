def turnintolist(name):
    file = open(name, "r+")
    linelist = file.readlines()
    file.close()
    print(linelist)
    return linelist
