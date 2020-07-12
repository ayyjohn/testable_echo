import random
import string
import pytest

from myecho import myecho, parse_args, ESCAPE_CHARS


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


def test__echo__with_e_flag__escapes_chars(capsys):
    args = ["-e", "yeet"]
    args += ESCAPE_CHARS.keys()
    parsed_args = parse_args(args)

    myecho(parsed_args)

    captured = capsys.readouterr()
    assert "yeet" in captured.out
    for escape_char, escaped_char in ESCAPE_CHARS.items():
        assert escape_char not in captured.out
        assert escaped_char in captured.out


def test__echo__default__doesnt_escape_chars(capsys):
    args = ["-n", "yeet"]
    args += ESCAPE_CHARS.keys()
    parsed_args = parse_args(args)

    myecho(parsed_args)

    captured = capsys.readouterr()
    assert "yeet" in captured.out
    for escape_char, escaped_char in ESCAPE_CHARS.items():
        assert escape_char in captured.out
        assert " " + escaped_char + " " not in captured.out
