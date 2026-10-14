"""Модуль математической модели частиц дождя."""

import random


class RainDropModel:
    """Класс, описывающий состояние и математическую модель отдельной капли."""

    def __init__(self, screen_width: int, screen_height: int) -> None:
        """Инициализирует каплю дождя.

        Args:
            screen_width (int): Ширина области симуляции.
            screen_height (int): Высота области симуляции.
        """
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.x = 0.0
        self.y = 0.0
        self.speed = 0.0
        self.length = 0.0
        self.thickness = 1
        self.reset(initial=True)

    def reset(self, initial: bool = False) -> None:
        """Сбрасывает положение и характеристики капли.

        Args:
            initial (bool): Флаг первого запуска.
        """
        self.x = float(random.randint(0, self.screen_width))
        if initial:
            self.y = float(random.randint(0, self.screen_height))
        else:
            self.y = float(random.randint(-50, -10))

        self.speed = float(random.randint(4, 12))
        self.length = self.speed * 2.0
        self.thickness = 1 if self.speed < 8 else 2

    def update(self) -> None:
        """Выполняет один шаг перемещения капли вниз по оси Y."""
        self.y += self.speed
        if self.y > self.screen_height:
            self.reset(initial=False)