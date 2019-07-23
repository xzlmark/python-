import os
path = os.getcwd()
all_files = []
list_files = os.walk(path)
for dirpath,dirnames,filenames in list_files:
    for dir in dirnames:
        all_files.append(os.path.join(dirpath,dir))
    for name in filenames:
        all_files.append(os.path.join(dirpath,name))
for file in all_files:
    print(file)
    
