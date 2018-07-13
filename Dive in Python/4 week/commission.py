"""
This module contents a class of the  Account and descriptor,
that subtracts a commission from a payment.
"""


class Value:
    def __init__(self):
        self.value = None

    def __get__(self, obj, obj_type):
        return self.value

    def __set__(self, obj, value):
        self.value = value - value * obj.commission


class Account:

    amount = Value()

    def __init__(self, commission):
        self.commission = commission


def main():
    new_account = Account(0.1)
    new_account.amount = 100
    print(new_account.amount)


if __name__ == "__main__":
    main()
