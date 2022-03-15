def turnintolist(name):
    file = open(name, "r+")
    linelist = file.readlines()
    file.close()
    print(linelist)
    return linelist
def backtolist(name, linelist):
    file = open(name, "w")
    for i in range (len(linelist)):
        file.write(linelist[i])
        file.write("\n")
    file.close()
    return
