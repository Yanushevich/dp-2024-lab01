import threading
import os
from datetime import datetime


class Singleton:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            with cls._lock:
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

    def log(self, level: str, message: str):
        """Запись лога в файл"""
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_message = f"{timestamp} [{level}] {message}\n"
        with self._lock:
            with open(self.log_file_path, 'a') as log_file:
                log_file.write(log_message)
        print(log_message, end='')  # Для наглядного вывода в консоль


"""Пример использования"""
if __name__ == '__main__':
    logger = Logger('C:/Users/Максим/PycharmProjects/dp-2024-lab01')
    logger.log('INFO', 'Application started successfully')
    logger.log('ERROR', 'An error occurred')