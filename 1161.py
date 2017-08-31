def Fat(n):
    if n == 0: return 1

    return n * Fat(n - 1)

while True:
    try:
        n1, n2 = map(int, input().split())
        tot = Fat(n1) + Fat(n2)
        print(tot)
    except EOFError:
            break