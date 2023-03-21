import types


def flat_generator(list_of_lists):
    for root_list in list_of_lists:
        for elem in root_list:
            yield elem


def test_2():

    list_of_lists_1 = [
                        ['a', 'b', 'c'],
                        [], [],
                        ['d', 'e', 'f', 'h', False],
                        [], [], [],
                        [1, 2, None],
                        [], []
                       ]

    print('Проверка поэлементно:')
    for flat_iterator_item, check_item in zip(flat_generator(list_of_lists_1), ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]):
        assert flat_iterator_item == check_item
        print(f'{flat_iterator_item} = {check_item}')


    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    print(f"\nПроверка списков:\n {list(flat_generator(list_of_lists_1))} = {['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]}")

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)
    print(f'\nПроверка типа: {type(flat_generator(list_of_lists_1))}')


if __name__ == '__main__':
    test_2()

