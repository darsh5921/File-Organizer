from tkinter import *
import os
import sys


# from pathlib import path
cwd = f"[{os.getcwd()}]"
root = Tk()
root.geometry('450x415')
root.title('File Organizer')
root.minsize(450, 415)
root.maxsize(450, 415)
root['bg'] = 'sky blue'
frame = Frame(root ,relief=SUNKEN,bg="sky blue")
frame.pack(side=BOTTOM)

#for getting assets from temp folder
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

root.wm_iconbitmap(resource_path("icon.ico"))

label1 = Label(root, text="Put this Application inside a Folder",font=("SegoeUI",9),bg="light cyan",fg="Black").pack(pady=4)
label1 = Label(root, text="To organize file types into Folders Automatically",font=("SegoeUI",9),bg="light cyan",fg="Black").pack(pady=2)
label2=Label(root,text="Current Folder "+cwd,bg="light cyan",fg="Black",font=("SegoeUI",9)).pack(side=TOP,pady=5)
label3 = Label(root,text="Click To Organize Files",bg="Sky Blue",fg="blue",font=("Times new roman",13,"bold")).pack(side=TOP,pady=8)



def allfiles():
    import os
    from pathlib import Path
    DIRECTORIES = {
    "HTML": [".html5", ".html", ".htm", ".xhtml"],

    "IMAGES": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", ".svg",
               ".heif", ".psd",".webp",".ico"],

    "VIDEOS": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng",
               ".qt", ".mpg", ".3gp", ".m4v", ".mkv",".mpeg",".rm", ".swf"],

    "DOCUMENTS": [".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf", ".ods",
                  ".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox",
                  ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt",
                  ".pptx"],

    "ARCHIVES": [".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z",
                 ".dmg", ".rar", ".xar", ".zip"],

    "AUDIO": [".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3",
              ".msv", ".ogg", ".oga", ".raw", ".vox", ".wav", ".wma"],

    "PLAINTEXT": [".txt", ".in", ".out",".md"],

    "PDF": [".pdf"],
    "PYTHON": [".py",".pyc"],
    "C++":[".cpp"],
    "Java":[".java"],
    "XML": [".xml"],
    "EXE": [".exe",".msi"],
    "SHELL": [".sh"]}

    EXCLUDE_FILE_NAME = "File Organizer.exe"

    FILE_FORMATS = {file_format: directory
                for directory, file_formats in DIRECTORIES.items()
                for file_format in file_formats}
    def organize_junk():
        for entry in os.scandir():
            if entry.is_dir():
                continue
            file_path = Path(entry)
            file_format = file_path.suffix.lower()
            file_name = file_path.name

            if file_name.lower() == EXCLUDE_FILE_NAME.lower():
                continue

            if file_format in FILE_FORMATS:
                directory_path = Path(FILE_FORMATS[file_format])
                directory_path.mkdir(exist_ok=True)
                file_path.rename(directory_path.joinpath(file_path))
            for dir in os.scandir():
                try:
                    os.rmdir(dir)
                except:
                    pass
    if __name__ == "__main__":
        organize_junk()
def onlydoc():
    import os
    from pathlib import Path
    DIRECTORIES = {
    "DOCUMENTS": [".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf", ".ods",
                  ".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox",
                  ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt",
                  "pptx",".txt",".pdf",".xml"] }

    EXCLUDE_FILE_NAME = "File Organizer.exe"

    FILE_FORMATS = {file_format: directory
                for directory, file_formats in DIRECTORIES.items()
                for file_format in file_formats}
    def organize_junk():
        for entry in os.scandir():
            if entry.is_dir():
                continue
            file_path = Path(entry)
            file_format = file_path.suffix.lower()
            file_name = file_path.name

            if file_name.lower() == EXCLUDE_FILE_NAME.lower():
                continue

            if file_format in FILE_FORMATS:
                directory_path = Path(FILE_FORMATS[file_format])
                directory_path.mkdir(exist_ok=True)
                file_path.rename(directory_path.joinpath(file_path))

            for dir in os.scandir():
                try:
                    os.rmdir(dir)
                except:
                    pass
    if __name__ == '__main__':
        organize_junk()
def onlyimages():
    import os
    from pathlib import Path
    DIRECTORIES = {
    "IMAGES": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", ".svg",
               ".heif",".heic", ".psd",".webp",".raw",".ico"]}

    EXCLUDE_FILE_NAME = "File Organizer.exe"

    FILE_FORMATS = {file_format: directory
                for directory, file_formats in DIRECTORIES.items()
                for file_format in file_formats}
    def organize_junk():
        for entry in os.scandir():
            if entry.is_dir():
                continue
            file_path = Path(entry)
            file_format = file_path.suffix.lower()

            file_name = file_path.name

            if file_name.lower() == EXCLUDE_FILE_NAME.lower():
                continue


            if file_format in FILE_FORMATS:
                directory_path = Path(FILE_FORMATS[file_format])
                directory_path.mkdir(exist_ok=True)
                file_path.rename(directory_path.joinpath(file_path))
            for dir in os.scandir():
                try:
                    os.rmdir(dir)
                except:
                    pass
    if __name__ == '__main__':
        organize_junk()
def onlyvideos():
    import os
    from pathlib import Path
    DIRECTORIES = {
    "VIDEOS": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng",
               ".qt", ".mpg", ".3gp", ".m4v", ".mkv",".mpeg",".rm", ".swf"]}

    EXCLUDE_FILE_NAME = "File Organizer.exe"

    FILE_FORMATS = {file_format: directory
                for directory, file_formats in DIRECTORIES.items()
                for file_format in file_formats}
    def organize_junk():
        for entry in os.scandir():
            if entry.is_dir():
                continue
            file_path = Path(entry)
            file_format = file_path.suffix.lower()

            file_name = file_path.name

            if file_name.lower() == EXCLUDE_FILE_NAME.lower():
                continue


            if file_format in FILE_FORMATS:
                directory_path = Path(FILE_FORMATS[file_format])
                directory_path.mkdir(exist_ok=True)
                file_path.rename(directory_path.joinpath(file_path))
            for dir in os.scandir():
                try:
                    os.rmdir(dir)
                except:
                    pass
    if __name__ == '__main__':
        organize_junk()
def onlyaudios():
    import os
    from pathlib import Path
    DIRECTORIES = {
    "AUDIO": [".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3",
              ".msv", ".ogg", ".oga", ".raw", ".vox", ".wav", ".wma",".aiff", ".amr", ".flac", ".opus"]
              }
    EXCLUDE_FILE_NAME = "File Organizer.exe"

    FILE_FORMATS = {file_format: directory
                for directory, file_formats in DIRECTORIES.items()
                for file_format in file_formats}
    def organize_junk():
        for entry in os.scandir():
            if entry.is_dir():
                continue
            file_path = Path(entry)
            file_format = file_path.suffix.lower()

            file_name = file_path.name

            if file_name.lower() == EXCLUDE_FILE_NAME.lower():
                continue

            if file_format in FILE_FORMATS:
                directory_path = Path(FILE_FORMATS[file_format])
                directory_path.mkdir(exist_ok=True)
                file_path.rename(directory_path.joinpath(file_path))
            for dir in os.scandir():
                try:
                    os.rmdir(dir)
                except:
                    pass
    if __name__ == '__main__':
        organize_junk()
b6 = Button(frame, fg='Black', text='          Exit         ', pady=6, padx=45, font=('SegoeUI 10 bold'),bg="Light grey", command=root.quit).pack(side=BOTTOM,pady=8)
b1 = Button(frame, fg='Black', text='      All Files      ',pady=6, padx=45, font=('SegoeUI 10 bold'),bg="white", command=allfiles).pack(side=BOTTOM,pady=3)
b3 = Button(frame, fg='Black', text='  Only Images   ',pady=6, padx=45, font=('SegoeUI 10 bold'),bg="white",command=onlyimages).pack(side=BOTTOM,pady=3)
b2 = Button(frame, fg='Black', text='Only Documents',pady=6, padx=44, font=('SegoeUI 10 bold'),bg="white",command=onlydoc).pack(side=BOTTOM,pady=3)
b4 = Button(frame, fg='Black', text='   Only Videos   ',pady=6, padx=45, font=('SegoeUI 10 bold'),bg="white", command=onlyvideos).pack(side=BOTTOM,pady=3)
b5 = Button(frame, fg='Black', text='    Only Audio    ',pady=6, padx=45, font=('SegoeUI 10 bold'),bg="white", command=onlyaudios).pack(side=BOTTOM,pady=3)

root.mainloop()