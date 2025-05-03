import random

rabbitLocation = 0

def turtle():
    turtlespace = random.randint(0, 15)
    return turtlespace

def rabbit(currentrabbit):
    rabbitspace = random.randint(0, 10)
    if rabbitspace == 3:
        rabbitspace = 0
        if rabbitspace == 2:
            rabbitspace == rabbitspace - currentrabbit
    return rabbitspace

while True:
    turtleLocation = turtle()
    print("Turtle Location:", turtleLocation)

    if turtleLocation == 10:
        print("🏁The Turtle has won the Race!🏁")
        break  

    rabbitLocationTurn = rabbit(rabbitLocation) # Fixed the call to the rabbit function
    rabbitLocation = rabbitLocation + rabbitLocationTurn # Updates the rabbit's actual location
    print("Rabbit Location:", rabbitLocation)

    if rabbitLocation == 0:
        print("The Rabbit is sleeping 🐇💤")
       
    if rabbitLocation == 2:
        print("The Rabbit has tripped 🐇💥")

    if rabbitLocation == 10:
        print("🏁The Rabbit has won the Race!🏁")
        break
