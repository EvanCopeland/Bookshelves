#Programmers: Evan Copeland
#Date: 3/7/2022
#output: Main for bookshelf project
import creation
#have user decide whether to create a file, access a file, or search through all files
x = int(input("Are you creating a new file(1), accessing one(2), or searching through all files (3)"))
#check user decision
if (x == 1):
    #asks user for name of book collection
    name = str(input("please enter a name for the new collection: "))
    #create list
    array = creation.createlist()
    #sort list
    array = creation.bubblesort(array)
    #write sorted list to file
    creation.filecreation(name, array)
    #add file name to bookshelflist file
    file = open ("bookshelflist", "a")
    file.write(name)
    file.close()
elif (x == 2):
    #display files
    #have user choose file
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
    print("option not available")
        
    
