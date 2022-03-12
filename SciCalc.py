greeting = 'Hello, '
Name = input('What is your name?: ')
Exp = ' this is a program meant for calculating in the field of science.'
Intorduction = (greeting + Name + Exp)
print(Intorduction)
def mass():
    Mass = int(A) * int(B)
def volume():
    Volume = int(A) * int(B) * int(C)
def density():
    Density = int(A) / int(B)
print('What will you be using this calculator for today?')
print('1. Mass')
print('2 Volume')
print('3 Density')

while True:
    choice = input("Enter choice(1/2/3): ")

    if choice == '1':
        A = input("What is the volume?: ")
        B = input('What is the density?: ')
        Mass = int(A) * int(B)
        print(Mass)
    elif choice == '2':
        A = input("Length?: ")
        B = input("Width?: ")
        C = input('Height?: ')
        Volume = int(A) * int(B) * int(C)
        print(Volume)
    elif choice == '3':
        A = input('Mass?: ')
        B = input('Volume?: ')
        Density = int(A) / int(B)
        print(Density)
    next_calc = input("Would you like to do another calculation?(Y/N): ")
    if next_calc == "N":
        break

    else:
        print('Invalid Input')