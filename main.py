import random
import turtle

def drawShape(sideLen,sides):
    turtle.speed(0)
    for side in range(sides):
        turtle.forward(sideLen)
        turtle.right(360/sides)

sideLength = input("Side length: ")
numSides = input("Number of sides: ")

try:
    sideLength = int(sideLength)
    numSides = int(numSides)
except(ValueError):
    print("Please input numbers next time")
    exit

drawShape(sideLength,numSides)
input("Press enter to close")