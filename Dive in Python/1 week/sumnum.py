"""
Получает от пользователя число и находит сумму цифр этого числа
"""


def sum(num_string):
    summa = int()
    for number in num_string:
        summa += int(number)
    return summa


if __name__ == "__main__":
    print(str(sum(str(input("Введите число: ")))))
