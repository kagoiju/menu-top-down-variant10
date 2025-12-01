def is_int(s):
    """
    Проверка на то, что s - целое число
    """
    try:
        if type(s) is int:
            return True
        if s is None:
            return False
        if not s.isdecimal():
            return False
        int(s)
        return True
    except (Exception, ValueError, TypeError):
        return False


def entering_valid_value_integer(message_input: str, message_err: str, template: list):
    """
    Ввод допустимого целого числа
    :param message_input: Сообщение перед вводом
    :param message_err:     Сообщение при вводе символа, не из шаблона
    :param template:        Список допустимых значений
    :return: целое число
    """
    while True:
        ch = input(message_input, )
        if is_int(ch):
            ch = int(ch)
            if ch in template:
                return ch
        print(message_err)


def start_menu(message_input: str, message_err: str, template: dict):
    """
    Универсальное меню. Выбор пункта меню вводом его номера
    :param message_input: Сообщение перед вводом
    :param message_err:     Сообщение при вводе символа, не из шаблона
    :param template: словарь, где ключ - номер меню. Значение - кортеж (f, is_break)
                             f            - функция, которая вызовиться
                             is_break == True  - выход из меню после вызова f
                             is_break == False - остаёмся в меню после вызова f
    """
    while True:
        # Ввод корректного ch
        ch = entering_valid_value_integer(message_input,
                                          message_err,
                                          list(template))
        # Выбор действия
        f, is_break = template[ch]
        f()
        if is_break:
            break
    # завершение программы
    return False

# Код ниже также должен быть скопирован, но он служит только для тестов, если запускать menu_template.py напрямую.
if __name__ == "__main__":
    # тесты

    caption_start = "menu_main \n 1) f1 \n 2) f2 \n 0) exit \n"
    caption_err = 'err'
    menu_template = {
        0: (lambda: True, True),
        1: (lambda: print("f1"), False),
        2: (lambda: print("f2"), False)}  
    start_menu(caption_start, caption_err, menu_template)

    exit(0)