mylist = [3, 5, 1, 12, 4, 8, 14, 2, 10]
high = len(mylist)
low = 0
for i in range(low, high):
    key = mylist[i]
    place = i - 1
    if mylist[place] > key:
        while place >= low and mylist[place] > key:
            temp = mylist[place + 1]
            mylist[place + 1] = mylist[place]
            mylist[place] = temp
            place = place - 1
        mylist[place + 1] = key
print(mylist)
