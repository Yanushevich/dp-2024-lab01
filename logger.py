import threading
import os
from datetime import datetime
import log_level
import singleton


class Logger(singleton.Singleton):
    """Класс логгера для записи сообщений с указанными стратегиями формата и вывода"""

    def __init__(self, file_path: str):
        """
        Инициализация: создание файла

        Args:
            file_path (str): Путь к файлу
        """
        self._writer_lock = threading.Lock()
        self._create_file(file_path)

    def _create_file(self, file_path: str) -> None:
        """
        Метод создания файла

        Args:
            file_path (str): Путь к файлу
        """
        timestamp = datetime.now().strftime('%Y-%m-%d.%H-%M-%S')
        log_filename = f'DP.P1.{timestamp}.log'
        self.log_file_path = os.path.join(file_path, log_filename)
        with open(self.log_file_path, 'w'):
            pass

    def _create_message(self, level: log_level.LogLevel, message: str) -> str:
        """
        Создание сообщения с указанным уровнем логирования и временной отметкой

        Args:
            level (log_level.LogLevel): Уровень логирования из перечисления
            message (str): Текстовое сообщение
        """
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return f"{timestamp} [{level.value}] {message}\n"

    def log(self, level: log_level.LogLevel, message: str):
        """
        Логирует сообщение

        Args:
            level (log_level.LogLevel): Уровень логирования из перечисления
            message (str): Текстовое сообщение
        """
        message = self._create_message(level, message)
        with self._writer_lock:
            with open(self.log_file_path, 'a') as log_file:
                log_file.write(message)
