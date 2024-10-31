import threading


class Singleton:
    """Класс, обеспечивающий создание единственного экземпляра"""
    _instance = None
    _creator_lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        """Создание единственного экземпляра"""
        if cls._instance is None:
            with cls._creator_lock:
                if cls._instance is None:
                    cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance
