from typing import Dict, Any


class HashTable:
    """
    Класс хеш-таблицы.
    """

    def __init__(self, input_dict: dict[Any, Any] = None):
        """
        Инициализация хеш-таблицы.

        Args:
            input_dict: Словарь для инициализации хеш-таблицы. Если None, то инициализация пустой хеш-таблицы.
        """

        if input_dict is None:
            self.length = 0
            self.space_size = 20
            self.data = [[] for _ in range(self.space_size)]
        else:
            self.length = len(input_dict)
            self.space_size = self.length * 5
            self.data = [[] for _ in range(self.space_size)]
            for key, value in input_dict.items():
                self.data[hash(key) % self.space_size].append((key, value))
    
    def __setitem__(self, key: Any, value: Any) -> None:
        """
        Добавляет новый ключ-значение в хеш-таблицу.
        Если ключ уже существует, то обновляет значение.
        Если количество ключей в хеш-таблице превышает 66% от ее размера, то удваивает размер хеш-таблицы.

        Args:
            key: Ключ.
            value: Значение.
        """

        if value not in self.data[hash(key) % self.space_size]:
            self.data[hash(key) % self.space_size] = [(key, value)]
            self.length += 1
        else:
            del self[key]
            self.data[hash(key) % self.space_size] = [(key, value)]
            self.length += 1
        if self.length > int(self.space_size * 0.66):
            self.space_size *= 2
            self.new_data = [[] for _ in range(self.space_size)]
            for cell in self.data:
                for key, value in cell:
                    self.new_data[hash(key) % self.space_size].append((key, value))
            self.data = self.new_data
    
    def __getitem__(self, key: Any) -> Any:
        """
        Возвращает значение по ключу.

        Args:
            key: Ключ.
        Returns:
            Значение.
        """
        for key_, value in self.data[hash(key) % self.space_size]:
            if key == key_:
                return value
        raise IndexError("Key not found")
    
    def __delitem__(self, key: Any) -> None:
        """
        Удаляет ключ-значение из хеш-таблицы.

        Args:
            key: Ключ.
        """
        for key, value in self.data[hash(key) % self.space_size]:
            if key == key:
                self.data[hash(key) % self.space_size].remove((key, value))
                self.length -= 1    
    
    def __contains__(self, key: Any) -> bool:
        """
        Возвращает True, если ключ существует в хеш-таблице.

        Args:
            key: Ключ.
        Returns:
            True, если ключ существует в хеш-таблице. Иначе False.
        """
        for key_, _ in self.data[hash(key) % self.space_size]:
            if key == key_:
                return True
        return False