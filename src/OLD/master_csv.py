import os
from glob import glob
import csv

def create_master_csv(path):
    possible_csv_files = glob(os.path.join(path, "*.csv"))
    master_path = os.path.join(path, "master.csv")
    """
    for file in possible_csv_files:
        bank_trans = csv.reader(open(file, newline=''))
    """
    master_list_1 = []
    with open(possible_csv_files[1], 'r') as curr, open(master_path, 'rb') as master:
        temp = curr.readlines()
        master_file = master.readlines()
        master_list_1 = list(master_file)
        #print(master_list_1)

        for line in temp:
            if line not in master_list_1:
                line_list = []
                line_list.append(line)
                master_list_1.append(line_list)
        #print(master_list_1[2][0])
        print(master_list_1)
        for i in range(len(master_list_1)):
            file_name = "output.csv"
            print(master_list_1[i][0])
            with open(os.path.join(path,file_name), 'w', newline='') as output:
                writer = csv.writer(output)
                #print(master_list_1[0][0])
                writer.writerows(master_list_1[i][0])

def main():
    path = r"C:\Users\Study\Documents\budget_project\cache\csv"
    create_master_csv(path)

if __name__ == "__main__":
    main()
