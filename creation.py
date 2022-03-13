def createlist():
    #create list for bookshelf
    array = []
    #have user create list
    book = ""
    while( book != "done"):
        book = str(input("please enter book title, type done to finish: "))
        array.append(book)
    array.remove("done")
    return array
def bubblesort(array):
    print("Sorting...")
    for i in range (len(array)):
        for j in range (0, len(array)-1):
            if(array[j] > array[j+1]):
               temp = array[j]
               array[j] = array[j+1]
               array[j+1] = temp
    #present sorted list
    print(array)
    return array
def filecreation(name, array):
    file = open(name, "x")
    file.close()
    file = open (name, "a")
    for i in range (len(array)):
        file.write(array[i])
    file.close()
    
