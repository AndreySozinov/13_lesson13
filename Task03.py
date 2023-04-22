# Создайте класс с базовым исключением и дочерние классы-исключения:
# ○ ошибка уровня,
# ○ ошибка доступа.
class MyBaseException(Exception):
    pass


class LevelError(MyBaseException):
    def __init__(self, value, value2):
        self.value = value
        self.value2 = value2

    def __str__(self):
        return f'Level Error: your level {self.value} is lesser than required - {self.value2}'


class AccessError(MyBaseException):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'Access Error: no user with name {self.value}'
