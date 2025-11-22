# Data Redundancy System – CodeAlpha Internship (Task 1)

This project is my submission for **Task 1 of the CodeAlpha Cloud Internship**.  
The goal of this task is to create a simple **Data Redundancy System**.

Data Redundancy means storing **multiple copies of the same data** so that even if one copy is lost, the data is still safe.

---

What My Project Does

My Python program:
- Takes an original file  
- Creates **two extra copies**  
- Stores them safely  
- Shows how redundancy works  

This is a simple example showing how data can be backed up using redundant copies.

---

Files Included

data_redundancy_code.py  
This Python file creates two redundant copies of a selected file.

Task1_Data_Redundancy_System.zip  
A zipped folder containing the project code.

---

How It Works (Simple Explanation)

1. You choose a file (example: `Image1.jpg`).
2. The program makes:
   - `Image1_Copy1.jpg`
   - `Image1_Copy2.jpg`
3. Now you have **3 total copies**, which prevents data loss.

---

Code Used (Python)

```python
import shutil

# Original file name
original = "Image1.jpg"

# Creating two extra copies
shutil.copy(original, "Image1_Copy1.jpg")
shutil.copy(original, "Image1_Copy2.jpg")

print("Redundant copies created successfully!")
