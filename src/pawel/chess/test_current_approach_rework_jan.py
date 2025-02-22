from .current_approach_rework_jan import (
    check_is_even,
    check_is_odd,
    check_is_ratio_good,
    get_best_dimensions,
    draw_for_prime,
    draw_for_non_prime,
    prime,
    get_more_squareish,
    draw,
    solve
)


def test_check_is_even():
    assert check_is_even(2) == True
    assert check_is_even(3) == False


def test_check_is_odd():
    assert check_is_odd(2) == False
    assert check_is_odd(3) == True


def test_check_is_ratio_good():
    assert check_is_ratio_good(2, 4) == True
    assert check_is_ratio_good(2, 5) == False


def test_get_best_dimensions():
    assert get_best_dimensions(4) == (2, 2)
    assert get_best_dimensions(6) == (2, 3)
    assert get_best_dimensions(7) == (1, 7)


def test_draw_for_prime():
    assert draw_for_prime(2, 2, 0) == "GGPPDDLL"


def test_draw_for_non_prime():
    assert draw_for_non_prime(2, 2, 0) == "GGPPDDLL"


def test_prime():
    assert prime(2) == True
    assert prime(3) == True
    assert prime(4) == False
    assert prime(5) == True


def test_get_more_squareish():
    assert get_more_squareish(4) == (2, 2, 0, False)


def test_draw():
    assert draw(2, 2, 0, True) == "GGPPDDLL"


def test_solve():
    assert solve(4) == "GGPPDDLL"
