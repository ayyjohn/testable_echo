#! /usr/local/bin/python3

import argparse

ESCAPE_CHARS = {
    "\\a": "\a",
    "\\b": "\b",
    "\\f": "\f",
    "\\n": "\n",
    "\\r": "\r",
    "\\t": "\t",
    "\\\\": "\\",
}


def myecho():

    parser = argparse.ArgumentParser(
        prog="myecho",
        description="my implementation of echo. writes any number of operands separated by single blank space characters and followed by a newline to stdout",
    )
    parser.add_argument(
        "-n",
        action="store_true",
        help="do not print the trailing newline character",
    )
    parser.add_argument(
        "-e",
        action="store_true",
        help="interpret backslash-escaped characters (\\a \\b \\c \\E \\f \\n \\r \\t \\v \\\\)",
    )
    parser.add_argument(
        "-E",
        action="store_true",
        help="explicitly turn off the above backslash-escaped characters",
    )
    parser.add_argument(
        "ARGS",
        help="any number of other words",
        nargs="*"
    )

    args = parser.parse_args()
    print_end = "" if args.n else "\n"

    output = ""
    for arg in args.ARGS:
        if arg in ESCAPE_CHARS:
            output += ESCAPE_CHARS[arg] if args.e else arg
        else:
            output += arg
        output += " "

    print(output, end=print_end)


if __name__ == "__main__":
    myecho()