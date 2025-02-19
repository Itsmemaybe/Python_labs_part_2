
import doctest

class Vehicle:
    """
    Базовый класс для всех транспортных средств.

    Атрибуты:
    - brand (str): Марка транспортного средства.
    - model (str): Модель транспортного средства.
    - year (int): Год выпуска.
    - mileage (float): Пробег в километрах.
    """

    def __init__(self, brand: str, model: str, year: int, mileage: float):
        """
        Инициализация транспортного средства.

        :param brand: Марка транспортного средства.
        :param model: Модель транспортного средства.
        :param year: Год выпуска.
        :param mileage: Пробег в километрах.

        Примеры:
        >>> vehicle = Vehicle("Toyota", "Corolla", 2020, 15000.5)
        """
        if not isinstance(brand, str):
            raise TypeError("Марка должна быть типа str")
        if not isinstance(model, str):
            raise TypeError("Модель должна быть типа str")
        if not isinstance(year, int):
            raise TypeError("Год выпуска должен быть типа int")
        if not isinstance(mileage, (int, float)):
            raise TypeError("Пробег должен быть типа int или float")

        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage

    def __str__(self) -> str:
        """
        Возвращает строковое представление транспортного средства.

        :return: Строка в формате "Марка Модель, Год выпуска, Пробег: mileage км".

        Примеры:
        >>> vehicle = Vehicle("Toyota", "Corolla", 2020, 15000.5)
        >>> str(vehicle)
        'Toyota Corolla, 2020, Пробег: 15000.5 км'
        """
        return f"{self.brand} {self.model}, {self.year}, Пробег: {self.mileage} км"

    def __repr__(self) -> str:
        """
        Возвращает строку, по которой можно инициализировать экземпляр.

        :return: Строка в формате "Vehicle(brand='Toyota', model='Corolla', year=2020, mileage=15000.5)".

        Примеры:
        >>> vehicle = Vehicle("Toyota", "Corolla", 2020, 15000.5)
        >>> repr(vehicle)
        "Vehicle(brand='Toyota', model='Corolla', year=2020, mileage=15000.5)"
        """
        return f"Vehicle(brand={repr(self.brand)}, model={repr(self.model)}, year={self.year}, mileage={self.mileage})"

    def drive(self, distance: float) -> None:
        """
        Увеличивает пробег транспортного средства на указанное расстояние.

        :param distance: Расстояние в километрах.

        Примеры:
        >>> vehicle = Vehicle("Toyota", "Corolla", 2020, 15000.5)
        >>> vehicle.drive(100)
        >>> vehicle.mileage
        15100.5
        """
        if not isinstance(distance, (int, float)):
            raise TypeError("Расстояние должно быть типа int или float")
        if distance < 0:
            raise ValueError("Расстояние должно быть положительным числом")
        self.mileage += distance


class Car(Vehicle):
    """
    Дочерний класс для легковых автомобилей.

    Атрибуты:
    - brand (str): Марка автомобиля.
    - model (str): Модель автомобиля.
    - year (int): Год выпуска.
    - mileage (float): Пробег в километрах.
    - num_doors (int): Количество дверей.
    """

    def __init__(self, brand: str, model: str, year: int, mileage: float, num_doors: int):
        """
        Инициализация легкового автомобиля.

        :param brand: Марка автомобиля.
        :param model: Модель автомобиля.
        :param year: Год выпуска.
        :param mileage: Пробег в километрах.
        :param num_doors: Количество дверей.

        Примеры:
        >>> car = Car("Toyota", "Corolla", 2020, 15000.5, 4)
        """
        super().__init__(brand, model, year, mileage)
        if not isinstance(num_doors, int):
            raise TypeError("Количество дверей должно быть типа int")
        if num_doors < 2 or num_doors > 5:
            raise ValueError("Количество дверей должно быть от 2 до 5")
        self.num_doors = num_doors

    def __str__(self) -> str:
        """
        Возвращает строковое представление легкового автомобиля.

        :return: Строка в формате "Марка Модель, Год выпуска, Пробег: mileage км, Двери: num_doors".

        Примеры:
        >>> car = Car("Toyota", "Corolla", 2020, 15000.5, 4)
        >>> str(car)
        'Toyota Corolla, 2020, Пробег: 15000.5 км, Двери: 4'
        """
        return f"{super().__str__()}, Двери: {self.num_doors}"

    def __repr__(self) -> str:
        """
        Возвращает строку, по которой можно инициализировать экземпляр.

        :return: Строка в формате "Car(brand='Toyota', model='Corolla', year=2020, mileage=15000.5, num_doors=4)".

        Примеры:
        >>> car = Car("Toyota", "Corolla", 2020, 15000.5, 4)
        >>> repr(car)
        "Car(brand='Toyota', model='Corolla', year=2020, mileage=15000.5, num_doors=4)"
        """
        return f"Car(brand={repr(self.brand)}, model={repr(self.model)}, year={self.year}, mileage={self.mileage}, num_doors={self.num_doors})"

    def drive(self, distance: float) -> None:
        """
        Перегруженный метод для увеличения пробега.
        Добавляет проверку на максимальный пробег для легковых автомобилей.

        :param distance: Расстояние в километрах.

        Примеры:
        >>> car = Car("Toyota", "Corolla", 2020, 15000.5, 4)
        >>> car.drive(100)
        >>> car.mileage
        15100.5
        """
        if self.mileage + distance > 300000:
            raise ValueError("Легковой автомобиль не может иметь пробег более 300000 км")
        super().drive(distance)


class Truck(Vehicle):
    """
    Дочерний класс для грузовых автомобилей.

    Атрибуты:
    - brand (str): Марка грузовика.
    - model (str): Модель грузовика.
    - year (int): Год выпуска.
    - mileage (float): Пробег в километрах.
    - max_load (float): Максимальная грузоподъемность в тоннах.
    """

    def __init__(self, brand: str, model: str, year: int, mileage: float, max_load: float):
        """
        Инициализация грузового автомобиля.

        :param brand: Марка грузовика.
        :param model: Модель грузовика.
        :param year: Год выпуска.
        :param mileage: Пробег в километрах.
        :param max_load: Максимальная грузоподъемность в тоннах.

        Примеры:
        >>> truck = Truck("Volvo", "FH16", 2018, 250000.0, 20.5)
        """
        super().__init__(brand, model, year, mileage)
        if not isinstance(max_load, (int, float)):
            raise TypeError("Грузоподъемность должна быть типа int или float")
        if max_load <= 0:
            raise ValueError("Грузоподъемность должна быть положительным числом")
        self.max_load = max_load

    def __str__(self) -> str:
        """
        Возвращает строковое представление грузового автомобиля.

        :return: Строка в формате "Марка Модель, Год выпуска, Пробег: mileage км, Грузоподъемность: max_load т".

        Примеры:
        >>> truck = Truck("Volvo", "FH16", 2018, 250000.0, 20.5)
        >>> str(truck)
        'Volvo FH16, 2018, Пробег: 250000.0 км, Грузоподъемность: 20.5 т'
        """
        return f"{super().__str__()}, Грузоподъемность: {self.max_load} т"

    def __repr__(self) -> str:
        """
        Возвращает строку, по которой можно инициализировать экземпляр.

        :return: Строка в формате "Truck(brand='Volvo', model='FH16', year=2018, mileage=250000.0, max_load=20.5)".

        Примеры:
        >>> truck = Truck("Volvo", "FH16", 2018, 250000.0, 20.5)
        >>> repr(truck)
        "Truck(brand='Volvo', model='FH16', year=2018, mileage=250000.0, max_load=20.5)"
        """
        return f"Truck(brand={repr(self.brand)}, model={repr(self.model)}, year={self.year}, mileage={self.mileage}, max_load={self.max_load})"

    def load_cargo(self, weight: float) -> None:
        """
        Проверяет, может ли грузовик перевезти указанный вес.

        :param weight: Вес груза в тоннах.
        :raise ValueError: Если вес превышает грузоподъемность.

        Примеры:
        >>> truck = Truck("Volvo", "FH16", 2018, 250000.0, 20.5)
        >>> truck.load_cargo(15)
        >>> truck.load_cargo(25)
        Traceback (most recent call last):
        ...
        ValueError: Вес груза превышает грузоподъемность
        """
        if weight > self.max_load:
            raise ValueError("Вес груза превышает грузоподъемность")
        print(f"Груз весом {weight} т успешно загружен.")


if __name__ == "__main__":
    doctest.testmod()
