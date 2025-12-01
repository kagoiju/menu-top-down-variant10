# data_processing.py (Итерация 3 - Финальная реализация)
import re

VOWELS_RUS = 'аяуюоеёэиы'
CONSONANTS_RUS = 'бвгджзклмнпрстфхцчшщ'

def count_vowels_consonants(word: str) -> tuple[int, int]:
    """Считает количество гласных и согласных в одном слове."""
    vowel_count = 0
    consonant_count = 0
    lower_word = word.lower()
    
    for char in lower_word:
        if char in VOWELS_RUS:
            vowel_count += 1
        elif char in CONSONANTS_RUS:
            consonant_count += 1
            
    return vowel_count, consonant_count

def process_text_for_menu(text: str) -> dict:
    """
    Основной алгоритм (Вариант 10):
    Возвращает массив троек (слово, гласные, согласные) и общее кол-во гласных.
    """
    # Токенизация: извлечение русских слов, игнорируя знаки препинания
    words = re.findall(r'[а-яА-ЯёЁ]+', text)
    
    result_triplets = []
    total_vowels_in_text = 0
    
    for word in words:
        vowels, consonants = count_vowels_consonants(word)
        result_triplets.append((word, vowels, consonants))
        total_vowels_in_text += vowels
        
    return {
        "triplets": result_triplets,
        "total_vowels": total_vowels_in_text
    }