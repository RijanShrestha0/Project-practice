ArrayNode = []
for x in range(20):
    ArrayNode.append([-1, -1, -1])

Freenode = 6
Root = 0
ArrayNode = [[1, 20, 5], [2, 15, -1], [-1, 3, 3], [-1, 9, 4], [-1, 10, -1], [-1, 58, -1], [-1, -1, -1]]
# print(ArrayNode)


def SearchValue(Root, Value):
    global ArrayNode
    if Root == -1:
        return -1
    elif ArrayNode[Root, 1] == Value:
        return Root
    elif ArrayNode[Root, 1] == -1:
        return -1
    if ArrayNode[Root, 1] > Value:
        return SearchValue(ArrayNode[Root, 0], Value)
    if ArrayNode[Root, 1] < Value:
        return SearchValue(ArrayNode[Root, 2], Value)


def PostOrder(RootNode):
    if RootNode[-1] != -1:
        PostOrder(ArrayNode[RootNode[-1]])
    if RootNode[1] != -1:
        PostOrder(ArrayNode[RootNode[1]])
    print(str(RootNode[0]))


