# Python Automated File Organizer

A Python automation tool that scans a folder and automatically organizes files into categorized subfolders based on their file extensions.

## Features

- Automatically categorizes files
- Creates folders when needed
- Supports images, documents, videos, audio, archives, spreadsheets, and more
- Prevents filename conflicts
- Handles unknown file types using an "Others" category
- Uses Python's built-in `os` and `shutil` libraries

## Technologies

- Python
- os
- shutil
- File System Automation

## How It Works

The script scans the specified directory, identifies each file's extension, determines the appropriate category, creates the corresponding folder, and moves the file into that folder.

### Example

Before:

    Downloads/
    ├── photo.jpg
    ├── resume.pdf
    ├── video.mp4
    ├── music.mp3
    └── project.zip

After:

    Downloads/
    ├── Images/
    │   └── photo.jpg
    ├── Documents/
    │   └── resume.pdf
    ├── Videos/
    │   └── video.mp4
    ├── Audio/
    │   └── music.mp3
    └── Archives/
        └── project.zip

## Skills Demonstrated

- Python programming
- File and directory manipulation
- Automation
- Functions
- Dictionaries
- Loops and conditional logic
- Error handling
- Working with the Python standard library


## 🔄 Undo / Recovery Utility

The project includes `undo_file_organizer.py`, a recovery utility designed to reverse the file organization performed by `file_organizer.py`.

### What it does

The undo script:

* Scans the category folders created by the organizer
* Moves organized files back to the original `Downloads` folder
* Helps restore files without manually moving them one by one
* Prevents accidental filename overwrites by creating a unique filename when necessary

### Usage

Run the following command from the project folder:

```bash
python undo_file_organizer.py
```

The script will display the number of files successfully restored.

### Example

```text
Undo completed!
Files restored: 168
```

### ⚠️ Important

The undo utility is intended to reverse file organization performed by this project. Always review the target folder and understand what files will be moved before running automation scripts that modify your filesystem.
