import doctest

class Bed:
    def __init__(self, cleanliness: bool, occupancy: int):
        """
        Создание и подготовка к работе объекта "Кровать"

        :param cleanliness: Заправленность кровати
        :param occupancy: Занятость кровати

        examples:
        >>> bed = Bed(False, 2) # инициализация экземпляра класса
        """
        if not isinstance(cleanliness, bool):
            raise TypeError("Заправленность кровати должна быть типа bool")
        self.cleanliness = cleanliness

        if not isinstance(occupancy, int):
            raise TypeError("Занятость кровати должна быть целым числом")
        if occupancy < 0 or occupancy > 5:
            raise ValueError("Занятость кровати не может быть отрицательной или больше 5")
        self.occupancy = occupancy

    def clean_bed(self) -> None:
        """
        Заправление кровати.
        :raise ValueError: Если кровать уже заправлена и если кровать занята

        examples:
        >>> bed = Bed(False, 0)
        >>> bed.clean_bed()
        """
        if self.cleanliness is True:
            raise ValueError("Заправить можно только незаправленную кровать")
        if self.occupancy > 0:
            raise ValueError("Заправить можно только пустую кровать")
        self.cleanliness = True

    def do_bed(self) -> None:
        """
        Расстилание кровати.
        :raise ValueError: Если кровать не заправлена, её нельзя расстелить
        examples:
        >>> bed = Bed(True, 0)
        >>> bed.do_bed()
        """
        if self.cleanliness is False:
            raise ValueError("Расстелить можно только заправленную кровать")
        self.cleanliness = False

    def into_the_bed(self, man: int) -> None:
        """
        Лечь в кровать.
        :raise ValueError: Нельзя лечь в заправленную кровать и  в кровать, где нет места
        :raise TypeError: Добаление людей в кровать может быть выражено только целым числом
        examples:
        >>> bed = Bed(False, 0)
        >>> bed.into_the_bed(2)
        """
        if self.cleanliness is True:
            raise ValueError("Лечь можно только в расправленную кровать")
        if man + self.occupancy > 5:
            raise ValueError("Недостаточно места")
        if not isinstance(man, int):
            raise TypeError("Добаление людей в кровать может быть выражено только типом int")
        self.occupancy += man

    def from_bed(self, man: int) -> None:
        """
        Покинуть кровать.
        :raise ValueError: Покинуть кровать может только количество людей, находящихся в кровати
        :raise TypeError: Люди, покидающие кровать, могут быть выражены только целым числом
        examples:
        >>> bed = Bed(False, 3)
        >>> bed.from_bed(1)
        """
        if man > self.occupancy:
            raise ValueError("В кровати нет столько людей")
        if not isinstance(man, int):
            raise TypeError("Люди, покидающие кровать, могут быть выражены только типом int")
        self.occupancy -= man

if __name__ == "__main__":
    doctest.testmod()
    pass
