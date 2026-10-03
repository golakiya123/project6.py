# 📔 Personal Journal Manager

> A simple and user-friendly **Python Personal Journal Manager** that
> lets you create, view, search, and delete journal entries using a text
> file.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Project](https://img.shields.io/badge/Project-Personal%20Journal%20Manager-green)
![File Storage](https://img.shields.io/badge/Storage-Text%20File-orange)

------------------------------------------------------------------------

## ✨ Project Overview

**Personal Journal Manager** is a beginner-friendly Python project
designed to manage personal journal entries from the terminal.

The program provides a simple menu where users can:

-   📝 Add a new journal entry
-   📖 View all saved entries
-   🔍 Search entries using a keyword or date
-   🗑️ Delete all journal entries
-   🚪 Exit the program safely

Journal entries are stored in a `journal.txt` file, making the project a
practical example of **file handling in Python**.

------------------------------------------------------------------------

## 🚀 Features

### 📝 1. Add a New Entry

Users can enter a journal message, and the program automatically adds
the current date and time before saving it to the journal file.

### 📖 2. View All Entries

Displays all previously saved journal entries. If the journal file does
not exist, the program handles the situation with a helpful message.

### 🔍 3. Search for an Entry

Users can search their journal using a **keyword or date**. The search
is case-insensitive.

### 🗑️ 4. Delete All Entries

Users can delete all saved journal entries after confirming the
operation.

### 🚪 5. Exit

Closes the program with a friendly goodbye message.

------------------------------------------------------------------------

## 🛠️ Technologies Used

-   🐍 **Python**
-   📁 **File Handling**
-   🕒 **datetime module**
-   💻 **Terminal / Command Line Interface**
-   🔎 **String Searching**
-   ⚠️ **Exception Handling**

------------------------------------------------------------------------

## 📚 Python Concepts Demonstrated

This project demonstrates several important Python concepts:

-   Variables
-   `if / elif / else`
-   `while` loops
-   User input
-   File handling with `open()`
-   Append and read file modes
-   `os.path.exists()`
-   `os.remove()`
-   `try / except`
-   `datetime.now()`
-   String methods such as `.lower()`
-   Basic input validation

------------------------------------------------------------------------

## 📂 Project Structure

``` text
Personal-Journal-Manager/
│
├── project6.py
├── journal.txt
├── README.md
├── screenshot-1.png
└── demo-video.mp4
```

> `journal.txt` is created/used by the program to store journal entries.

------------------------------------------------------------------------

## ▶️ How to Run

### 1️⃣ Clone the Repository

``` bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2️⃣ Open the Project Folder

``` bash
cd Personal-Journal-Manager
```

### 3️⃣ Run the Python Program

``` bash
python project6.py
```

------------------------------------------------------------------------

## 🖥️ Sample Menu

``` text
Welcome to personal journal manager!

please select an option:
1. Add a New Entyry
2. View All Entries
3. Search for an Entry
4. Delete all Entries
5. Exit

Enter Your Choice:
```

------------------------------------------------------------------------

## 📸 Screenshots

### Part 1 --- Project Execution

Add your own project screenshot here:

<img width="532" height="542" alt="screenshot9" src="https://github.com/user-attachments/assets/654c8a48-cb25-4484-8acb-19755741d943" />


### Part 2 --- Project Output

Add your own output screenshot here:

<img width="581" height="410" alt="screenshot10" src="https://github.com/user-attachments/assets/a7e0979f-0bdc-4900-aefd-02e35f3c5a19" />


------------------------------------------------------------------------

## 🎥 Project Demo Video

▶️ **Watch the project demonstration:**\
[![Project Demo
Video](https://img.shields.io/badge/▶️%20Watch-Demo%20Video-red)](YOUR_VIDEO_LINK_HERE)

> Replace `YOUR_VIDEO_LINK_HERE` with your YouTube, Google Drive, or
> other video link.

------------------------------------------------------------------------

## 💡 What I Learned

Through this project, I practiced how to:

-   Work with files in Python
-   Store and retrieve information
-   Handle missing files using exceptions
-   Search text efficiently
-   Work with dates and timestamps
-   Build a menu-driven command-line application
-   Handle invalid user choices
-   Organize a practical Python project for GitHub

------------------------------------------------------------------------

## 🎯 Future Improvements

Some possible improvements for future versions:

-   🔐 Add password protection
-   ✏️ Add an option to edit existing entries
-   📅 Add date-based filtering
-   🏷️ Add journal categories or tags
-   🎨 Create a graphical user interface
-   💾 Use a database instead of a text file

------------------------------------------------------------------------

## 👨‍💻 Author

**Vency**

This project was created as part of my Python learning and portfolio
development journey.

------------------------------------------------------------------------

## ⭐ Support

If you find this project useful or interesting, feel free to ⭐ **star
the repository** and explore the code!
