def similar_numbers(arr):
    numbers = []
    for num in arr:
        if num >= 100:
            numbers.append(num // 100)

    numbers.sort()

    for i in range(0, len(numbers)-1):
        if numbers[i] == numbers[i + 1]:
            return True


arr = [9104, 7208, 3015, 7241]
print(similar_numbers(arr)) 