from task1 import climb


def test_hight_3():
    print(list(climb(3)))
    assert set(list(climb(3))) == set(["111", "21", "12"])


def test_hight_4():
    print(list(climb(4)))
    assert set(list(climb(4))) == set(["1111", "22", "112", "121", "211"])


def test_hight_5():
    print(list(climb(5)))
    assert set(list(climb(5))) == set(['1112', '1121', '1211', '2111', '122', '212', '221', '11111'])