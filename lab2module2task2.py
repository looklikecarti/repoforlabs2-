class Book:
    def __init__(self, id_, name, pages):
        """
        конструктор для инициализации атрибутов книги.

        id_: идентификатор книги (целое число)
        name: название книги (строка)
        pages: количество страниц в книге (целое число)
        """
        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self):
        """
        метод для строкового представления экземпляра.

        return: строка в формате: книга "название_книги"
        """
        return f'Книга "{self.name}"'

    def __repr__(self):
        """
        метод для формального представления экземпляра.

        return: создает аналогичный объект Book
        """
        return f"Book(id_={self.id}, name='{self.name}', pages={self.pages})"


class Library:
    def __init__(self, books=None):
        """
        конструктор для инициализации атрибута библиотеки.

        books: список книг (изначально пустой список)
        """
        self.books = books if books is not None else []

    def get_next_book_id(self):
        """
        метод возвращает следующий идентификатор для новой книги.

        return: эт идентификатор книги (целое число)
        """
        if not self.books:
            return 1
        return self.books[-1].id + 1

    def get_index_by_book_id(self, book_id):
        """
        метод возвращает индекс книги в списке по ее id.

        book_id: идентификатор книги (целое число)
        return: индекс книги в списке
        raises ValueError: исли книга с переданным id не найдена
        """
        for index, book in enumerate(self.books):
            if book.id == book_id:
                return index
        raise ValueError("Книги с запрашиваемым id не существует")


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


if __name__ == '__main__':
    # Инициализация пустой библиотеки
    empty_library = Library()
    print(empty_library.get_next_book_id())  # Проверка следующего id для пустой библиотеки

    # Инициализация библиотеки с книгами
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)
    print(library_with_books.get_next_book_id())  # Проверка следующего id для библиотеки с книгами

    # Проверка получения индекса книги по id
    print(library_with_books.get_index_by_book_id(1))  # Индекс книги с id = 1