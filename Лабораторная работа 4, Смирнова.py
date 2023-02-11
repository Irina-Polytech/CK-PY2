if __name__ == "__main__":

    class Spotlight:
        """Базовый класс прожекторов"""
        def __init__(self, id: int, socket_number: int):
            self.__id = id #Идентификационный номер прожектора устанавливается единожды и не подлежит замене.
            self.socket_number = socket_number

        def __str__(self) -> str:
            return f'Прожектор №{self.__id}'

        def __repr__(self) -> str:
            return f'{self.__class__.__name__} №{self.__id}'

        @classmethod
        def change_socket(cls, new_socket: int):
            """Метод используется при настройке театрального света,
            позволяя изменять розетки при смене места положения прожектора"""
            cls = self.__class__
            cls.socket_number = new_socket

    class LampSpotlight(Spotlight):
        """Дочерний класс прожекторов: Ламповые"""
        def __init__(self, id: int, socket_number: int, lens: str, filter_color: str):
            super().__init__(id)
            self.lens = lens
            self.filter_color = filter_color

    class HalogenSpotlight(Spotlight):
        """Дочерний класс прожекторов: Галогенные"""
        def __init__(self, id: int, socket_number: int, power: int, glass_color: str):
            super().__init__(id)
            self.power = power
            self.glass_color = glass_color

        def __str__(self) -> str:
        #В осветительской терминологии галогенный прожектор называют Лягушка, поэтому в списке название удобнее выводить в привычном формате.
            return f'Лягушка №{self.__id}'

    class LedSpotlight(Spotlight):
        """Дочерний класс прожекторов: Светодиодные"""
        def __init__(self, id: int, socket_number: int, RGB: str):
            super().__init__(id)
            self.RGB = RGB

        def change_rgb(self, new_rgb: str):
            """Метод, изменяющий цвет светодиодной лампы в спектре RGB"""
            self.RGB = new_rgb

pass
