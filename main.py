#Programmers: Evan Copeland
#Date: 3/7/2022
#output: Main for bookshelf project
import creation
#have user decide whether to create a new collection, manage a collection, or search through all collections
x = int(input("Are you creating a new collection (1), accessing one collection(2) or searching through all collections (3), press other key to quit: "))
#check user decision
if (x == 1):
    #asks user for name and # of shelves of the book collection
    name = str(input("please enter a name for the new collection: "))
    shelves = int(input("please enter the number of shelves this collection will be stored on: "))
    #create list
    array = creation.createlist()
    #sort list
    array = creation.bubblesort(array)
    #write sorted list to file
    creation.filecreation(name, array, shelves)
    #add file name to bookshelflist file
    file = open("bookshelflist", "a")
    file.write(name)
    file.write("\n")
    file.close()
elif (x == 2):
    #display files
    file = open("bookshelflist", "r")
    #read contents
    print(file.read())
    file.close()
    #have user choose file
    name = str(input("which collection would you like to access? "))
    x = int(input("What operation would you like to perform?\n1. display collection contents\n2. edit shelf number\n3. search collection for book\n4. add to collection\5. remove from collection\n6. look up new book\n"))
    #create
    def choices(x):
        match x:
            case 1:
                file = open(name, "r+")
                print(file.read())
                return
            case 2:
                #edit # of shelves
                file = open(name, "r+")
                linelist=file.readlines()
                currentshelves = linelist[0]
                print("current number of shelves = "+currentshelves)
                newshelves = str(input("please enter new number of shelves: "))
                linelist[0] = "shelves: "+newshelves+"\n"
                file.close()
                file = open(name, "w")
                for i in range (len(linelist)):
                    file.write(linelist[i])
                file.close()
                return
            case 3:
                #search and shelf #
                search = str(input("please enter book you are searching for"))
                search = search+"\n"
                file = open(name, "r+")
                linelist = file.readlines()
                file.close()
                shelves = linelist[0]
                linelist.remove(shelves)
                #converting ascii value of shelf number to its original integer value
                shelves = ord(shelves[9])-48
                #finding books per shelf for shelf # calculation
                bookspershelf = (len(linelist)+1)/shelves
                #searching
                for i in range(len(linelist)):
                    if(linelist[i] == search):
                        shelfnumber = round((i+1)/bookspershelf)
                        print(search + " found on shelf "+ str(shelfnumber) + " next to "+ linelist[i-1] + " and "+linelist[i+1])
                file = open(name,"w")
                file.write("shelves: " + chr(shelves+48) + "\n")
                for i in range (len(linelist)):
                    file.write(linelist[i])
                file.close()
                return
            case 4:
                #add to file
                newbook = str(input("enter the name of the book you have acquired: "))
                file = open(name, "a")
                file.write("\n"+newbook)
                #sort file 
                print("book added!")
                return
            case 5:
                #remove from file
                return
            case 6:
                #look up book
                return
    choices(x)
    print("option under construction")
elif (x == 3):
    #put all files into lists
    #allow binary search
    #present to user if found and in which lists on which shelf
    print("option under construction")
else:
    quit()
