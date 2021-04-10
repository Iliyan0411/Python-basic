def similar_numbers(arr):
    numbers = []
    for num in arr:
        if num >= 100:
            numbers.append(num // 100)

    numbers.sort()

    finded = None
    for i in range(0, len(numbers)-1):
        if numbers[i] == numbers[i + 1]:
            finded = numbers[i]

    counter = 0
    for num in arr:
        if num // 100 == finded:
            counter += 1
        if counter == 2:
            return True
    
    return False


arr = [9104, 7208, 3015, 7241]
print(similar_numbers(arr)) 