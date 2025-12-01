# main_app.py (Итерация 1)
from menu_template import start_menu

# --- ГЛОБАЛЬНОЕ СОСТОЯНИЕ ---
INPUT_DATA = None       # Исходный текст
ALGORITHM_RESULT = None # Результат алгоритма. Сброс при новом вводе.

def input_data_manually():
    """Заглушка: Ввод данных вручную. Имитация ввода и сброс состояния."""
    global INPUT_DATA, ALGORITHM_RESULT
    print(">>> (Заглушка) Ввод данных вручную: 'Test Text'")
    INPUT_DATA = "Test Text"
    ALGORITHM_RESULT = None
    print("Состояние: Данные введены, Результат сброшен.")
    input("Нажмите Enter...")

def input_data_random():
    """Заглушка: Случайная генерация. Имитация генерации и сброс состояния."""
    global INPUT_DATA, ALGORITHM_RESULT
    print(">>> (Заглушка) Случайная генерация: 'Random Text'")
    INPUT_DATA = "Random Text"
    ALGORITHM_RESULT = None
    print("Состояние: Данные введены, Результат сброшен.")
    input("Нажмите Enter...")

def menu_input_data():
    """Подменю: Ввод исходных данных."""
    caption_start = "\n--- Ввод Исходных Данных ---\n 1) Ввод вручную \n 2) Случайная генерация \n 0) Назад \n"
    menu_template = {
        0: (lambda: True, True),
        1: (input_data_manually, True),
        2: (input_data_random, True)}
    start_menu(caption_start, 'Ошибка ввода', menu_template)

def execute_algorithm():
    """Заглушка: Выполнение алгоритма (Вариант 10)."""
    global ALGORITHM_RESULT
    if INPUT_DATA is None:
        print("!!! ОШИБКА: Сначала необходимо ввести исходные данные.")
        input("Нажмите Enter...")
        return
    
    print(f">>> (Заглушка) Выполнение алгоритма для: '{INPUT_DATA}'")
    # Фиктивный результат для проверки логики
    ALGORITHM_RESULT = "Результат: [(слово, 2, 3), (текст, 1, 3)], Общее: 3"
    print("Состояние: Алгоритм выполнен, Результат сохранен.")
    input("Нажмите Enter...")

def display_result():
    """Заглушка: Вывод результата."""
    if ALGORITHM_RESULT is None:
        print("!!! ОШИБКА: Сначала необходимо выполнить алгоритм.")
        input("Нажмите Enter...")
        return
    
    print("\n--- (Заглушка) РЕЗУЛЬТАТ ---\n")
    print(ALGORITHM_RESULT)
    print("\n---------------------------\n")
    input("Нажмите Enter...")

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