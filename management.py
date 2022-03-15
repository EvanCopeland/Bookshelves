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
def linearsearch(name, search):
    search = search+"\n"
    linelist = turnintolist(name)
    shelves = linelist[0]
    linelist.remove(shelves)

    shelves = ord(shelves[9])-48

    bookspershelf = (len(linelist)+1)/shelves

    for i in range(len(linelist)):
        if(linelist[i] == search):
            shelfnumber = round((i+1)/bookspershelf)
            search2 = search.strip()
            neighbor1 = linelist[i-1].strip()
            print(search2 + " found on shelf " +str(shelfnumber) + " next to " + neighbor1)
    file = open(name, "w")
    file.write("shelves: " + chr(shelves + 48) + "\n")
    
    for i in range (len(linelist)):
        file.write(linelist[i])
    file.close()
    return
    
