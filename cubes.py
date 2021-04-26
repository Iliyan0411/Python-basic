def is_cube(x):
    for i in range(1, x):
        if i**3 == x:
            return (True, i)

    return (False, 0)


def helper(a):
    y = 1
    while y <= a:
        x = a + y**3
        pair = is_cube(x)
        if pair[0]:
            print("{0} {1}".format(pair[1],y))
            break
        
        y += 1

    if y > a:
        print("NO")


def cubes(a, b):
    helper(a)
    helper(b)


def main():
    a = int(input())
    b = int(input())

    cubes(a, b)



main()
