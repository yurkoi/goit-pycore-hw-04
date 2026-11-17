from pathlib import Path


def get_cats_info(path):
    cats = []

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                cat_id, name, age = line.split(",")
                cats.append({"id": cat_id, "name": name, "age": age})
    except FileNotFoundError:
        print(f"Файл {path} не знайдено")
        return []
    except OSError:
        print(f"Не вдалося прочитати файл {path}")
        return []
    except ValueError:
        print(f"Файл {path} пошкоджений")
        return []

    return cats


if __name__ == "__main__":
    cats_info = get_cats_info(Path(__file__).parent / "cats_file.txt")
    print(cats_info)
