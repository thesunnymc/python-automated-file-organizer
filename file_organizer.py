import os
import shutil

# Folder to organize
SOURCE_FOLDER = r"C:\Users\YourName\Downloads"

# File categories and their extensions
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".rtf", ".odt"],
    "Spreadsheets": [".xls", ".xlsx", ".csv"],
    "Presentations": [".ppt", ".pptx"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv"],
    "Audio": [".mp3", ".wav", ".flac", ".aac", ".m4a"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Programs": [".exe", ".msi", ".apk"],
}


def get_category(file_extension):
    """Return the category for a given file extension."""

    for category, extensions in FILE_CATEGORIES.items():
        if file_extension.lower() in extensions:
            return category

    return "Others"


def get_unique_filename(destination_folder, filename):
    """Prevent overwriting an existing file."""

    base_name, extension = os.path.splitext(filename)
    counter = 1

    new_filename = filename

    while os.path.exists(os.path.join(destination_folder, new_filename)):
        new_filename = f"{base_name}_{counter}{extension}"
        counter += 1

    return new_filename


def organize_files():
    """Scan the folder and organize files into categories."""

    if not os.path.exists(SOURCE_FOLDER):
        print(f"Error: Folder does not exist:\n{SOURCE_FOLDER}")
        return

    moved_files = 0

    for filename in os.listdir(SOURCE_FOLDER):

        file_path = os.path.join(SOURCE_FOLDER, filename)

        # Skip folders
        if not os.path.isfile(file_path):
            continue

        # Get file extension
        _, extension = os.path.splitext(filename)

        # Determine category
        category = get_category(extension)

        # Create category folder if it doesn't exist
        category_folder = os.path.join(SOURCE_FOLDER, category)
        os.makedirs(category_folder, exist_ok=True)

        # Prevent duplicate filenames
        unique_filename = get_unique_filename(
            category_folder,
            filename
        )

        destination_path = os.path.join(
            category_folder,
            unique_filename
        )

        # Move the file
        shutil.move(file_path, destination_path)

        print(f"Moved: {filename} → {category}/")

        moved_files += 1

    print("\n--------------------------------")
    print("File organization completed!")
    print(f"Files moved: {moved_files}")
    print("--------------------------------")


if __name__ == "__main__":
    organize_files()