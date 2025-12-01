# data_processing.py (Итерация 2)
import re

VOWELS_RUS = 'аяуюоеёэиы'
CONSONANTS_RUS = 'бвгджзклмнпрстфхцчшщ'

def process_text_for_menu(text: str):
    """
    Заглушка для Варианта 10.
    Возвращает структуру, ожидаемую на выходе.
    """
    print(f"Обработка текста (вызов заглушки): '{text[:20]}...'")
    # Возвращаем "образец" результата в виде, удобном для Итерации 3
    return {"triplets": [("Тест", 2, 2)], "total_vowels": 2}