class FlatIterator:

    def __init__(self, list_of_list):
        self.data = list_of_list

    def __iter__(self):
        self.root_index = 0
        self.next_index = 0
        return self

    def _check_stop(self):
        if self.root_index >= len(self.data):
            raise StopIteration

    def __next__(self):
        # Проверяем на окончание списка
        self._check_stop()

        # Дополнительная проверка на присутствие пустого элемента в середине списке и в конце
        while self.next_index >= len(self.data[self.root_index]):
            self.next_index = 0
            self.root_index += 1

            # Проверяем на окончание списка
            self._check_stop()

        # Основная реализация
        item = self.data[self.root_index][self.next_index]
        self.next_index += 1
        if self.next_index >= len(self.data[self.root_index]):
            self.next_index = 0
            self.root_index += 1

        return item


def test_1():

    list_of_lists_1 = [
                        ['a', 'b', 'c'],
                        [], [],
                        ['d', 'e', 'f', 'h', False],
                        [], [], [],
                        [1, 2, None],
                        [], []
                       ]

    flat = FlatIterator(list_of_lists_1)
    list_2 = ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    print('Проверка поэлементно:')
    for flat_iterator_item, check_item in zip(flat, list_2):
        assert flat_iterator_item == check_item
        print(f'{flat_iterator_item} = {check_item}')

    assert list(flat) == list_2
    print(f"\nПроверка списков:\n{list(flat)} = {list_2}")


if __name__ == '__main__':
    test_1()


