import random

def guessNumber():
    num = int(100*random.random() + 1)
    counter, minNum, maxNum = 1, 1, 100

    while counter < 6:
        x = int(input(f'{counter}) -----enter number({minNum}-{maxNum}): '))
        if x < minNum or x > maxNum: continue

        if x == num:
            print('\nCongratulations, you win!\n')
            return
        elif x < num: minNum = x + 1
        else: maxNum = x - 1

        counter = counter + 1

    print(f'\nYou lose! The correct number is {num}\n')


def main():
    while True:
        print('[1] Play')
        print('[2] Exit')

        choice = 0
        while choice < 1 or choice > 2:
            choice = int(input('-> '))

        if choice == 1: 
            print(' ')
            guessNumber()
        else: return


main()