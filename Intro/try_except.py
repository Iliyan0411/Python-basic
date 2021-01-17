def enterEven():
    while True:
        try:
            n = int(input('enter number: '))
            if n % 2 == 0:
                return n
                break
            
        except ValueError:
            print('Invalid number')

num = enterEven()
print(num)
