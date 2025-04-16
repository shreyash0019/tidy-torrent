# Tidy Torrent

A simple Python script to automatically organize your Downloads folder into categorized subfolders based on file extensions.

---

## 📁 Features
- Automatically detects and sorts files by extension
- Organizes files into folders like `images`, `videos`, `documents`, `programs`, and more
- Handles unknown extensions by moving them to an `others` folder
- Easy to customize and extend

---

## 🛠️ Setup & Usage

### 1. Clone the Repository
```bash
git clone https://github.com/shreyash0019/tidy-torrent.git
cd tidy-torrent
```

### 2. Edit the Script (Optional)
Update the Downloads folder path in the script if yours is different:
```python
os.chdir("E:/downloads")
```

### 3. Create Destination Folders
Make sure the following directory exists relative to your Downloads folder:
```
../download-sorting/
```
Inside it, you can manually create subfolders (e.g. `images`, `videos`, `others`, etc.) or enhance the script to auto-create them.

### 4. Run the Script
```bash
python tidy_torrent.py
```

---

## 🧩 Extension Categories
The script currently supports:
- **Images**: `.jpg`, `.png`, `.jpeg`, `.gif`
- **Videos**: `.mp4`, `.mkv`
- **Music**: `.mp3`, `.wav`
- **Archives**: `.zip`, `.tgz`, `.rar`, `.tar`
- **Documents**: `.pdf`, `.docx`, `.csv`, `.xlsx`, `.pptx`, `.doc`, `.ppt`, `.xls`
- **Setup**: `.msi`, `.exe`
- **Programs**: `.py`, `.c`, `.cpp`, `.php`
- **Design**: `.xd`, `.psd`
- **Others**: everything else

You can modify or expand these in the `extensions` dictionary.

---

##  Contributing 🤍🤝
Pull requests are welcome! If you have suggestions for improvements or want to support more file types, feel free to contribute.

---



## 🙌 Author
Made with 💻 by [Shreyash](https://github.com/shreyash0019)

---

