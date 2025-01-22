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



class Library:
    def __init__(self, books: list[Book] = None):
        """

        :param books: Список книг (по умолчанию None, что означает пустую библиотеку)

        Примеры:
        book1 = Book(id_=1, name="test_name_1", pages=200)
        book2 = Book(id_=2, name="test_name_2", pages=300)
        library = Library([book1, book2])  # инициализация экземпляра класса
        """
        if books is not None and not isinstance(books, list):
            raise TypeError("Список книг должен быть типа list")
        self.books = books if books is not None else []

    def get_next_book_id(self) -> int:
        """

        :return: Идентификатор следующей книги

        Примеры:
        library = Library()
        library.get_next_book_id()
        book1 = Book(id_=1, name="test_name_1", pages=200)
        library = Library([book1])
        library.get_next_book_id()
        """
        if not self.books:
            return 1
        return self.books[-1].id + 1

    def get_index_by_book_id(self, book_id: int) -> int:
        """

        :param book_id: Идентификатор книги
        :return: Индекс книги в списке
        :raise ValueError: Если книги с указанным id не существует

        Примеры:
        book1 = Book(id_=1, name="test_name_1", pages=200)
        book2 = Book(id_=2, name="test_name_2", pages=300)
        library = Library([book1, book2])
        library.get_index_by_book_id(2)
        """
        for index, book in enumerate(self.books):
            if book.id == book_id:
                return index
        raise ValueError("Книги с запрашиваемым id не существует")





if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
