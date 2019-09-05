from decimal_time import decimal_time


def test_fib() -> None:
    assert decimal_time.fib(0) == 0
    assert decimal_time.fib(1) == 1
    assert decimal_time.fib(2) == 1
    assert decimal_time.fib(3) == 2
    assert decimal_time.fib(4) == 3
    assert decimal_time.fib(5) == 5
    assert decimal_time.fib(10) == 55
