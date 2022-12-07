"""
Advent Of Code 2022 Day 7
Author: PineapplePeddler
Date: 07/12/22
"""

class directory(object):
    def __init__(self,name,subdirs,files) -> None:
        self.name = name
        self.subdirs = subdirs
        self.files = files
    
    def add_subdir(self, subdir):
        self.subdirs.append(subdir)

    def add_file(self, file):
        self.files.append(file)

    def calc_size(slef):
        size = 0

        for directory in slef.subdirs:
            size += directory.calc_size()

        for file in slef.files:
            size += file.sile

        return size



class file(object):
    def __init__(self, name, size) -> None:
        self.name = name
        self.size = size


# class File:
#     def __init__(self,text) -> None:
#         text = re.split('\s|\.',text)
#         self.name = name
#         self.size = size
#         self.type = type

# def create_files(text):
#     for i in range(0, len(text)):
#         if not ('$' in text[i] or 'dir' in text[i]):
#             file_info = text [i]
#             file_info = re.split('\s|\.',file_info)
#             if len(file_info) == 3:
#     return text

# Import termianal text
with open("2022/Day7_Input.txt") as f:
   terminal_data = f.read().split("\n")

# Remove unhelpful cd comands
terminal_data = [command for command in terminal_data if command != '$ cd ..']
# remove unhelpful ls commands
terminal_data = [command for command in terminal_data if command != '$ ls']

# Organise into directories with sib directories and files.

directories = []
current_directory = -1
files = []

for line in terminal_data:
    if '$ cd' in line:
        current_directory += 1
        directories.append(directory(line.replace('& cd ',''),[],[]))
    if 'dir' in line:
        directories[current_directory].add_subdir(line.replace('dir ',''))
    else:
        file_info = line.split(' ')
        files.append(file(file_info[1],file_info[0]))
        directories[current_directory].add_file(files[-1])

# Find sum of sizes of directories smaller than 100000

total_size = 0

print(directories[1])

for directory in directories:
    size = directory.calc_size()
    if size <= 100000:
        total_size += size

print(total_size)