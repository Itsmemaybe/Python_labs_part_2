BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


# TODO написать класс Book
class Book:
    def __init__(self, id_: int, name: str, pages: int):
        """
        :param id_: Уникальный идентификатор книги
        :param name: Название книги
        :param pages: Количество страниц в книге

        Примеры:
        book = Book(id_=1, name="test_name_1", pages=200)  # инициализация экземпляра класса
        """
        if not isinstance(id_, int):
            raise TypeError("Идентификатор книги должен быть типа int")
        if id_ <= 0:
            raise ValueError("Идентификатор книги должен быть положительным числом")
        self.id = id_

        if not isinstance(name, str):
            raise TypeError("Название книги должно быть типа str")
        self.name = name

        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self.pages = pages

    def __str__(self) -> str:
        """
        :return: Строка в формате "Книга 'название_книги'"

        Примеры:
        book = Book(id_=1, name="test_name_1", pages=200)
        str(book)
        """
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        """

        :return: Строка в формате "Book(id_=1, name='test_name_1', pages=200)"

        Примеры:
        book = Book(id_=1, name="test_name_1", pages=200)
        repr(book)
        """
        return f"Book(id_={self.id}, name={repr(self.name)}, pages={self.pages})"

if __name__ == '__main__':
    # инициализируем список книг
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)  # проверяем метод __str__

    print(list_books)  # проверяем метод __repr__
