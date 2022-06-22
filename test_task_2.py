from task2 import highest_sum_range


def test_all_negative():
    data = [-5, -5, -6, -7, -2, -3]
    assert highest_sum_range(data) == (4, 4)


def test_all_positive():
    data = [1, 5, 6, 7, 2, 3]
    assert highest_sum_range(data) == (0, 5)


def test_mixed_1():
    data = [1, 1, 1, -100, 1, 1]
    assert highest_sum_range(data) == (0, 2)


def test_mixed_2():
    data = [0, 10, 20, -647, 10, 4, 20]
    assert highest_sum_range(data) == (4, 6)


def test_mixed_3():
    data = [-100, -100, 1, -100]
    assert highest_sum_range(data) == (2, 2)
