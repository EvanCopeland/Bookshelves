#Programmers: Evan Copeland
#Date: 3/7/2022
#output: Main for bookshelf project
import creation
import management
from isbntools.app import *

#have user decide whether to create a new collection, manage a collection, or search through all collections
x = 0
while(x != 7):

    x = int(input("\n1. Are you creating a new collection\n2. accessing one collection\n3. or searching through all collections\nenter 7 to quit: "))
#check user decision
    if (x == 1):

        #asks user for name and # of shelves of the book collection
        name = str(input("please enter a name for the new collection: "))
        shelves = int(input("please enter the number of shelves this collection will be stored on: "))

        #create and sort list and write list to file
        array = creation.createlist()
        array = creation.bubblesort(array)
        creation.filecreation(name, array, shelves)

        #add file name to bookshelflist file
        file = open("bookshelflist", "a")
        file.write(name)
        file.write("\n")
        file.close()

    elif (x == 2):

        #display files through bookshelflist and have user choose file from bookshelflist
        file = open("bookshelflist", "r")
        print(file.read())
        file.close()
        name = str(input("which collection would you like to access? "))
        
        #operations to be performed on file
        x = int(input("What operation would you like to perform?\n1. display books in "+name+"\n2. edit shelf numbers in "+name+"\n3. search "+name+" for book\n4. add book to "+name+"\n5. remove book from "+name+"\n6. look up new book for "+name+"\n"))
        def choices(x):
            match x:
                case 1:

                    #display books
                    linelist = management.turnintolist(name)
                    for i in range (len(linelist)):
                        linelist[i] = linelist[i].strip()
                        print(linelist[i]+"\n")
                    management.backtolist(name, linelist)
                    return
                    
                case 2:

                    #edit # of shelves
                    linelist = management.turnintolist(name)
                    currentshelves = linelist[0]
                    print("current number of shelves = "+currentshelves)
                    newshelves = str(input("please enter new number of shelves: "))
                    linelist[0] = "shelves: "+newshelves+"\n"
                    file = open(name, "w")
                    for i in range (len(linelist)):
                        file.write(linelist[i])
                    file.close()
                    return

                case 3:

                    #search and shelf #
                    search = str(input("please enter the book you are searching for"))
                    management.linearsearch(name, search)

                case 4:

                    #add book to file
                    newbook = str(input("enter the name of the book you have acquired: "))
                    file = open(name, "a")
                    file.write("\n"+newbook)
                    file.close()
                    print("book added!")

                    #sort the file contents
                    linelist = management.turnintolist(name)

                    #strip the line list elements of new lines
                    for i in range (len(linelist)-1):
                        linelist[i] = linelist[i].strip()

                    #store shelf # and remove from line list
                    shelves = linelist[0]
                    linelist.remove(shelves)

                    #call sort function to sort
                    linelist = creation.bubblesort(linelist)
                    file = open(name,"w")

                    #add shelf # back into line list and write back to file
                    linelist[0] = shelves
                    management.backtolist(name, linelist)
                    print("done!")
                    return

                case 5:

                    #remove from file
                    oldbook = str(input("what is the name of the book you would like to get rid of?"))
                    linelist = management.turnintolist(name)
                    for i in range (len(linelist)):
                        linelist[i] = linelist[i].strip()
                    linelist.remove(oldbook)
                    management.backtolist(name, linelist)
                    print("book removed")
                    return

                case 6:

                    #get prompt from user, find isbn from prompt
                    prompt = str(input("enter key words (I.E: author, title, series) for the book you want to add to "+name+": "))
                    isbn = isbn_from_words(prompt)
                    print("\nISBN: " + isbn)

                    #search isbn on google
                    print("\nsearching on google...")
                    try:
                        from googlesearch import search
                    except ImportError:
                        print("google module not working :(")
                    query = isbn
                    for i in search(query, tld = "com", num = 10, stop = 10, pause = 4):
                        print(i)
                       
        choices(x)

    elif (x == 3):

        #get book to be searched for, retrieve list from bookshelflist
        search = str(input("enter book you are looking for: "))
        linelist = management.turnintolist("bookshelflist")
        print(linelist)
        for i in range (len(linelist)):
            linelist[i] = linelist[i].strip()

        # use each element in line list to prompt search for each element in line list
        for i in range (len(linelist)):
            print("searching in collection: " + linelist[i])
            management.linearsearch(linelist[i], search)

        #return list to bookshelflist
        file = open("bookshelflist", "w")
        for i in range (len(linelist)):
            file.write(linelist[i])
            file.write("\n")
        file.close()
    else:

        #tell user they chose an invalid option
        print("not a valid option")
        quit()
quit()
