stack = ["NaN" for index in range(0,5)]

base = 0
top = -1
full = 5
# user input for pop
# item1 = int(input("Enter the number for pop: "))
# user input for push
for i in range(6):
    item = int(input("Enter the number for stacking: "))
# pop condition
if top == base - 1:
    print("Stack is empty...")
else:
    item1 = stack[top]
    top = top - 1
# push condition
if top < full + 1:
    top = top + 1
    stack[top] = item
else:
    print("The Stack is Full...")

print(stack)

