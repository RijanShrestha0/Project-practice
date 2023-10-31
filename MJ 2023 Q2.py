class Vehicle:
    # ID as String
    # MaxSpeed as Integer
    # CurrentSpeed as Integer
    # IncreaseAmount as Integer
    # HorizontalPosition as Integer
    def __init__(self, IDNum, Max, Increase):
        self.__ID = IDNum
        self.__MaxSpeed = Max
        self.__CurrentSpeed = 0
        self.__IncreaseAmount = Increase
        self.__HorizontalPosition = 0

    def GetCurrentSpeed(self):
        return self.__IncreaseAmount

    def GetIncreaseAmount(self):
        return self.__IncreaseAmount

    def GetMaxSpeed(self):
        return self.__MaxSpeed

    def GetHorizontalPosition(self):
        return self.__HorizontalPosition

    def SetCurrentSpeed(self, CSP):
        self.__CurrentSpeed = CSP

    def SetHorizontalPosition(self, HPP):
        self.__HorizontalPosition = HPP

    def IncreaseSpeed(self):
        self.__CurrentSpeed = self.__CurrentSpeed + self.__IncreaseAmount
        if self.__CurrentSpeed > self.__MaxSpeed:
            self.__CurrentSpeed = self.__MaxSpeed
        self.__HorizontalPosition = self.__HorizontalPosition + self.__CurrentSpeed

class Helicopter(Vehicle):
    # VerticalPosition as Integer
    # VerticalChange as Integer
    # MaxHeight as Integer
    def __init__(self, IDNum, Max, Increase, Vertical, MaxHeightP):
        Vehicle.__init__(self, IDNum, Max, Increase)
        self.__VerticalPosition = 0
        self.__VerticalChange = Vertical
        self.__MaxHeight = MaxHeightP

    def IncreaseSpeed(self):
        self.__VerticalPosition = self.__VerticalPosition + self.__VerticalChange
        if self.__VerticalPosition == self.__MaxHeight:
            self.__VerticalPosition = self.__MaxHeight
        Vehicle.SetCurrentSpeed(self, Vehicle.GetCurrentSpeed(self) + Vehicle.IncreaseSpeed(self))
        if self.GetCurrentSpeed() > self.GetMaxSpeed():
            Vehicle.GetCurrentSpeed(self=Vehicle.GetMaxSpeed(self))
        Vehicle.SetHorizontalPosition(self, Vehicle.GetHorizontalPosition(self) + Vehicle.GetCurrentSpeed(self))

    def OutputCurrentPosition(self):
        print("The Horizontal Position is ", Vehicle.GetHorizontalPosition(self))
        print("The Speed of the Vehicle is ", Vehicle.GetCurrentSpeed(self))
        print("The Vertical Position is ", self.__VerticalPosition)

    OutputCurrentPosition()
