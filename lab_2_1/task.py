import doctest


class BankAccount:
    def __init__(self, owner: str, balance: float):
        """
        Создание и подготовка к работе объекта "Банковский счет"

        :param owner: Владелец счета
        :param balance: Баланс счета

        Примеры:
        >>> account = BankAccount("John Doe", 1000.0)  # инициализация экземпляра класса
        """
        if not isinstance(owner, str):
            raise TypeError("Имя владельца должно быть строкой")
        self.owner = owner

        if not isinstance(balance, (int, float)):
            raise TypeError("Баланс должен быть числом")
        if balance < 0:
            raise ValueError("Баланс не может быть отрицательным")
        self.balance = balance

    def deposit(self, amount: float) -> None:
        """
        Внесение денег на счет.

        :param amount: Сумма для внесения
        :raise ValueError: Если сумма отрицательная

        Примеры:
        account = BankAccount("John Doe", 1000.0)
        account.deposit(200.0)
        """
        if not isinstance(amount, (int, float)):
            raise TypeError("Сумма для внесения должна быть числом")
        if amount <= 0:
            raise ValueError("Сумма для внесения должна быть положительной")
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        """
        Снятие денег со счета.

        :param amount: Сумма для снятия
        :raise ValueError: Если сумма отрицательная или превышает баланс

        Примеры:
        >>> account = BankAccount("John Doe", 1000.0)
        >>> account.withdraw(100.0)
        """
        if not isinstance(amount, (int, float)):
            raise TypeError("Сумма для снятия должна быть числом")
        if amount <= 0:
            raise ValueError("Сумма для снятия должна быть положительной")
        if amount > self.balance:
            raise ValueError("Недостаточно средств на счете")
        self.balance -= amount

    def get_balance(self) -> float:
        """
        Получение текущего баланса счета.

        :return: Текущий баланс

        Примеры:
        >>> account = BankAccount("John Doe", 1000.0)
        >>> account.get_balance()
        1000.0
        """
        return self.balance


class Trunk:
    def __init__(self, capacity: float, occupied_space: float):
        """
        Создание и подготовка к работе объекта "Багажник"

        :param capacity: Объем багажника (в литрах)
        :param occupied_space: Занятый объем (в литрах)

        Примеры:
        >>> trunk = Trunk(500.0, 100.0)  # инициализация экземпляра класса
        """

        if not isinstance(capacity, (int, float)):
            raise TypeError("Объем багажника должен быть числом")
        if capacity <= 0:
            raise ValueError("Объем багажника должен быть положительным числом")
        self.capacity = capacity

        if not isinstance(occupied_space, (int, float)):
            raise TypeError("Занятый объем должен быть числом")
        if occupied_space < 0:
            raise ValueError("Занятый объем не может быть отрицательным")
        if occupied_space > capacity:
            raise ValueError("Занятый объем не может превышать объем багажника")
        self.occupied_space = occupied_space

    def add_item(self, item_volume: float) -> None:
        """
        Добавление предмета в багажник.

        :param item_volume: Объем добавляемого предмета (в литрах)
        :raise ValueError: Если объем предмета превышает свободное место в багажнике

        Примеры:
        >>> trunk = Trunk(500.0, 100.0)
        >>> trunk.add_item(50.0)
        """

        if not isinstance(item_volume, (int, float)):
            raise TypeError("Объем предмета должен быть числом")
        if item_volume <= 0:
            raise ValueError("Объем предмета должен быть положительным числом")
        if self.occupied_space + item_volume > self.capacity:
            raise ValueError("Недостаточно места в багажнике")
        self.occupied_space += item_volume

    def remove_item(self, item_volume: float) -> None:
        """
        Удаление предмета из багажника.

        :param item_volume: Объем удаляемого предмета (в литрах)
        :raise ValueError: Если объем удаляемого предмета превышает занятый объем

        Примеры:
        >>> trunk = Trunk(500.0, 100.0)
        >>> trunk.remove_item(30.0)
        """

        if not isinstance(item_volume, (int, float)):
            raise TypeError("Объем предмета должен быть числом")
        if item_volume <= 0:
            raise ValueError("Объем предмета должен быть положительным числом")
        if item_volume > self.occupied_space:
            raise ValueError("Объем удаляемого предмета превышает занятый объем")
        self.occupied_space -= item_volume

    def get_free_space(self) -> float:
        """
        Получение свободного объема в багажнике.

        :return: Свободный объем (в литрах)

        Примеры:
        >>> trunk = Trunk(500.0, 100.0)
        >>> trunk.get_free_space()
        400.0
        """
        return self.capacity - self.occupied_space


class Notebook:
    def __init__(self, pages: int, used_pages: int):
        """
        Создание и подготовка к работе объекта "Записная книжка"

        :param pages: Общее количество страниц в записной книжке
        :param used_pages: Количество использованных страниц

        Примеры:
        >>> notebook = Notebook(100, 20)  # инициализация экземпляра класса
        """
        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть целым числом")
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self.pages = pages
        if not isinstance(used_pages, int):
            raise TypeError("Количество использованных страниц должно быть целым числом")
        if used_pages < 0:
            raise ValueError("Количество использованных страниц не может быть отрицательным")
        if used_pages > pages:
            raise ValueError("Количество использованных страниц не может превышать общее количество страниц")
        self.used_pages = used_pages

    def add_note(self, pages_needed: int) -> None:
        """
        Добавление записи в записную книжку.

        :param pages_needed: Количество страниц, необходимых для записи
        :raise ValueError: Если недостаточно свободных страниц

        Примеры:
        >>> notebook = Notebook(100, 20)
        >>> notebook.add_note(5)
        """
        if not isinstance(pages_needed, int):
            raise TypeError("Количество страниц должно быть целым числом")
        if pages_needed <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        if self.used_pages + pages_needed > self.pages:
            raise ValueError("Недостаточно свободных страниц")
        self.used_pages += pages_needed

    def remove_note(self, pages_to_remove: int) -> None:
        """
        Удаление записи из записной книжки.

        :param pages_to_remove: Количество страниц, которые нужно освободить
        :raise ValueError: Если количество удаляемых страниц превышает использованные страницы

        Примеры:
        >>> notebook = Notebook(100, 20)
        >>> notebook.remove_note(5)
        """
        if not isinstance(pages_to_remove, int):
            raise TypeError("Количество страниц должно быть целым числом")
        if pages_to_remove <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        if pages_to_remove > self.used_pages:
            raise ValueError("Количество удаляемых страниц превышает использованные страницы")
        self.used_pages -= pages_to_remove

    def get_free_pages(self) -> int:
        """
        Получение количества свободных страниц.

        :return: Количество свободных страниц

        Примеры:
        >>> notebook = Notebook(100, 20)
        >>> notebook.get_free_pages()
        80
        """
        return self.pages - self.used_pages


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()