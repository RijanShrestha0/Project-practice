QueueArray = ["NaN" for i in range(10)]
head = 0
tail = 0
item = 0


def Enqueue(QueueArray, head, tail, item, data):
    if item >= 10:
        return False, QueueArray, head, tail, item
    QueueArray[tail] = data
    if tail >= 9:
        tail = 0
    else:
        tail = tail + 1
    item = item + 1
    return True, QueueArray, head, tail, item


def DeQueue(QueueArray, head, tail, item):
    if item == 0:
        return False, QueueArray, head, tail, item
    else:
        Value = QueueArray[head]
        head = head + 1
        if head >= 9:
            head = 0
        item = item - 1
        return Value, QueueArray, head, tail, item


for i in range(11):
    InputData = str(input("Enter any String: "))
    Value, QueueArray, head, tail, item = Enqueue(QueueArray, head, tail, item, InputData)
    if Value == True:
        print("Successful...")
    else:
        print("Not Successful...")
Value, QueueArray, head, tail, item = DeQueue(QueueArray, head, tail, item)
print(QueueArray)