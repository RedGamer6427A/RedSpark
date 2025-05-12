import colorama

from collections.abc import Callable
from typing import Callable, TypeVar


colorama.init(autoreset=True)


def message(msg: str):
    print(colorama.Fore.BLUE +
          msg
          .replace("%l", colorama.Fore.LIGHTBLUE_EX)
          .replace("%n", colorama.Fore.BLUE)
    )


def forbidden(msg: str):
    print(colorama.Fore.RED +
          msg
          .replace("%l", colorama.Fore.LIGHTRED_EX)
          .replace("%n", colorama.Fore.RED)
    )


def str_input(msg: str) -> str:
    return input(
        colorama.Fore.YELLOW +
        msg
        .replace("%l", colorama.Fore.LIGHTYELLOW_EX)
        .replace("%n", colorama.Fore.YELLOW) + colorama.Fore.LIGHTYELLOW_EX + " > "
    )


def int_input(msg: str) -> int:
    a = str_input(msg)
    try:
        return int(a)
    except ValueError:

        forbidden(f"Please enter a whole number. %l\"{a}\"%n is not an integer. Examples: 0, 5, -20")
        return int_input(msg)


def float_input(msg: str) -> float:
    a = str_input(msg)
    try:
        return float(a)
    except ValueError:
        forbidden(f"Please provide a whole or decimal number. %l\"{a}\"%n is not a float. Examples: 4.2, -3.4, 6")
        return float_input(msg)


def bool_input(msg: str) -> bool:
    a = str_input(msg)
    if a.lower() in ["y", "true", "yes", "ye", "1", "1.0", "positive", "t"]:
        return True
    elif a.lower() in ["n", "false", "no", "nah", "0", "0.0", "negative", "f"]:
        return False
    else:
        forbidden("Please provide a boolean value. %l\"{a}\"%n is not a boolean value. Examples: true, n, yes, negative")
        return bool_input(msg)


R = TypeVar('R')

def confirmed_input(msg: str, function: Callable[[str], R]) -> R:
    a = function(msg)
    b = bool_input(f"You typed in: \"%l{a}%n\". Please confirm")
    if b:
        return a
    else:
        return confirmed_input(msg, function)
