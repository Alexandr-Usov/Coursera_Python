"""
This module contendet car classes.
"""

import csv


class BaseCar():
    """
    This class is a parent for all other car's classes.
    """
    def __init__(self, brand, photo_file_name, carryng):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carryng = carryng

    def get_photo_file_ext(self):
        pass  # TODO


class Car(BaseCar):
    """
    This class describes a passanger car.
    """
    def __init__(self, brand, photo_file_name, carryng, passenger_seat_count):
        super().__init__(brand, photo_file_name, carryng)
        self.passenger_seat_count = passenger_seat_count


class Truck(BaseCar):
    """
    This class describes a truck.
    """
    def __init__(self, brand, photo_file_name, carryng, body_width: float,
                 body_height: float, body_length: float):
        super().__init__(brand, photo_file_name, carryng)
        self.body_width = float(body_width)
        self.body_height = float(body_height)
        self.body_length = float(body_length)

    def get_body_volume(self):
        return self.body_width * self.body_height * self.body_length


class SpecMachine(BaseCar):
    """
    This class describes a special machine.
    """
    def __init__(self, brand, photo_file_name, carryng, extra):
        super().__init__(brand, photo_file_name, carryng)
        self.extra = extra


def row_parce(row):
    if row == []:
        return

    if row[0] == 'car':
        car = Car(row[1], row[3], row[5], row[2])
        return car

    elif row[0] == 'truck':
        if row[4] != '':
            capacity = row[4].split('x')
        else:
            capacity = [0, 0, 0]
        truck = Truck(row[1], row[3], row[5], capacity[0],
                      capacity[1], capacity[2])
        return truck

    elif row[0] == 'spec_machine':
        spec_machine = SpecMachine(row[1], row[3], row[5],
                                   row[6])
        return spec_machine


def get_car_list(csv_file_name: str):
    """The function parse and to build a list of cars from csv file"""
    car_list = []
    with open(csv_file_name) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)  # Skip the header of the file
        for row in reader:
            if row_parce(row) is not None:
                car_list.append(row_parce(row))
        return car_list


def main():
    print(get_car_list("coursera_week3_cars.csv"))

if __name__ == "__main__":
    main()
