class Book:
    def __init__(self, id_, name, pages):
        """
        Конструктор для инициализации атрибутов книги.

        """
        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self):
        """
        тут у нас метод для строкового представления экземпляра.

        """
        return f'Книга "{self.name}"'

    def __repr__(self):
        """
        а тут метод для формального представления экземпляра.

        """
        return f"Book(id_={self.id}, name='{self.name}', pages={self.pages})"


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
    # инициализируем список книг
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)  # проверяем метод __str__

    print(list_books)  # проверяем метод __repr__