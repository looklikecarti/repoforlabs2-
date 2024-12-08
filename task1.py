import doctest


class Fridge:
    """Класс, представляющий холодильник.
    Атрибуты:
    brand (str): Марка холодильника.
    capacity (int): Вместимость холодильника в литрах.
    items (dict): Список продуктов в формате {название: количество}.
    """

    def __init__(self, brand: str, capacity: int):
        """
        Инициализирует объект холодильника.
        Аргументы:
        brand (str): Марка холодильника.
        capacity (int): Вместимость холодильника.
        Исключения:
        ValueError: Если вместимость меньше 50 литров.
        """
        if capacity < 50:
            raise ValueError("Вместимость должна быть не менее 50 литров.")
        self.brand = brand
        self.capacity = capacity
        self.items = {}

    def add_item(self, name: str, quantity: int) -> None:
        """
        Добавляет продукт в холодильник.
        Аргументы:
        name (str): Название продукта.
        quantity (int): Количество продукта.
        Исключения:
        ValueError: Если количество меньше 1.
        Пример:
        >>> fridge = Fridge("Samsung", 200)
        >>> fridge.add_item("Milk", 2)
        >>> fridge.items
        {'Milk': 2}
        """
        if quantity < 1:
            raise ValueError("Количество должно быть не меньше 1.")
        self.items[name] = self.items.get(name, 0) + quantity

    def get_item(self, name: str, quantity: int) -> None:
        """
        Убирает продукт из холодильника.
        Аргументы:
        name (str): Название продукта.
        quantity (int): Количество продукта для удаления.
        Исключения:
        KeyError: Если продукта нет в холодильнике.
        ValueError: Если количество для удаления больше, чем есть.
        Пример:
        >>> fridge = Fridge("Samsung", 200)
        >>> fridge.add_item("Milk", 2)
        >>> fridge.get_item("Milk", 1)
        >>> fridge.items
        {'Milk': 1}
        """
        if name not in self.items:
            raise KeyError(f"Продукт '{name}' отсутствует в холодильнике.")
        if self.items[name] < quantity:
            raise ValueError("Недостаточно продукта для удаления.")
        self.items[name] -= quantity
        if self.items[name] == 0:
            del self.items[name]


class BankAccount:
    """Класс, представляющий банковский счёт.
    Атрибуты:
    account_number (str): Номер счёта.
    balance (float): Баланс счёта.
    currency (str): Валюта счёта.
    """

    def __init__(self, account_number: str, balance: float, currency: str):
        """
        Инициализирует объект банковского счёта.
        Аргументы:
        account_number (str): Номер счёта.
        balance (float): Начальный баланс.
        currency (str): Валюта счёта.
        Исключения:
        ValueError: Если баланс отрицательный.
        """
        if balance < 0:
            raise ValueError("Баланс не может быть отрицательным.")
        self.account_number = account_number
        self.balance = balance
        self.currency = currency

    def deposit(self, amount: float) -> None:
        """
        Вносит деньги на счёт.
        Аргументы:
        amount (float): Сумма для внесения.
        Исключения:
        ValueError: Если сумма меньше или равна нулю.
        Пример:
        >>> account = BankAccount("123456", 100.0, "USD")
        >>> account.deposit(50.0)
        >>> account.balance
        150.0
        """
        if amount <= 0:
            raise ValueError("Сумма должна быть больше 0.")
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        """
        Снимает деньги со счёта.
        Аргументы:
        amount (float): Сумма для снятия.
        Исключения:
        ValueError: Если сумма меньше 0 или превышает баланс.
        Пример:
        >>> account = BankAccount("123456", 100.0, "USD")
        >>> account.withdraw(50.0)
        >>> account.balance
        50.0
        """
        if amount <= 0:
            raise ValueError("Сумма должна быть больше 0.")
        if amount > self.balance:
            raise ValueError("Недостаточно средств.")
        self.balance -= amount

class Library:
    """Класс, представляющий библиотеку.
    Атрибуты:
    name (str): Название библиотеки.
    address (str): Адрес библиотеки.
    max_books (int): Максимальное количество разных книг.
    books (dict): Список книг в формате {название: количество}.
    """

    def __init__(self, name: str, address: str, max_books: int):
        """
        Инициализирует объект библиотеки.
        Аргументы:
        name (str): Название библиотеки.
        address (str): Адрес библиотеки.
        max_books (int): Максимальное количество разных книг.
        Исключения:
        ValueError: Если max_books меньше 1.
        """
        if max_books < 1:
            raise ValueError("Максимальное количество книг должно быть больше 0.")
        self.name = name
        self.address = address
        self.max_books = max_books
        self.books = {}

    def add_book(self, title: str, quantity: int) -> None:
        """
        Добавляет книгу в библиотеку.
        Аргументы:
        title (str): Название книги.
        quantity (int): Количество экземпляров.
        Исключения:
        ValueError: Если количество меньше 1 или библиотека достигла максимума книг.
        Пример:
        >>> library = Library("City Library", "123 Main St", 2)
        >>> library.add_book("1984", 3)
        >>> library.books
        {'1984': 3}
        """
        if len(self.books) >= self.max_books:
            raise ValueError("Библиотека достигла максимального количества разных книг.")
        if quantity < 1:
            raise ValueError("Количество должно быть больше 0.")
        self.books[title] = self.books.get(title, 0) + quantity

    def borrow_book(self, title: str) -> None:
        """
        Выдаёт книгу из библиотеки.
        Аргументы:
        title (str): Название книги.
        Исключения:
        KeyError: Если книги нет в библиотеке.
        ValueError: Если книга закончилась.
        Пример:
        >>> library = Library("City Library", "123 Main St", 2)
        >>> library.add_book("1984", 3)
        >>> library.borrow_book("1984")
        >>> library.books
        {'1984': 2}
        """
        if title not in self.books:
            raise KeyError(f"Книга '{title}' отсутствует в библиотеке.")
        if self.books[title] == 0:
            raise ValueError(f"Книга '{title}' закончилась.")
        self.books[title] -= 1

    def get_info(self) -> str:
        """
        Возвращает информацию о библиотеке.
        Возвращаемое значение:
        str: Информация о библиотеке.
        Пример:
        >>> library = Library("City Library", "123 Main St", 2)
        >>> library.get_info()
        'Библиотека: City Library, Адрес: 123 Main St, Максимум разных книг: 2'
        """
        return f"Библиотека: {self.name}, Адрес: {self.address}, Максимум разных книг: {self.max_books}"


if __name__ == "main":
    doctest.testmod()  # тестирование примеров, которые находятся в документации