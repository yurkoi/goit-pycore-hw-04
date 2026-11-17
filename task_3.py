import sys
from pathlib import Path

from colorama import Fore, init


def show_directory(path, prefix=" "):
    try:
        items = sorted(path.iterdir())
    except PermissionError:
        print(prefix + "┗ " + Fore.RED + "немає доступу")
        return

    for index, item in enumerate(items):
        is_last = index == len(items) - 1
        connector = "┗ " if is_last else "┣ "

        if item.is_dir():
            print(prefix + connector + Fore.BLUE + "📂" + item.name)
            show_directory(item, prefix + ("  " if is_last else "┃ "))
        else:
            print(prefix + connector + Fore.GREEN + "📜" + item.name)


def main():
    init(autoreset=True)

    if len(sys.argv) != 2:
        print(Fore.RED + "Використання: python task_3.py /шлях/до/директорії")
        sys.exit(1)

    path = Path(sys.argv[1])

    if not path.exists():
        print(Fore.RED + f"Шлях {path} не існує")
        sys.exit(1)

    if not path.is_dir():
        print(Fore.RED + f"{path} не є директорією")
        sys.exit(1)

    print(Fore.YELLOW + "📦" + path.resolve().name)
    show_directory(path)


if __name__ == "__main__":
    main()
