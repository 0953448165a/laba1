N = int(input("Введіть ціле число N (1 < N < 9): "))
if N <= 1 or N >= 9:
    print("Помилка! N повинно бути в межах 1 < N < 9.")
else:
    for i in range(N, 0, -1):
        for j in range(i, N + 1):
            print(j, end=" ")
        print()
    for i in range(1, N + 1):
        for j in range(i, 0, -1):
            print(j, end=" ")
        print()
