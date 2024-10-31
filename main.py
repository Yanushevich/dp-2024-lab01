from logger import Logger
import log_level

if __name__ == '__main__':
    """Пример использования"""
    logger = Logger('./logs')
    logger.log(log_level.LogLevel.INFO, 'Application started successfully')
    logger.log(log_level.LogLevel.ERROR, 'An error occurred')
    logger2 = Logger('./logs')
    logger2.log(log_level.LogLevel.INFO, 'Testing new instance')
    logger2.log(log_level.LogLevel.WARN, 'Warning message')
