import argparse
import shutil
from pathlib import Path
import sys

def parse_arguments():
    """
    Парсинг аргументів командного рядка.
    """
    parser = argparse.ArgumentParser(description="Рекурсивне копіювання та сортування файлів за розширенням.")
    parser.add_argument("source", type=str, help="Шлях до вихідної директорії")
    parser.add_argument("output", type=str, nargs="?", default="dist", help="Шлях до директорії призначення (за замовчуванням: dist)")
    return parser.parse_args()

def copy_file(file_path: Path, output_root: Path):
    """
    Копіює файл у відповідну підпапку на основі його розширення.
    """
    try:
        # Отримуємо розширення файлу (без крапки). Якщо розширення немає -> 'no_extension'
        extension = file_path.suffix[1:] if file_path.suffix else "no_extension"
        
        # Формуємо шлях до цільової папки (наприклад: dist/txt)
        target_dir = output_root / extension
        
        # Створюємо папку, якщо вона не існує
        target_dir.mkdir(parents=True, exist_ok=True)
        
        # Формуємо кінцевий шлях файлу
        destination_file = target_dir / file_path.name
        
        # Копіюємо файл (copy2 зберігає метадані файлу, наприклад, час створення)
        shutil.copy2(file_path, destination_file)
        print(f"[OK] Скопійовано: {file_path} -> {destination_file}")

    except PermissionError:
        print(f"[Error] Немає прав доступу для копіювання файлу: {file_path}")
    except OSError as e:
        print(f"[Error] Помилка ОС при копіюванні {file_path}: {e}")
    except Exception as e:
        print(f"[Error] Невідома помилка з файлом {file_path}: {e}")

def read_folder_recursively(source_path: Path, output_root: Path):
    """
    Рекурсивно проходить по всіх елементах директорії.
    """
    try:
        # Перевіряємо, чи існує вихідна папка
        if not source_path.exists():
            print(f"[Error] Вихідна директорія не знайдена: {source_path}")
            return

        # Ітеруємося по всіх об'єктах у директорії
        for item in source_path.iterdir():
            if item.is_dir():
                # Рекурсивний виклик для підпапки
                read_folder_recursively(item, output_root)
            elif item.is_file():
                # Обробка файлу
                copy_file(item, output_root)

    except PermissionError:
        print(f"[Error] Немає прав доступу до директорії: {source_path}")
    except OSError as e:
        print(f"[Error] Помилка доступу до файлової системи: {e}")

def main():
    args = parse_arguments()
    
    source_path = Path(args.source)
    output_path = Path(args.output)

    print(f"Початок роботи...")
    print(f"Звідки: {source_path}")
    print(f"Куди: {output_path}")
    print("-" * 40)

    read_folder_recursively(source_path, output_path)
    
    print("-" * 40)
    print("Роботу завершено.")

if __name__ == "__main__":
    main()