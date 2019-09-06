#

from colorama import Fore

from decimal_time import decimal_time

# from decimal_time.decimal_time import color_time_list, main, return_time_list


ts = 1440950558
expect_ts = "14:4:0:9 5:05:58"
expect_tl = ["14", "4", "0", "9", "5", "05", "58"]
colors = [
    Fore.MAGENTA,
    Fore.BLUE,
    Fore.CYAN,
    Fore.GREEN,
    Fore.YELLOW,
    Fore.RED,
    Fore.WHITE,
]


def test_time_string():
    assert decimal_time.time_string(ts) == expect_ts


def test_return_time_list():
    assert decimal_time.return_time_list(ts) == expect_tl


def test_color_time_list():
    cl = decimal_time.color_time_list(expect_tl)
    ecl = ["".join(i) for i in zip(colors, expect_tl, [Fore.RESET] * len(expect_tl))]
    for i in zip(cl, ecl):
        assert i[0] == i[1]


# this is a crap test.
def test_main():
    assert decimal_time.main([]) is None


def test_foo():
    assert True


##
