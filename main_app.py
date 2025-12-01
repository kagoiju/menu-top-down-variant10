# main_app.py (Итерация 3 - Финальная версия)

from menu_template import start_menu
from data_processing import process_text_for_menu
from random import choice

# --- ГЛОБАЛЬНОЕ СОСТОЯНИЕ ---
INPUT_DATA = None
ALGORITHM_RESULT = None

# ... (Функции input_data_manually, input_data_random, menu_input_data, execute_algorithm
# остаются как в Итерации 2, но execute_algorithm теперь вызывает РЕАЛЬНЫЙ алгоритм)

def input_data_manually():
    # КОД ИЗ ИТЕРАЦИИ 2
    global INPUT_DATA, ALGORITHM_RESULT
    user_input = input("Введите текст: ")
    if user_input.strip():
        INPUT_DATA = user_input
        ALGORITHM_RESULT = None
        print("Данные успешно введены. Результат алгоритма сброшен.")
    else:
        print("Ввод отменен. Данные не изменены.")
    input("Нажмите Enter для продолжения...")

def input_data_random():
    # КОД ИЗ ИТЕРАЦИИ 2
    global INPUT_DATA, ALGORITHM_RESULT
    sentences = ["...", "...", "..."] # Ваш список фраз
    INPUT_DATA = choice(sentences)
    ALGORITHM_RESULT = None
    print(f"Случайный текст сгенерирован: '{INPUT_DATA}'")
    print("Результат алгоритма сброшен.")
    input("Нажмите Enter для продолжения...")

def menu_input_data():
    # КОД ИЗ ИТЕРАЦИИ 2
    caption_start = "\n--- Ввод Исходных Данных ---\n 1) Ввод вручную \n 2) Случайная генерация \n 0) Назад \n"
    menu_template = {0: (lambda: True, True), 1: (input_data_manually, True), 2: (input_data_random, True)}
    start_menu(caption_start, 'Ошибка ввода', menu_template)

def execute_algorithm():
    # КОД ИЗ ИТЕРАЦИИ 2
    global ALGORITHM_RESULT
    if INPUT_DATA is None:
        print("!!! ОШИБКА: Сначала необходимо ввести исходные данные (пункт 1).")
        input("Нажмите Enter для продолжения...")
        return
    print(f">>> Выполнение алгоритма для текста: '{INPUT_DATA[:30]}...'")
    ALGORITHM_RESULT = process_text_for_menu(INPUT_DATA)
    print("Алгоритм выполнен. Результат сохранен.")
    input("Нажмите Enter для продолжения...")

def display_result():
    """Финальная реализация: Вывод результата."""
    global ALGORITHM_RESULT
    
    if ALGORITHM_RESULT is None:
        print("!!! ОШИБКА: Сначала необходимо выполнить алгоритм (пункт 2).")
        input("Нажмите Enter для продолжения...")
        return

    triplets = ALGORITHM_RESULT.get('triplets', [])
    total_vowels = ALGORITHM_RESULT.get('total_vowels', 0)
    
    print("\n--- РЕЗУЛЬТАТ АЛГОРИТМА (Вариант 10) ---\n")
    print(f"Исходный текст: {INPUT_DATA}")
    
    print("\nМассив троек (Слово, Кол-во гласных, Кол-во согласных):")
    if not triplets:
        print("  <Не было найдено слов для анализа>")
    else:
        for word, vowels, consonants in triplets:
            print(f"  - '{word}': {vowels} гласных, {consonants} согласных")
            
    print(f"\nОбщее количество гласных в тексте: **{total_vowels}**")
    
    print("\n------------------------------------------------\n")
    input("Нажмите Enter для продолжения...")

def menu_main():
    # КОД ИЗ ИТЕРАЦИИ 2
    caption_start = "\n--- ГЛАВНОЕ МЕНЮ ---\n 1) Ввод исходных данных \n 2) Выполнение алгоритма \n 3) Вывод результата \n 0) Завершение работы \n"
    menu_template = {0: (lambda: True, True), 1: (menu_input_data, False), 2: (execute_algorithm, False), 3: (display_result, False)}
    print("Приложение запущено.")
    start_menu(caption_start, 'Некорректный ввод', menu_template)
    print("Работа приложения завершена.")

if __name__ == "__main__":
    menu_main()