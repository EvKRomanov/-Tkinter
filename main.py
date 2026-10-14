"""Точка входа в программу симуляции дождя."""

from src.app import App


def main() -> None:
    """Запуск приложения."""
    app = App()
    app.run()


if __name__ == "__main__":
    main()