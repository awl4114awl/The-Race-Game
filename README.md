# The Race Game

## Overview
This project is a Python-based game where you race your car against the computer's car. The game uses Object-Oriented Programming (OOP) principles to simulate the race. The first car to reach 50 hyphens wins.

## Features
- Two car models: Model_1 (blue) and Model_2 (red).
- Random distance increments for each turn.
- Horn sounds for each car.
- Interactive user input to continue the race.

## Code Explanation

### Module File (`race_game_module.py`)

#### Car Class
1. **Initialization (`__init__` method):**
   - Initializes four private attributes: `distance`, `horn`, `color`, and `line`.
   - Sets default values for these attributes.

2. **Methods:**
   - `soundHorn()`: Prints the horn sound.
   - `getColor()`: Returns the color of the car.
   - `showLine(distance)`: Appends a specified number of hyphens to the line and returns it.
   - `setHorn(horn_sound)`: Sets the horn sound.

#### Model_1 Class
- Inherits from `Car`.
- Initializes the car color to blue.
- Overrides `getColor()` to return the color.

#### Model_2 Class
- Inherits from `Car`.
- Initializes the car color to red and sets the horn sound to "honk honk".
- Overrides `getColor()` to return the color.

### Main File (`race_game_main.py`)

1. **Imports:**
   - Imports `random` module and classes from the module file.

2. **Main Function:**
   - Initializes `myCar` and `computerCar` objects.
   - Displays the car details and sounds the horn.
   - Loops to prompt the user to continue the race.
   - Generates random distances, updates, and displays car lines.
   - Checks for a winner and displays the result.

## Full Code

### `race_game_module.py`
```python
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
```

### `race_game_main.py`
```python
import random
from race_game_module import Car, Model_1, Model_2

def main():
    myCar = Model_1()
    print("Your car is Model_1 and the color is " + myCar.getColor())
    myCar.soundHorn()

    computerCar = Model_2()
    print("The computer's car is Model_2 and the color is " + computerCar.getColor())
    computerCar.soundHorn()

    while True:
        drive_more = input("Drive some more? (y/n): ").strip()
        if drive_more.lower() == "n":
            break
        elif drive_more.lower() == "y" or drive_more == "":
            distance_mine = random.randint(1, 5)
            distance_computer = random.randint(1, 5)
            myLine = myCar.showLine(distance_mine)
            computerLine = computerCar.showLine(distance_computer)
            print("(" + myCar.getColor() + ") " + myLine + " (" + str(len(myLine)) + ")")
            print("(" + computerCar.getColor() + ") " + computerLine + " (" + str(len(computerLine)) + ")")

            if len(myLine) >= 50 and len(computerLine) >= 50:
                print("It's a tie!")
                break
            elif len(myLine) >= 50:
                print("You win!")
                break
            elif len(computerLine) >= 50:
                print("Computer wins!")
                break

if __name__ == "__main__":
    main()
```

## How to Run
1. Ensure Python is installed on your machine.
2. Clone the repository.
3. Navigate to the project directory.
4. Run `race_game_main.py`.

## Example Output
```
Your car is Model_1 and the color is blue
beep beep
The computer's car is Model_2 and the color is red
honk honk
Drive some more? (y/n): y
(blue) ----> (6)
(red ) -------> (7)
...
```

## License
This project is licensed under the MIT License.
