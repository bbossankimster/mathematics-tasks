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


def test_hight_8():
    print(list(climb(8)))
    assert set(list(climb(8))) == set(['1111112', '1111121', '1111211', '1112111', '1121111',
    '1211111', '2111111', '111122', '111212', '111221', '112112', '112121', '112211', '121112',
    '121121', '121211', '122111', '211112', '211121', '211211', '212111', '221111', '11222',
    '12122', '12212', '12221', '21122', '21212', '21221', '22112', '22121', '22211', '2222', '11111111'])


def test_hight_100():
    # don't run, takes a long time
    return 0
    count = len(list(climb(100)))
    assert count == 1000
