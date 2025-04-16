import os
import shutil

# Set the working directory to your Downloads folder
os.chdir("E:/downloads")  # Use raw string or forward slashes

# Get list of all files in the directory
files = os.listdir()

# Define categories and associated extensions
extensions = {
    "images": [".jpg", ".png", ".jpeg", ".gif"],
    "videos": [".mp4", ".mkv"],
    "musics": [".mp3", ".wav"],
    "zip": [".zip", ".tgz", ".rar", ".tar"],
    "documents": [".pdf", ".docx", ".csv", ".xlsx", ".pptx", ".doc", ".ppt", ".xls"],
    "setup": [".msi", ".exe"],
    "programs": [".py", ".c", ".cpp", ".php", ".C", ".CPP"],
    "design": [".xd", ".psd"]
}

# Function to return folder name based on file extension
def sorting(file):
    for key, exts in extensions.items():
        for ext in exts:
            if file.endswith(ext):
                return key
    return None

# Sort each file into its category
for file in files:
    category = sorting(file)
    dest_dir = f"../download-sorting/{category if category else 'others'}"
    
    try:
        shutil.move(file, dest_dir)
    except:
        print(f"{file} already exists or couldn't be moved.")
 
