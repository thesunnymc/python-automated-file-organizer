import os
import shutil

DOWNLOADS_FOLDER = r"C:\Users\rinaa\Downloads"

CATEGORIES = [
    "Images",
    "Documents",
    "Spreadsheets",
    "Presentations",
    "Videos",
    "Audio",
    "Archives",
    "Programs",
    "Others"
]


def get_unique_filename(folder, filename):
    """Prevent overwriting an existing file."""

    base_name, extension = os.path.splitext(filename)
    counter = 1
    new_filename = filename

    while os.path.exists(os.path.join(folder, new_filename)):
        new_filename = f"{base_name}_{counter}{extension}"
        counter += 1

    return new_filename


def undo_organization():
    moved_files = 0

    for category in CATEGORIES:

        category_folder = os.path.join(
            DOWNLOADS_FOLDER,
            category
        )

        if not os.path.exists(category_folder):
            continue

        for filename in os.listdir(category_folder):

            source_path = os.path.join(
                category_folder,
                filename
            )

            # Only move files, not folders
            if not os.path.isfile(source_path):
                continue

            unique_filename = get_unique_filename(
                DOWNLOADS_FOLDER,
                filename
            )

            destination_path = os.path.join(
                DOWNLOADS_FOLDER,
                unique_filename
            )

            shutil.move(
                source_path,
                destination_path
            )

            print(f"Restored: {filename}")

            moved_files += 1

    print("\n--------------------------------")
    print("Undo completed!")
    print(f"Files restored: {moved_files}")
    print("--------------------------------")


if __name__ == "__main__":
    undo_organization()