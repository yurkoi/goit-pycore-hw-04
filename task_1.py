from pathlib import Path


def total_salary(path):
    total = 0
    count = 0

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                _, salary = line.split(",")
                total += int(salary)
                count += 1
    except FileNotFoundError:
        print(f"Файл {path} не знайдено")
        return 0, 0
    except ValueError:
        print(f"Файл {path} пошкоджений")
        return 0, 0

    if count == 0:
        return 0, 0

    average = total / count
    return total, average


total, average = total_salary(Path(__file__).parent / "salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
