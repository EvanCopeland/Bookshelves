#Programmers: Evan Copeland
#Date: 3/7/2022
#output: Main for bookshelf project
import creation
#have user decide whether to create a new collection, manage a collection, or search through all collections
x = int(input("Are you creating a new collection (1), accessing one (2) or searching through all collection (3), press other key to quit: "))
#check user decision
if (x == 1):
    #asks user for name and # of shelves of book collections
    name = str(input("please enter a name for the new collection: "))
    shelves = int(input("please enter the number of shelves this collection will be stored on: "))
    #create list
    array = creation.createlist()
    #sort list
    array = creation.bubblesort(array)
    #write sorted list to file
    creation.filecreation(name, array, shelves)
    #add file name to bookshelflist file
    file = open ("bookshelflist", "a")
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
    file = open(name, "r+")
    print(file.read())
    #edit # of shelves
    #binary search within file and determine shelf #
    #present file contents
    #add to file
    #remove from file
    print("option under construction")
elif (x == 3):
    #put all files into lists
    #allow binary search
    #present to user if found and in which lists on which shelf
    print("option under construction")
else:
    quit()
