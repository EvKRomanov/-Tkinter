"""Главный модуль графического приложения и цикла анимации."""

import tkinter as tk
from typing import List
from src.models.animation_model import RainDropModel
from src.renderers.renderer import RainRenderer


class App:
    """Основной класс приложения для управления жизненным циклом симуляции."""

    WIDTH = 800
    HEIGHT = 600
    PARTICLE_COUNT = 120
    FRAME_DELAY_MS = 16

    def __init__(self) -> None:
        """Инициализирует окно приложения, холст, модель и визуализатор."""
        self.root = tk.Tk()
        self.root.title("Лабораторная работа: Симуляция дождя")
        self.root.resizable(False, False)

        self.canvas = tk.Canvas(
            self.root,
            width=self.WIDTH,
            height=self.HEIGHT,
            bg="#1a1c23",
            highlightthickness=0,
        )
        self.canvas.pack()

        self.particles: List[RainDropModel] = [
            RainDropModel(self.WIDTH, self.HEIGHT)
            for _ in range(self.PARTICLE_COUNT)
        ]

        self.renderer = RainRenderer(self.canvas)
        self.renderer.init_particles(self.particles)

    def _loop(self) -> None:
        """Один шаг главного цикла анимации."""
        for drop in self.particles:
            drop.update()
        self.renderer.render(self.particles)
        self.root.after(self.FRAME_DELAY_MS, self._loop)

    def run(self) -> None:
        """Запускает симуляцию и главный цикл событий Tkinter."""
        self._loop()
        self.root.mainloop()