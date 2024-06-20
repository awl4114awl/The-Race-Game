class Car:
    def __init__(self):
        self.__distance = 2
        self.__horn = "beep beep"
        self.__color = ""
        self.__line = "-"

    def soundHorn(self):
        print(self.__horn)

    def getColor(self):
        return self.__color

    def showLine(self, distance):
        self.__line += "-" * distance
        return self.__line

    def setHorn(self, horn_sound):
        self.__horn = horn_sound

class Model_1(Car):
    def __init__(self):
        super().__init__()
        self.__color = "blue"

    def getColor(self):
        return self.__color

class Model_2(Car):
    def __init__(self):
        super().__init__()
        self.__color = "red"
        self.setHorn("honk honk")

    def getColor(self):
        return self.__color