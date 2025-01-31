import os
import shutil
from pathlib import Path

def sort_files_by_extension(source_dir: Path, dest_dir: Path):
    try:
        if not source_dir.exists() or not source_dir.is_dir():
            print("Вказана вихідна директорія не існує або не є папкою.")
            print("Копіювання та сортування неможливо!")
            return

        dest_dir.mkdir(exist_ok=True)
        
        for item in source_dir.rglob("*"):
            if item.is_file():
                ext = item.suffix.lstrip(".") or "no_extension"
                target_folder = dest_dir / ext
                target_folder.mkdir(exist_ok=True)
                shutil.copy2(item, target_folder / item.name)
        
        print("Копіювання та сортування завершено!")
    except Exception as e:
        print(f"Сталася помилка: {e}")
        print("Копіювання та сортування неможливо!")

if __name__ == "__main__":
    src_input = input("Введіть шлях до вихідної директорії: ").strip()
    dest_input = input("Введіть шлях до директорії призначення (Enter для dist): ").strip()
    
    src_path = Path(src_input)
    #Якщо шлях не вказано, то створюємо папку на рівні вихідної директорії
    dest_path = Path(dest_input) if dest_input else src_path.parent / "dist"
    
    sort_files_by_extension(src_path, dest_path)
