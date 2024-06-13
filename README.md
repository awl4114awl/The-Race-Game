## README

# The Race Game

The Race Game is an interactive console-based game where you and the computer race to cover a certain distance. You drive a car, and the computer drives another car. Both cars cover random distances in each round. The game ends when either car (or both) cover a total distance of 50 units.

## How the Script Works

### 1. Car Class

The `Car` class is the base class representing a generic car.

#### Attributes:
- `__distance`: Initial distance set to 2 units.
- `__horn`: Initial horn sound set to "beep beep".
- `__color`: Car color (empty by default).
- `__line`: Visual representation of the car's progress.

#### Methods:
- `soundHorn()`: Prints the horn sound of the car.
- `getColor()`: Returns the color of the car.
- `showLine(distance)`: Appends dashes to the car's line to represent movement.
- `setHorn(horn_sound)`: Sets the horn sound of the car.

### 2. Model_1 Class

The `Model_1` class inherits from the `Car` class and represents a specific model of the car.

#### Attributes:
- Inherits attributes from `Car`.
- Sets the color to "blue".

#### Methods:
- Inherits methods from `Car`.
- Overrides `getColor()` to return "blue".

### 3. Model_2 Class

The `Model_2` class also inherits from the `Car` class and represents another specific model of the car.

#### Attributes:
- Inherits attributes from `Car`.
- Sets the color to "red".
- Sets a different horn sound "honk honk".

#### Methods:
- Inherits methods from `Car`.
- Overrides `getColor()` to return "red".

### 4. Main Function

The `main()` function drives the game logic:

1. **Car Initialization**:
   - Creates an instance of `Model_1` for the player.
   - Creates an instance of `Model_2` for the computer.

2. **Game Loop**:
   - Continuously prompts the user to drive more.
   - Generates random distances for both cars.
   - Updates and prints the visual representation of each car's progress.
   - Checks if either car has reached the finish line (50 units).

## Full Code

### race_game_module.py

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

### race_game.py

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

## How to Run the Code

### Prerequisites

1. **Python Installed**: Ensure that you have Python installed on your machine. You can download Python from the [official Python website](https://www.python.org/downloads/).

### Steps to Run the Script

1. **Clone the Repository**

   First, you need to clone the repository to your local machine. Open your terminal or command prompt and run the following command:

   ```sh
   git clone https://github.com/awl4114awl/The-Race-Game.git
   ```

2. **Navigate to the Directory**

   Change to the directory where the script is located:

   ```sh
   cd The-Race-Game
   ```

3. **Run the Script**

   Run the Python script using the following command:

   ```sh
   python race_game.py
   ```

### Playing the Game

1. **Start the Game**

   When you run the script, you will see a welcome message indicating your car model and color.

2. **Drive Your Car**

   The game will prompt you to decide whether to drive more:

   ```
   Drive some more? (y/n): 
   ```

   - Enter `y` or press Enter to drive more.
   - Enter `n` to stop the game.

3. **Game Progress**

   The game will show the progress of both cars after each round, displaying the color and distance covered by each car. The game continues until one or both cars cover 50 units.

4. **Win Condition**

   The game ends with a win message for you or the computer, or a tie if both reach the finish line at the same time.

Enjoy playing The Race Game!

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
