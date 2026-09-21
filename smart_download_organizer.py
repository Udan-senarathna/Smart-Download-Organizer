from pathlib import Path
import shutil

source = Path(
    input("Enter downloads folder: ").strip()
)

if not source.is_dir():
    print("Folder not found!")
    exit()

categories = {
    "Images": {".jpg", ".jpeg", ".png", ".gif"},
    "Documents": {".pdf", ".docx", ".txt", ".xlsx"},
    "Archives": {".zip", ".rar", ".7z"},
    "Videos": {".mp4", ".mkv", ".avi"},
}

moved = 0

print("\n" + "=" * 55)
print("          SMART DOWNLOAD ORGANIZER")
print("=" * 55)

for file in source.iterdir():

    if not file.is_file():
        continue

    category = next(
        (
            name
            for name, extensions in categories.items()
            if file.suffix.lower() in extensions
        ),
        "Others"
    )

    folder = source / category
    folder.mkdir(exist_ok=True)

    destination = folder / file.name

    if destination.exists():
        print(f"Skipped: {file.name}")
        continue

    shutil.move(str(file), str(destination))

    print(f"{file.name} -> {category}/")
    moved += 1

print("\n" + "-" * 55)
print(f"✓ {moved} files organized successfully!")
print("=" * 55)