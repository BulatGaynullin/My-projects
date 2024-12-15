def get_pass(n):
    for i in range(1, ((n + 1) // 2) + 1):
        for j in range(i + 1, (n - i) + 1):
            if n % (i + j) == 0:
                print(i, j, end="", sep="")
get_pass(int(input()))