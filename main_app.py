# main_app.py (Итерация 2)

from menu_template import start_menu
from data_processing import process_text_for_menu # <-- ИМПОРТ ЗАГЛУШКИ АЛГОРИТМА
from random import choice # <-- ИМПОРТ ДЛЯ СЛУЧАЙНОЙ ГЕНЕРАЦИИ

# --- ГЛОБАЛЬНОЕ СОСТОЯНИЕ ---
INPUT_DATA = None       # Исходный текст
ALGORITHM_RESULT = None # Результат алгоритма. Сбрасывается при новом вводе.

def input_data_manually():
    """Реализация: Ввод данных вручную. Обновляет INPUT_DATA и сбрасывает ALGORITHM_RESULT."""
    global INPUT_DATA, ALGORITHM_RESULT
    
    user_input = input("Введите текст: ")
    
    if user_input.strip():
        INPUT_DATA = user_input
        ALGORITHM_RESULT = None # Сброс результата при вводе новых данных
        print("Данные успешно введены. Результат алгоритма сброшен.")
    else:
        print("Ввод отменен. Данные не изменены.")
        
    input("Нажмите Enter для продолжения...")

def input_data_random():
    """Реализация: Случайная генерация данных. Обновляет INPUT_DATA и сбрасывает ALGORITHM_RESULT."""
    global INPUT_DATA, ALGORITHM_RESULT
    
    sentences = [
        "Это тестовый текст, чтобы проверить логику Варианта 10.",
        "Каждая итерация нисходящего проектирования важна.",
        "Пример предложения со знаками препинания: точка, запятая!"
    ]
    
    INPUT_DATA = choice(sentences)
    ALGORITHM_RESULT = None # Сброс результата при вводе новых данных
    
    print(f"Случайный текст сгенерирован: '{INPUT_DATA}'")
    print("Результат алгоритма сброшен.")
    input("Нажмите Enter для продолжения...")

def menu_input_data():
    """Подменю: Ввод исходных данных."""
    caption_start = "\n--- Ввод Исходных Данных ---\n 1) Ввод вручную \n 2) Случайная генерация \n 0) Назад \n"
    menu_template = {
        0: (lambda: True, True),
        1: (input_data_manually, True), # Возврат в главное меню
        2: (input_data_random, True)}   # Возврат в главное меню
        
    start_menu(caption_start, 'Ошибка ввода', menu_template)

def execute_algorithm():
    """Реализация: Выполнение алгоритма (Вариант 10) с проверкой наличия данных."""
    global ALGORITHM_RESULT
    
    # ПРОВЕРКА 1: Алгоритм не может быть выполнен без введенных данных
    if INPUT_DATA is None:
        print("!!! ОШИБКА: Сначала необходимо ввести исходные данные (пункт 1).")
        input("Нажмите Enter для продолжения...")
        return
    
    print(f">>> Выполнение алгоритма для текста: '{INPUT_DATA[:30]}...'")
    
    # Вызов заглушки из data_processing
    # В Итерации 3 эта функция будет заменена на реальный код
    ALGORITHM_RESULT = process_text_for_menu(INPUT_DATA)
    
    print("Алгоритм выполнен. Результат сохранен.")
    input("Нажмите Enter для продолжения...")

def display_result():
    """Реализация: Вывод результата с проверкой выполнения алгоритма."""
    
    # ПРОВЕРКА 2: Вывод результата не может быть осуществлен без выполнения алгоритма
    if ALGORITHM_RESULT is None:
        print("!!! ОШИБКА: Сначала необходимо выполнить алгоритм (пункт 2).")
        input("Нажмите Enter для продолжения...")
        return
    
    print("\n--- (Заглушка) РЕЗУЛЬТАТ АЛГОРИТМА ---\n")
    # В Итерации 3 здесь будет форматированный вывод
    print(ALGORITHM_RESULT)
    print("\n---------------------------------------\n")
    input("Нажмите Enter для продолжения...")

def menu_main():
    """Главное меню."""
    caption_start = "\n--- ГЛАВНОЕ МЕНЮ ---\n 1) Ввод исходных данных \n 2) Выполнение алгоритма \n 3) Вывод результата \n 0) Завершение работы \n"
    menu_template = {
        0: (lambda: True, True),
        1: (menu_input_data, False),
        2: (execute_algorithm, False),
        3: (display_result, False)}
    
    print("Приложение запущено.")
    start_menu(caption_start, 'Некорректный ввод', menu_template)
    print("Работа приложения завершена.")

if __name__ == "__main__":
    menu_main()