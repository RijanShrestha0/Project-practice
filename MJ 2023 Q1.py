DataArray = [] # 25 Integer Elements
try:
    DataFile = open("Data.txt", 'r')
    for line in DataFile:
        DataArray.append(int(line))
    DataFile.close()
except IOError:
    print("Couldn't find the file.")

def PrintArray(DataArray):
    output = ""
    for x in range(0, len(DataArray)):
        output = output + str(DataArray[x]) + " "
    print(output)


PrintArray(DataArray)

def LinearSearch(DataArray, Search):
    count = 0
    for x in range(0, len(DataArray)):
        if (DataArray[x] == Search):
            count = count + 1
    return count


Search = int(input("Enter any Number between 0 to 100: "))
while Search < 0 or Search >100:
    Search = int(input("Enter any Number between 0 to 100: "))
times = LinearSearch(DataArray, Search)
print("The Number ", Search, "is Found ", times, "times")