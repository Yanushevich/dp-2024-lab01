import threading
import os
from datetime import datetime
import log_level
import singleton


class Logger(singleton.Singleton):
    """Класс логгера для записи сообщений с указанными стратегиями формата и вывода"""

    def __init__(self, file_path: str):
        """Инициализация: создание файла"""
        _writer_lock = threading.Lock()
        self._create_file(file_path)

    def _create_file(self, file_path: str):
        """Создание файла"""
        timestamp = datetime.now().strftime('%Y-%m-%d.%H-%M-%S')
        log_filename = f'DP.P1.{timestamp}.log'
        self.log_file_path = os.path.join(file_path, log_filename)
        with open(self.log_file_path, 'w'):
            pass

    def _create_message(self, level: log_level.LogLevel, message: str) -> str:
        """Создание сообщения с указанным уровнем логирования и временной отметкой"""
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return f"{timestamp} [{level.value}] {message}\n"

    def log(self, level: log_level.LogLevel, message: str):
        """Логирует сообщение"""
        message = self._create_message(level, message)
        with self._writer_lock:
            with open(self.log_file_path, 'a') as log_file:
                log_file.write(message)
        print(message, end='')  # Для наглядного вывода в консоль
