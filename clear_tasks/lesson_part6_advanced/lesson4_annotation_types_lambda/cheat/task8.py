# Задание 8: Словарь с типами
#
# Создайте функцию count_occurrences, которая принимает список строк и возвращает словарь,
# где ключи — это строки, а значения — количество их вхождений в списке. Укажите аннотации типов.

from typing import List, Dict


def count_occurrences(words: List[str]) -> Dict[str, int]:
    occurrences = {}
    for word in words:
        occurrences[word] = occurrences.get(word, 0) + 1
    return occurrences
