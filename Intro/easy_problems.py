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
bitcoins = int(input('bitcoins = '))
chnsYoan = float(input('chnsYoan = '))
comiss = float(input('comiss = ')) / 100

euros = bitcoins * 1168 / 1.95 + chnsYoan * 0.15 * 1.76 / 1.95
euros -= euros * comiss

print('euros = ', "%.2f" % euros)

