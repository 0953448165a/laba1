a = float(input("Введіть число a: "))
b = float(input("Введіть число b: "))
if a <= 0 or b <= 0:
    print("Помилка! Числа a та b повинні бути додатними.")
elif a > 100 or b > 100:
    print("Помилка! Числа a та b повинні бути в межах від 1 до 100.")
else:
    if a > b:
        X = a / b + 1
    elif a == b:
        X = a + 25
    else:  # a < b
        X = (a * b - 2) / a
    print(f"Результат: X = {X}")
