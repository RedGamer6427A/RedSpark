import os
import random
import time
from time import sleep
import redspark.terminal.logger as logger
import redspark.processing.string
from redspark.terminal import cli
from redspark.terminal.cli import forbidden
from redspark.timing import performance


def clear_logs_folder():
    folder = "logs"
    if not os.path.exists(folder):
        print(f"'{folder}' folder does not exist.")
        return
    counter = 0
    for filename in os.listdir(folder):
        counter+=1
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
        except Exception as e:
            print(f"Failed to delete {file_path}: {e}")
    cli.message(f"Removed %l{counter}%n files.")

def summon_demon():
    name = cli.str_input("What is your name?")
    forbidden(f"Hello {name}")

    forbidden("BYE ! !!!  !  ! ")

def run_everything():
    for color in cli.Colors:
        cli.colored_message(f"This is a %l{color.name.capitalize()}%n message.", color)

    logger.init("TESTY")

    time.sleep(1)

    def e():
        for i in range(10):
            logger.debug("*Not aggressively excited* HI THERE!")
            logger.info("*Not aggressively excited* ITS ME KABOOOSH!")
            logger.warn(f"*Not aggressively excited* NUMBER: ohohohoohohohohooh {i}")
            logger.error("*Not aggressively excited* OH DEAR THAT WAS EVERYTHING I WANTED TO SAY!!!!!!!!!!!")
            logger.critical(
                "*Not aggressively excited* OK IMMA SAY A VERY GOOD BYE... VERY GOOD BYE!!!!!!!!!!! HAVE FUN :D")
            time.sleep(1)

    a = performance.measure_performance(e)

    time.sleep(1)

    import subprocess

    # Path to the Python file
    file_path = logger.REENACT_FILE

    # Run the Python script
    d = lambda: subprocess.run(['python', file_path])

    b = performance.measure_performance(d)

    cli.message(f"Comparison - LIVE: {a}, RECORD: {b}")
    sleep(1)
    cli.message("Mes%lsa%nge")
    cli.warning("Wa%lrn%ning")
    cli.forbidden("For%lbi%nden")


if __name__ == "__main__":
    options = {
        "Clear Logs Folder": clear_logs_folder,
        "Summon a demon": summon_demon,
        "Run Everything": run_everything
    }
    cli.menu_selector("Select what to do", options)