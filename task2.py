from mod2task1 import Fridge, BankAccount, Library  # Импортируем классы

if __name__ == "__main__":
    # Инстанцирование классов
    fridge = Fridge("LG", 300)
    account = BankAccount("123456", 1000.0, "USD")
    library = Library("City Library", "123 Main St", 5)

    # Тестирование методов с корректными данными
    print("=== Тестирование корректных вызовов ===")
    fridge.add_item("Milk", 2)
    print("Содержимое холодильника:", fridge.items)

    account.deposit(500.0)
    print("Баланс счёта после депозита:", account.balance)

    library.add_book("1984", 3)
    print("Книги в библиотеке:", library.books)

    # Тестирование некорректных данных
    print("\n=== Тестирование исключений ===")

    try:
        fridge.add_item("Milk", 0)  # Некорректное количество
    except ValueError as e:
        print(f"Ошибка: {e}")

    try:
        account.withdraw(2000.0)  # Сумма превышает баланс
    except ValueError as e:
        print(f"Ошибка: {e}")

    try:
        library.add_book("Too Many Books", 1)  # Превышение максимального количества разных книг
        library.add_book("Another Book", 1)
        library.add_book("Third Book", 1)
        library.add_book("Fourth Book", 1)
    except ValueError as e:
        print(f"Ошибка: {e}")