import os
import sys
# import magic

blacklist = ["keyword1", "keyword2", "keyword3"]

exclude_folders = ['.git']


def is_text_file(file_path):
    # mime = magic.Magic(mime=True)
    # file_type = mime.from_file(file_path)
    # return file_type.startswith('text')
    return True

def scan_file(file_path):
    print(file_path)
    with open(file_path, 'r') as f:
        for line_number, line in enumerate(f, 1):
            for keyword in blacklist:
                if keyword in line:
                    print(f'File: {file_path}, Line: {line_number}, Keyword: {keyword}')

def scan_directory(directory):
    for root, dirs, files in os.walk(directory):
        for exclude in exclude_folders:
            if exclude in dirs:
                dirs.remove(exclude)

        for file in files:
            file_path = os.path.join(root, file)
            if os.path.isfile(file_path) and is_text_file(file_path):
                scan_file(file_path)


if __name__ == "__main__":
    directory = os.getcwd()

    if len(sys.argv) == 2:
        directory = sys.argv[1]

    scan_directory(directory)
