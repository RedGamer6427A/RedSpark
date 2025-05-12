import enum

import colorama

from typing import Callable, TypeVar


colorama.init(autoreset=True)


def hex_to_rgb(hex_color: int) -> tuple[int, int, int]:
    red   = (hex_color >> 16) & 0xFF
    green = (hex_color >> 8) & 0xFF
    blue  = hex_color & 0xFF
    return red, green, blue

def ansi_rgb(r: int, g: int, b: int) -> str:
    return f"\033[38;2;{r};{g};{b}m"

def ansi_hex(color: int) -> str:
    r, g, b = hex_to_rgb(color)
    return ansi_rgb(r, g , b)


class Colors(enum.Enum):
    RED = "red"
    GREEN = "green"
    BLUE = "blue"
    YELLOW = "yellow"
    CYAN = "cyan"
    PURPLE = "purple"
    WHITE = "white"
    BLACK = "black"
    ORANGE = "orange"
    PINK = "pink"
    BROWN = "brown"
    GRAY = "gray"
    LIGHT_GRAY = "light_gray"
    NAVY = "navy"
    LIME = "lime"
    GOLD = "gold"
    INDIGO = "indigo"
    SKY_BLUE = "sky_blue"
    SALMON = "salmon"
    TURQUOISE = "turquoise"
    VIOLET = "violet"
    BEIGE = "beige"
    TEAL = "teal"

color_map = {
    Colors.RED: (colorama.Fore.LIGHTRED_EX, colorama.Fore.RED),
    Colors.GREEN: (colorama.Fore.LIGHTGREEN_EX, colorama.Fore.GREEN),
    Colors.BLUE: (colorama.Fore.LIGHTBLUE_EX, colorama.Fore.BLUE),
    Colors.YELLOW: (colorama.Fore.LIGHTYELLOW_EX, colorama.Fore.YELLOW),
    Colors.CYAN: (colorama.Fore.LIGHTCYAN_EX, colorama.Fore.CYAN),
    Colors.PURPLE: (colorama.Fore.LIGHTMAGENTA_EX, colorama.Fore.MAGENTA),
    Colors.WHITE: (colorama.Fore.LIGHTWHITE_EX, colorama.Fore.WHITE),
    Colors.BLACK: (colorama.Fore.LIGHTBLACK_EX, colorama.Fore.BLACK),
    Colors.ORANGE: (ansi_hex(0xEA9138), ansi_hex(0xFF7014)),
    Colors.PINK: (ansi_hex(0xFEC5E5), ansi_hex(0xF699CD)),
    Colors.BROWN: (ansi_hex(0xA0522D), ansi_hex(0x8B4513)),
    Colors.GRAY: (ansi_hex(0x808080), ansi_hex(0x505050)),
    Colors.LIGHT_GRAY: (ansi_hex(0xD3D3D3), ansi_hex(0xA9A9A9)),
    Colors.NAVY: (ansi_hex(0x000080), ansi_hex(0x000055)),
    Colors.TEAL: (ansi_hex(0x008080), ansi_hex(0x005F5F)),
    Colors.LIME: (ansi_hex(0xBFFF00), ansi_hex(0x7FFF00)),
    Colors.GOLD: (ansi_hex(0xFFD700), ansi_hex(0xFFC300)),
    Colors.SKY_BLUE: (ansi_hex(0x87CEFA), ansi_hex(0x4682B4)),
    Colors.SALMON: (ansi_hex(0xFFA07A), ansi_hex(0xFA8072)),
    Colors.TURQUOISE: (ansi_hex(0xAFEEEE), ansi_hex(0x40E0D0)),
    Colors.VIOLET: (ansi_hex(0xEE82EE), ansi_hex(0x9400D3)),
    Colors.BEIGE: (ansi_hex(0xF5F5DC), ansi_hex(0xDEB887)),
}


def colored_message(msg: str, color: Colors) -> None:
    light_color, normal_color = color_map.get(color, (colorama.Fore.RESET, colorama.Fore.RESET))
    print(normal_color + msg.replace("%l", light_color).replace("%n", normal_color))

def message(msg: str) -> None:
    colored_message(msg, Colors.BLUE)

def forbidden(msg: str) -> None:
    colored_message(msg, Colors.RED)

def warning(msg: str) -> None:
    colored_message(msg, Colors.YELLOW)


def str_input(msg: str) -> str:
    return input(
        colorama.Fore.GREEN +
        msg
        .replace("%l", colorama.Fore.LIGHTGREEN_EX)
        .replace("%n", colorama.Fore.GREEN) + colorama.Fore.LIGHTGREEN_EX + " > "
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
    if a.lower() in ["y", "true", "yes", "ye", "1", "1.0", "positive", "t", "sure", "fine", "absolutely"]:
        return True
    elif a.lower() in ["n", "false", "no", "nah", "0", "0.0", "negative", "f", "never", "nope","absolutely not"]:
        return False
    else:
        forbidden(f"Please provide a boolean value. %l\"{a}\"%n is not a boolean value. Examples: true, n, yes, negative")
        return bool_input(msg)


R = TypeVar('R')

def confirmed_input(msg: str, function: Callable[[str], R]) -> R:
    a = function(msg)
    b = bool_input(f"You typed in: \"%l{a}%n\". Please confirm")
    if b:
        return a
    else:
        colored_message("Retrying%l...", Colors.GREEN)
        return confirmed_input(msg, function)

