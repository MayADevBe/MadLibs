import os
from random import randint
from madlibs import MadLibs

def print_madlibs():
    print("Available Madlibs:")
    files = []
    if not os.path.isdir("madlibsfiles"):
        print("There is no 'madlibsfiles folder'")
    files = os.listdir("madlibsfiles")
    for i in range(len(files)):
        file = files[i]
        if file.endswith('.txt'):
            file = file[:-4]
            print(f"{i+1}: {file}")

def choose_madlibs():
    num = input("Type in the number of the MadLip you want to use: ")
    if not os.path.isdir("madlibsfiles"):
        print("There is no 'madlibsfiles folder'")
    files = os.listdir("madlibsfiles")
    try:
        num = int(num)
        if (num > 0) and (num <= len(files)):
            return files[num-1]
    except ValueError:
        pass
    
    print("Random MadLib")
    num = randint(1, len(files))
    return files[num-1]

def main():
    played = False
    madlib = MadLibs()
    while True:
        print("Welcome to MadLibs")
        print("1: New Mablib")
        if played:
            print("2: Same Madlib new Input")
            print("3: Same Input new Madlib")
        print("end: To Exit the game")
        num = input("Type number, to choose option: ")
        print()
        try:
            num = int(num)
            if (num > 0) and (num <= 3):
                if num == 1:
                    print_madlibs()
                    name = choose_madlibs()
                    madlib.get_inputs()
                    madlib.get_mad_libs(name)
                    played = True
                elif played:
                    if num == 2:
                        madlib.get_inputs()
                        madlib.get_mad_libs(name)
                    if num == 3:
                        print_madlibs()
                        name = choose_madlibs()
                        madlib.get_mad_libs(name)
        except ValueError:
            if num == "end":
                return
            print(f"{num} not a valid option!")
        
        print()
        input("Press Enter to continue...")
        print()

main()