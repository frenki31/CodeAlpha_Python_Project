import os

desktop_path = r'C:\Users\user\OneDrive\Desktop'


def change_dir(file):
    if file != 'Music':
        file = 'Homeworks\\' + file
    else:
        file = 'Music'
    needed_paths = os.path.join(desktop_path, file)
    if not os.path.exists(needed_paths):
        os.makedirs(needed_paths)
    new_path = os.path.join(needed_paths, name)
    os.rename(old_path, new_path)


for path, subdirs, files in os.walk(desktop_path):
    for name in files:
        old_path = os.path.join(path, name)
        if name.endswith('.mp3'):
            change_dir('Music')
        elif name.endswith('.docx'):
            change_dir('Docs')
        elif name.endswith('.pdf'):
            change_dir('PDFs')
        elif name.endswith('.pptx'):
            change_dir('Powerpoints')
        elif name.endswith('.csv') or name.endswith('.xlsx'):
            change_dir('Excels')
        elif name.endswith('.zip'):
            change_dir('Zips')
        elif name.endswith('.jpg') or name.endswith('.png') or name.endswith('.jpeg'):
            change_dir('Photos')
print("Task Completed")
