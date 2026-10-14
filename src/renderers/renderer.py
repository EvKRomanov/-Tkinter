"""Модуль графического отображения элементов симуляции."""

import tkinter as tk
from typing import Dict, List
from src.models.animation_model import RainDropModel


class RainRenderer:
    """Класс, отвечающий за визуализацию капель дождя на холсте Tkinter."""

    def __init__(self, canvas: tk.Canvas) -> None:
        """Инициализирует визуализатор холста.

        Args:
            canvas (tk.Canvas): Холст Tkinter для отрисовки графических примитивов.
        """
        self.canvas = canvas
        self.items: Dict[RainDropModel, int] = {}

    def init_particles(self, particles: List[RainDropModel]) -> None:
        """Создает графические примитивы линий для всех переданных моделей.

        Args:
            particles (List[RainDropModel]): Список моделей капель.
        """
        for drop in particles:
            item_id = self.canvas.create_line(
                drop.x,
                drop.y,
                drop.x,
                drop.y + drop.length,
                fill="#4a76a8",
                width=drop.thickness,
            )
            self.items[drop] = item_id

    def render(self, particles: List[RainDropModel]) -> None:
        """Обновляет экранные координаты линий на холсте.

        Args:
            particles (List[RainDropModel]): Список моделей капель.
        """
        for drop in particles:
            item_id = self.items.get(drop)
            if item_id is not None:
                self.canvas.coords(
                    item_id,
                    drop.x,
                    drop.y,
                    drop.x,
                    drop.y + drop.length,
                )