import threading
import os
from datetime import datetime
import log_level


class Singleton:
    _instance = None
    _writer_lock = threading.Lock()
    _creator_lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            with cls._creator_lock:
                if cls._instance is None:
                    cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance


class Logger(Singleton):
    def __init__(self, file_path: str):
        """Инициализация: создание файла"""
        self._create_file(file_path)

    def _create_file(self, file_path: str):
        """Создание файла"""
        timestamp = datetime.now().strftime('%Y-%m-%d.%H-%M-%S')
        log_filename = f'DP.P1.{timestamp}.log'
        self.log_file_path = os.path.join(file_path, log_filename)
        with open(self.log_file_path, 'w'):
            pass

    def _create_message(self, level: log_level.LogLevel, message: str) -> str:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return f"{timestamp} [{level.value}] {message}\n"

    def log(self, level: log_level.LogLevel, message: str):
        message = self._create_message(level, message)
        with self._writer_lock:
            with open(self.log_file_path, 'a') as log_file:
                log_file.write(message)
        print(message, end='')  # Для наглядного вывода в консоль


if __name__ == '__main__':
    """Пример использования"""
    logger = Logger(f'C:/Users/{os.getlogin()}/PycharmProjects/dp-2024-lab01')
    logger.log(log_level.LogLevel.INFO, 'Application started successfully')
    logger.log(log_level.LogLevel.ERROR, 'An error occurred')
    logger2 = Logger(f'C:/Users/{os.getlogin()}/PycharmProjects/dp-2024-lab01')
    logger2.log(log_level.LogLevel.INFO, 'Testing new instance')
    logger2.log(log_level.LogLevel.WARN, 'Warning message')
