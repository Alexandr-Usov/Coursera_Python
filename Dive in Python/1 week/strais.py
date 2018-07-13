"""
Программа запрашивает у пользователя количество
ступенек и строит лестницу на экране.
"""


def strais(quantily_steps):
    """Построение ступенек"""
    step = 1
    while step <= quantily_steps:
        print(" " * (quantily_steps - step) + "#" * step)
        step += 1


if __name__ == "__main__":
    strais(int(input("Введите количество ступенек: ")))
