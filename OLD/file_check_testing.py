import os
from glob import glob

path = r"C:\Users\Study\Documents\Budget_project\cache"
possible_files = os.path.join(path, "*.pdf")
file_dict = {}
for file_name in glob(possible_files):
    curr = file_name[-24:-14]
    if curr in file_dict.keys():
        file_dict[curr] = 2
    else:
        file_dict.update({curr : 1})

print(file_dict)
