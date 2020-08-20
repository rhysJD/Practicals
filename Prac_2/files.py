"""
CP1404 - Practical 2
Rhys Donaldson
"""

totalNumb = 0

names = open('name.txt', 'w')
print(input("What is your name? "), file= names)
names.close()

names = open('name.txt', 'r')
print('Your name is', names.readline())
names.close()

numbersTXT = open('numbers.txt', 'r')
numb1 = int(numbersTXT.readline())
numb2 = int(numbersTXT.readline())
print(numb1 + numb2)
numbersTXT.close()

numbersTXT = open('numbers.txt', 'r')
for line in numbersTXT:
    holdNumb = int(numbersTXT.readline())
    totalNumb = totalNumb + holdNumb
print(totalNumb)

numbersTXT.close()