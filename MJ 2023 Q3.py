Animal = []  # 20 Elements
Colour = []  # 10 Elements
global AnimalTop
global ColourTop
AnimalTop = 0
ColourTop = 0


def PushAnimal(DataToPush):
    global AnimalTop
    if AnimalTop == 20:
        return False
    else:
        Animal.append(DataToPush)
        AnimalTop = AnimalTop + 1
        return True
PushAnimal(10)
PushAnimal(20)


def PopAnimal():
    global AnimalTop
    if AnimalTop == 0:
        return ""
    else:
        ReturnData = Animal[AnimalTop - 1]
        AnimalTop = AnimalTop - 1
        return ReturnData
PopAnimal()
print(Animal)

def ReadAnimalData():
    try:
        AnimalData = open("AnimalData.txt", 'r')
        for i in AnimalData:
            Animal.append(str(i))
        AnimalData.close()
    except IOError:
        print("Couldn't Find the File...")
ReadAnimalData()
print(Animal)

def PushColour(DataToPush):
    global ColourTop
    if ColourTop == 20:
        return False
    else:
        Colour[ColourTop] = DataToPush
        ColourTop = ColourTop + 1
        return True


def PopColour():
    global ColourTop
    if ColourTop == 0:
        return ""
    else:
        ReturnData = Colour[ColourTop - 1]
        ColourTop = ColourTop - 1
        return ReturnData

def ReadColorData():
    try:
        ColourData = open("ColourData.txt", 'r')
        for i in ColourData:
            Colour.append(str(i))
        ColourData.close()
    except IOError:
        print("File Not Found...")
ReadColorData()


def OutputItem():
    AnimalVal = PopAnimal()
    ColourVal = PopColour()
    if AnimalVal == "":
        print("No Animal...")
        PushColour(ColourVal)
    elif ColourVal == "":
        print("No Colour...")
        PushAnimal(ColourVal)
    else:
        print(ColourVal, AnimalVal)


ReadColorData()
ReadAnimalData()
OutputItem()
OutputItem()
OutputItem()
OutputItem()