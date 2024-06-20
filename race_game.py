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