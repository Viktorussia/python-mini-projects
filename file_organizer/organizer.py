from pathlib import Path
import shutil

CATEGORIES = {
    "Images": {".jpg", ".jpeg", ".png", ".gif", ".webp", ".bmp"},
    "Documents": {".pdf", ".doc", ".docx", ".txt", ".rtf", ".xlsx", ".pptx"},
    "Archives": {".zip", ".rar", ".7z", ".tar", ".gz"},
    "Audio": {".mp3", ".wav", ".flac", ".aac", ".ogg"},
    "Video": {".mp4", ".mkv", ".avi", ".mov", ".webm"},
}

def category_for(ext: str) -> str:
    ext = ext.lower()
    for name, exts in CATEGORIES.items():
        if ext in exts:
            return name
    return "Other"
def organize(folder: Path) -> None:
    if not folder.exists() or not folder.is_dir():
        print("Папка не найдена:", folder)
        return
    
    for item in folder.iterdir():
        if item.is_file():
            cat = category_for(item.suffix)
            target_dir = folder / cat
            target_dir.mkdir(exist_ok=True)

            target_path = target_dir / item.name
            if target_path.exists():
              stem = item.stem
              suffix = item.suffix
              i = 1
              while (target_dir / f"{stem}_{i}{suffix}").exists():
                  i += 1
              target_path = target_dir /  f"{stem}_{i}{suffix}"

            shutil.move(str(item), str(target_path))

    print("Готово. Файлы отсортированы в:", folder)

if __name__ == "__main__":
    path_str = input("Введите путь к папке (например D:\\\\Downloads): ").strip().strip('"')
    organize(Path(path_str))    