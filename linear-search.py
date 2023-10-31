lst = [5, 6, 8, 10, 12]
found = False
high = len(lst)
low = len(lst) - len(lst)
sv = int(input("Search Value: "))
while found == False and sv != lst:
    num = (high + low)//2
    if lst[num] == sv:
        found = True
    elif lst[num] < sv:
        low = num + 1
    else:
        high = num - 1
if found == True:
    print("The Searched Value " + str(sv) + " is at " + str(num + 1))
else:
    print("Not Found")