# Создайте функцию, которая запрашивает числовые данные от
# пользователя до тех пор, пока он не введёт целое или вещественное число.
# 📌 Обрабатывайте не числовые данные как исключения.
def give_me_number() -> int | float:
    while True:
        a = input('Enter a number, please: ')
        try:
            number = int(a)
            return number
        except ValueError:
            try:
                number = float(a)
                return number
            except ValueError as e:
                print(f'Wrong value - {e}')


if __name__ == '__main__':
    print(give_me_number())
