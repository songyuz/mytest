import os

# 黑名单词列表
blacklist = ["word1", "word2", "word3"]

def check_file_for_blacklist(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        for line_number, line in enumerate(file, 1):
            for word in blacklist:
                if word in line:
                    print(f'File: {file_path}, Line: {line_number}, Keyword: {word}')

def read_files_in_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            check_file_for_blacklist(file_path)


current_directory = os.getcwd()


read_files_in_directory(current_directory)