#Programmers: Evan Copeland
#Date: 3/7/2022
#output: Main for bookshelf project

#have user decide whether to create a file, access a file, or search through all files
x = int(input("Are you creating a new file(1), accessing one(2), or searching through all files (3)"))
array = []
#check user decision
if (x == 1):
    #ask user for name of bookshelf
    name = str(input("please enter a name for the new collection: "))
    #have user create list
    book = ""
    while( book != "done"):
        book = str(input("please enter book title, type done to finish: "))
        array.append(book)
    print("sorting...")
    #sort list
    for i in range (len(array)):
        for j in range (0, len(array)-1):
            if(array[j] > array[j+1]):
               temp = array[j]
               array[j] = array[j+1]
               array[j+1] = temp
    #present sorted list
    print(array)
    #write sorted list to file
    file = open(name, "x")
    file.close()
    file = open (name, "a")
    for i in range (len(array)):
        file.write(array[i])
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
        
    
