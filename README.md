# 📂 Smart File Organizer

## Python Programming Task 08 – File Organizer & Data Management System

### 📌 Project Overview

The **Smart File Organizer** is a Python-based automation application developed as part of the **White Band Associates Python Internship (Task 08)**. The application automatically organizes files into different folders based on their file extensions, making file management faster, cleaner, and more efficient.

This project demonstrates practical concepts of **Python programming, Object-Oriented Programming (OOP), file handling, directory management, exception handling, automation, and report generation**.

---

# 🎯 Objective

The objective of this project is to develop a real-world automation tool that:

* Organizes files automatically.
* Classifies files into categories.
* Generates reports.
* Searches files efficiently.
* Detects duplicate files.
* Demonstrates practical Python programming skills.

---

# ✨ Features

## Required Features

* Select any folder from the computer.
* Validate the directory path.
* Scan all files in the selected folder.
* Display total number of files.
* Display file names and extensions.
* Automatically create folders:

  * Images
  * Documents
  * Videos
  * Audio
  * Archives
  * Programs
  * Others
* Move files into appropriate folders.
* Generate file statistics.
* Search files by filename.
* Search files by extension.
* Detect duplicate file names.
* Generate a detailed text report.
* Handle all common exceptions gracefully.

---

# 🌟 Bonus Features

* Progress Bar while organizing files
* CSV Report Export
* Largest File Finder
* Recently Modified Files
* Empty Folder Detection
* Delete Empty Folders

---

# 🛠 Technologies Used

* Python 3.x
* Object-Oriented Programming (OOP)
* os Module
* shutil Module
* csv Module
* datetime Module
* collections Module
* Exception Handling

---

# 📁 Project Structure

```
Python_Task_08_Priya/
│
├── smart_file_organizer.py
├── README.md
├── Project_Report.pdf
├── Screenshots/
└── Sample_Test_Folder/
|   ├── file_report.txt
|   ├── report.csv
```

---

# 📂 File Categories

| Category  | Extensions                                              |
| --------- | ------------------------------------------------------- |
| Images    | .jpg, .jpeg, .png, .gif, .bmp                           |
| Documents | .pdf, .doc, .docx, .txt, .ppt, .pptx, .xls, .xlsx, .csv |
| Videos    | .mp4, .avi, .mov, .mkv                                  |
| Audio     | .mp3, .wav, .aac, .ogg                                  |
| Archives  | .zip, .rar, .7z                                         |
| Programs  | .py, .java, .cpp, .c, .html, .css, .js                  |
| Others    | Unknown extensions                                      |

---

# ⚙️ Modules Implemented

## Module 1 – Directory Selection

* User enters folder path.
* Program validates whether the folder exists.
* Handles invalid paths.

---

## Module 2 – File Scanning

Displays:

* Total files
* File names
* File extensions

---

## Module 3 – Automatic File Organization

Creates folders automatically and moves files into their respective categories.

---

## Module 4 – File Statistics

Displays:

* Total files
* Images
* Documents
* Videos
* Audio
* Archives
* Programs
* Others

---

## Module 5 – Search Functionality

Supports searching files by:

* File name
* File extension

---

## Module 6 – Duplicate Detection

Detects duplicate filenames and displays their locations.

---

## Module 7 – Report Generation

Generates:

* `file_report.txt`
* `report.csv`

The report includes:

* Date and Time
* Folder Name
* Total Files
* Category-wise Count
* Duplicate Files
* Folder Structure

---

## Module 8 – Exception Handling

Handles:

* Invalid Folder
* Permission Denied
* Missing Folder
* File Already Exists
* Unexpected Errors


# 💻 Sample Menu

```
SMART FILE ORGANIZER

1. Scan Files
2. Organize Files
3. Statistics
4. Search by Name
5. Search by Extension
6. Duplicate Detection
7. Largest File
8. Recently Modified Files
9. Empty Folder Detection
10. Delete Empty Folders
11. Export CSV Report
12. Generate Text Report
13. Exit
```


# 📖 Learning Outcomes

Through this project, the following concepts were learned:

* Python Programming
* Object-Oriented Programming
* File Handling
* Directory Management
* Automation
* Exception Handling
* Report Generation
* CSV Handling
* Search Algorithms
* File Classification

---

# 🚧 Challenges Faced

* Categorizing multiple file types.
* Managing duplicate filenames.
* Handling file movement safely.
* Preventing program crashes using exception handling.
* Generating detailed reports automatically.
* Designing a reusable OOP-based architecture.

---

# 🚀 Future Improvements

* GUI using Tkinter or PyQt.
* Drag-and-drop folder selection.
* SHA-256 hash-based duplicate detection.
* Cloud storage integration.
* Automatic scheduled organization.
* File preview functionality.
* Multi-threaded file processing.
* Logging system.
* Undo last organization.
* Configuration file for custom categories.

---

# 📚 Internship Task

**White Band Associates**

**Python Programming Internship**

**Task 08 – Smart File Organizer**



If you found this project useful, consider giving the repository a ⭐ on GitHub.
