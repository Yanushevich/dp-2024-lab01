from enum import Enum


class LogLevel(Enum):
    """
    Перечисление различных уровней логирования

    Attributes:
        INFO (str) - Информационные сообщения
        TRACE (str) - Подробные сообщения для отслеживания выполнения
        WARN (str) - Предупреждающие сообщения
        ERROR (str) - Сообщения об ошибках, сбоях
        FATAL (str) - Критические сообщения об ошибках
    """
    INFO = "INFO"
    TRACE = "TRACE"
    WARN = "WARN"
    ERROR = "ERROR"
    FATAL = "FATAL"
