# zad1
# from datetime import datetime, timedelta

# day = int(input('day: '))
# month = (input('month: '))
# year = int(input('year: '))

# dataStr = f'{day} {month}, {year}'

# dataObj = datetime.strptime(dataStr, "%d %B, %Y")
# afterThousDays = dataObj + timedelta(days = 19)

# print(afterThousDays)
########################

#zad2
# bitcoins = int(input('bitcoins = '))
# chnsYoan = float(input('chnsYoan = '))
# comiss = float(input('comiss = ')) / 100

# euros = bitcoins * 1168 / 1.95 + chnsYoan * 0.15 * 1.76 / 1.95
# euros -= euros * comiss

# print('euros = ', "%.2f" % euros)
#######################################

#zad3: if clause
# num = int(input('Enter number: '))

# if num > 10:
#     print(f'{num} is bigger than 10')
# elif num == 10:
#     print(f'{num} is equal to 10')
# else:
#     print(f'{num} is smaller than 10')
##########################################

#zad4
# for i in range(ord('a'), ord('z') + 1):
#     print (chr(i), ' ')

#zad5
# n = -1
# while n <= 0:
#     n = int(input())

# max = 0
# for i in range(0, n):
#     x = int(input('Enter number: '))
    
#     if i == 0:
#         max = x
#     elif i > 0 and x > max:
#         max = x

# print('max = ', max)
