list = [5, 8, 15, 2, 6]
for i in range(len(list)):
    for j in range(len(list) - i - 1):
        if list[j] > list[j+1]:
            temp = list[j]
            list[j] = list[j+1]
            list[j+1] = temp
        print(list)
    print()