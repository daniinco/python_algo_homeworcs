def group_anagrams(words: list[str]) -> list[list[str]]:
    """
    Группирует анаграммы в массиве строк.

    Args:
        words: Массив строк.
    
    Returns:
        Массив групп анаграмм.
    """
    groups = {}
    for word in words:
        hash_sum = 0
        for letter in word:
            hash_sum += hash(letter)
        if hash_sum not in groups:
            groups[hash_sum] = []
        groups[hash_sum].append(word)
    return list(groups.values())
