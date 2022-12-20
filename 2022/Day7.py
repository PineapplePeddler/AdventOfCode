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

    def calc_size(self, directories):
        size = 0
        # print(self.subdirs)
        for subdirectory in self.subdirs:
            # print(subdirectory)
            for directory_1 in directories:
                # print(directory_1.name)
                if directory_1.name == subdirectory:
                    print("calculating sub directory size" )
                    size += directory_1.calc_size(directories)

        for file in self.files:
            size += file.size

        return size



class file(object):
    def __init__(self, name, size) -> None:
        self.name = name
        self.size = int(size)


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

for i in range(0,len(terminal_data)):
    if '$ ls' in terminal_data[i]:
        if '$ cd' not in terminal_data[i-1]:
            print('ls not proceded by cd')

# Remove unhelpful cd comands
terminal_data = [command for command in terminal_data if command != '$ cd ..']
# remove unhelpful ls commands
terminal_data = [command for command in terminal_data if command != '$ ls']

# Organise into directories with sib directories and files.

directories = []
current_directory = -1
files = []

for line in terminal_data:
    if "$ cd" in line:
        dir_exists = False
        dir_name = line.replace('$ cd ','')
        for directory_a in directories:
            if directory_a.name == dir_name:
                dir_exists = True
        
        if dir_exists == False:
            current_directory += 1
            directories.append(directory(line.replace('$ cd ',''),[],[]))
        else:
            continue

    elif 'dir ' in line:
        directories[current_directory].add_subdir(line.replace('dir ',''))
    else:
        file_info = line.split(' ')
        files.append(file(file_info[1],file_info[0]))
        directories[current_directory].add_file(files[-1])

#Check for repeated directories
""" 

print(len(directories))

for i in range(0,len(directories)-1):
    for j in range(i+1,len(directories)):
        if directories[i].name == directories[j].name:
            print("directory repeated")
            print(directories[i].name)

directory_names = []
for directory in directories:
    directory_names.append(directory.name)

print(sorted(directory_names))
"""

# Find sum of sizes of directories smaller than 100000

total_size = 0

for directory in directories:
    if directory.name != "/":
        print(directory.name)   
        size = directory.calc_size(directories)
        print(size)
        if size <= 100000:
            total_size += size

print(total_size)