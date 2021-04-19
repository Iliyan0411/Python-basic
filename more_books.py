
def more_books(arr, X):
    arr.sort()

    sum = 0
    choosed = []
    for book in arr:
        if sum + book <= X:
            sum += book
            choosed.append(book)
        else:
            return choosed

arr = [50,20,10,80]

print(more_books(arr, 45))