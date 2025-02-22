import nov24


def test_valid():
    tuples = [
        (1, 2),
        (1, 3),
        (3, 4),
        (20, 22),

    ]
    expected = [
        2,
        3,
        7,
        21,

    ]
    for i, t in enumerate(tuples):
        assert nov24.min_bajtalars(t[0], t[1]) == expected[i]


"""def test_multiply():
    raise NotImplementedError


def test_div():
    raise NotImplementedError


def test_prime():
    raise NotImplementedError"""
