import shutil

# Original file name
original = "Image1.jpg"

# Creating two extra copies
shutil.copy(original, "Image1_Copy1.jpg")
shutil.copy(original, "Image1_Copy2.jpg")

print("Redundant copies created successfully!")
