import random

def guessNumber():
    num = int(100*random.random() + 1)
    counter, minNum, maxNum = 1, 1, 100

    while counter < 6:
        x = int(input(f'{counter}) -----enter number({minNum}-{maxNum}): '))
        if x < minNum or x > maxNum: continue

        if x == num:
            print('Congratulations, you win!\n')
            return
        elif x < num:
            counter = counter + 1
            minNum = x + 1
        else:
            counter = counter + 1
            maxNum = x - 1

    print(f'You lose! The correct number is {num}\n')


def main():
    guessNumber()


main()