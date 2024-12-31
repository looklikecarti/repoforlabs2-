from typing import Any


class Device:
    """
    базовый класс для всех устройств.

    атрибуты:
        brand (str): бренд устройства.
        model (str): модель устройства.
        price (float): цена устройства.
    """

    def __init__(self, brand: str, model: str, price: float) -> None:
        """
        инициализация базового устройства.

        аргументы:
            brand (str): бренд устройства.
            model (str): модель устройства.
            price (float): цена устройства.
        """
        self._brand = brand  # Инкапсуляция для защиты от изменения напрямую
        self._model = model
        self._price = price

    def __str__(self) -> str:
        return f"{self._brand} {self._model} - {self._price:.2f} руб."

    def __repr__(self) -> str:
        return f"Device('{self._brand}', '{self._model}', {self._price})"

    def get_info(self) -> str:
        """
        возвращает информацию об устройстве.
        """
        return f"Устройство: {self._brand} {self._model}"


class Smartphone(Device):
    """
    дочерний класс для смартфонов.

    атрибуты:
        os (str): операционная система смартфона.
    """

    def __init__(self, brand: str, model: str, price: float, os: str) -> None:
        """
        инициализация смартфона.

        аргументы:
            brand (str): бренд устройства.
            model (str): модель устройства.
            price (float): цена устройства.
            os (str): операционная система смартфона.
        """
        super().__init__(brand, model, price)
        self._os = os

    def __str__(self) -> str:
        return f"{self._brand} {self._model} ({self._os}) - {self._price:.2f} руб."

    def get_info(self) -> str:
        """
        переопределение метода для вывода дополнительной информации о смартфоне.

        по причине: смартфоны имеют уникальные особенности, такие как ОС.
        """
        return f"Смартфон: {self._brand} {self._model}, ОС: {self._os}"


class Laptop(Device):
    """
    дочерний класс для ноутбуков.

    атрибуты:
        cpu (str): процессор ноутбука.
        ram (int): объём оперативной памяти в ГБ.
    """

    def __init__(self, brand: str, model: str, price: float, cpu: str, ram: int) -> None:
        """
        инициализация ноутбука.

        аргументы:
            brand (str): бренд устройства.
            model (str): модель устройства.
            price (float): цена устройства.
            cpu (str): процессор устройства.
            ram (int): объём оперативной памяти.
        """
        super().__init__(brand, model, price)
        self._cpu = cpu
        self._ram = ram

    def __str__(self) -> str:
        return f"{self._brand} {self._model} ({self._cpu}, {self._ram}GB RAM) - {self._price:.2f} руб."

    def upgrade_ram(self, additional_ram: int) -> None:
        """
        увеличивает объём оперативной памяти.

        аргументы:
            additional_ram (int): количество добавляемой оперативной памяти.
        """
        self._ram += additional_ram
        print(f"Объём оперативной памяти увеличен до {self._ram} ГБ.")

#...атрибуты brand, model и price сделаны непубличными, чтобы защитить их от изменения напрямую и обеспечить контроль через методы класса.

phone = Smartphone("Samsung", "Galaxy S23", 79999, "Android")
laptop = Laptop("Apple", "MacBook Pro", 149999, "M2", 16)

print(phone)
print(laptop)

print(phone.get_info())
laptop.upgrade_ram(8)