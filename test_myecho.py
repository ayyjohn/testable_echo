import random
import string
import pytest

from myecho import myecho, parse_args


def test__echo__with_no_args__returns_newline(capsys):
    parsed_args = parse_args([])

    myecho(parsed_args)

    captured = capsys.readouterr()
    assert captured.out == "\n"


def test__echo__with_n__strips_newline(capsys):
    random_other_args = [
        "".join(random.choice(string.ascii_lowercase))
        for i in range(5)
    ]
    args = random_other_args + ["-n"]
    parsed_args = parse_args(args)

    myecho(parsed_args)

    captured = capsys.readouterr()
    assert not captured.out.endswith("\n")
    for arg in random_other_args:
        assert arg in captured.out


def test__echo__with_escape_chars(capsys):
    assert False


def test__echo__with_escape_chars_and_e_on(capsys):
    assert False
