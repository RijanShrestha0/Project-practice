class Balloon:
    # Health as Integer
    # Color as String
    # DefenceItem as String
    def __init__(self, VDefenceItem, VColor):
        self.__Health = 100
        self.__DefenceItem = VDefenceItem
        self.__Color = VColor

    def GetDefenceItem(self):
        return self.__DefenceItem

    def ChangeHealth(self, Change):
        self.__Health = self.__Health + Change

    def CheckHealth(self):
        if self.__Health <= 0:
            return True
        else:
            return False


Method = input("Enter a Balloon Defence method: ")
Color = input("Enter the Balloon Colour: ")
Balloon1: Balloon = Balloon(Method, Color)


def Defend(MyBalloon):
    Strength = int(input("Enter the Strength of the opponent: "))
    MyBalloon.ChangeHealth(-Strength)
    print("You defended with a", MyBalloon.GetDefenceItem())
    if MyBalloon.CheckHealth() == True:
        print("Defence failed")
    else:
        print("Defence Succeed")
    return MyBalloon


Balloon1 = Defend(Balloon1)
