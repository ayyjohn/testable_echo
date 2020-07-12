import pytest
from myecho import myecho, parse_args


def test__echo__with_no_args__returns_newline(capsys):
    parsed_args = parse_args([])
    myecho(parsed_args)
    captured = capsys.readouterr()

    assert captured.out == "\n"


def test__echo__with_newline():
    assert False


def test__echo__with_escape_chars():
    assert False


def test__echo__with_escape_chars_and_e_on():
    assert False
