# Dawei Huang
# 07/17/2018
# CAAP Computer Science Assignment 1

# Programs for Part 1 of the assignment is contained in the file hello.py
# Programs for Part 2 of the assignment is contained in the file cash.py

# Part 2
print("Part 2: Change Program\n")
print("This program will prompt user for the amount of change and print the least possible number of coins returned")
change1 = int(float(input("Change owed: "))*100)
def leastChange(change):
    coinCounter = 0
    while change > 0:
        if change >= 25:
            coinCounter += 1
            change -= 25
        elif change >= 10:
            coinCounter += 1
            change -= 10
        elif change >= 5:
            coinCounter += 1
            change -= 5
        elif change >= 1:
            coinCounter += 1
            change -= 1
    return coinCounter
print ("least number of coin owed: "+ str(leastChange(change1)))