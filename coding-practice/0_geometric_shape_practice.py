def print_triangle(n: int):
    for i in range(1, n+1):
        print(' ' * (n - i) + '*' * (2 * i - 1))
        
def print_hexagon(size):
    for i in range(size):
        print(' ' * (size - i - 1) + '*' * (2 * size + 2 * i))
    for i in range(size-1, -1, -1):
        print(' ' * (size - i - 1) + '*' * (2 * size + 2 * i))

def print_hollow_square(n):
    for i in range(n):
        if i == 0 or i == n-1:
            print('*' * n)
        else:
            print('*' + ' ' * (n - 2) + '*')

def print_hourglass(n):
    for i in range(n, 0, -1):
        print(' ' * (n - i) + '*' * (2 * i - 1))
    for i in range(2, n+1):
        print(' ' * (n - i) + '*' * (2 * i - 1))

def print_hollow_diamond(n):
    for i in range(n):
        if i == 0:
            print(' ' * (n - i - 1) + '*')
        else:
            print(' ' * (n - i - 1) + '*' + ' ' * (2 * i - 1) + '*')
    for i in range(n-2, -1, -1):
        if i == 0:
            print(' ' * (n - i - 1) + '*')
        else:
            print(' ' * (n - i - 1) + '*' + ' ' * (2 * i - 1) + '*')