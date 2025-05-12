import colorama

import cli

colorama.init(autoreset=True)


for color in cli.Colors:
    cli.colored_message(f"This is a %l{color.name.capitalize()}%n message.", color)

cli.confirmed_input("Int pls", cli.int_input)