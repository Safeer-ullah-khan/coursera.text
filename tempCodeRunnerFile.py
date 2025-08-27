import os
# import shutil

# Folder_path = r"C:\Users\HP\Desktop\AI"

# File_Types = {
#     "Images": [".png", ".jpeg", ".jpg"],
#     "Documents": [".pdf", ".ppt", ".docx", ".txt"],
#     "Videos": [".mkv", ".mp4", ".avi"]
# }

# for filename in os.listdir(Folder_path):
#     File_path = os.path.join(Folder_path, filename)

#     # Skip folders
#     if os.path.isdir(File_path):
#         continue

#     # Get file extension
#     _, ext = os.path.splitext(filename)
#     ext = ext.lower()

#     moved = False
#     for category, extensions in File_Types.items():
#         if ext in extensions:
#             category_folder = os.path.join(Folder_path, category)
#             os.makedirs(category_folder, exist_ok=True)
#             shutil.move(File_path, os.path.join(category_folder, filename))
#             print(f"Moved {filename} --> {category}")
#             moved = True
#             break

#     if not moved:
#         other_folder = os.path.join(Folder_path, "Others")
#         os.makedirs(other_folder, exist_ok=True)
#         shutil.move(File_path, os.path.join(other_folder, filename))
#         print(f"Moved {filename} --> Others/")