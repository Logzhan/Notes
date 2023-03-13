import os
import chardet
import codecs
import tkinter as tk
from tkinter import filedialog


# 获取给定目录中的所有文件和子目录
def get_all_files(directory):
    files = []
    # 遍历目录中的所有文件和子目录
    for root, subdirs, files_list in os.walk(directory):
        for file in files_list:
            file_path = os.path.join(root, file)
            files.append(file_path)
    return files


# 检测文件编码格式
def detect_encoding(file_path):
    with open(file_path, 'rb') as file:
        raw_data = file.read(8192)
    return chardet.detect(raw_data)['encoding']


# 将文件转换为UTF-8编码格式
def convert_to_utf8(file_path, from_encoding):
    with codecs.open(file_path, 'r', encoding=from_encoding, errors='ignore') as file:
        lines = file.read()
    with codecs.open(file_path, 'w', encoding='utf-8') as file:
        file.write(lines)


# 将给定目录下的所有文件转换为UTF-8编码格式
def convert_files_in_directory(directory_path):
    files = get_all_files(directory_path)
    for file in files:
        if file.endswith('.py') or file.endswith('.c') or file.endswith('.cpp') or file.endswith('.h'):
            from_encoding = detect_encoding(file)
            if from_encoding != 'utf-8':
                print("file = " + file + "encoding = " + from_encoding)
                convert_to_utf8(file, from_encoding)
    print('所有文件均已转换为UTF-8编码格式')


# 按钮单击时执行的函数
def browse_folder():
    folder_path = filedialog.askdirectory()
    convert_files_in_directory(folder_path)


# 创建一个Tkinter窗口，其中包含一个选择文件夹的按钮
window = tk.Tk()
window.geometry('200x100')
button = tk.Button(text='选择文件夹', command=browse_folder)
button.pack()
window.mainloop()