import os
import csv
from datetime import datetime
from glob import glob
import sys

csv_files_processed = 0
csv_files_that_exist = 0

def better_txt_converter(path):
    """Checks if file has already been processed and if not
    it calls the converter method.
    """
    global csv_files_processed
    global csv_files_that_exist
    possible_text_files = glob(os.path.join(path, "*.txt"))
    possible_csv_files = glob(os.path.join(path, "*_processed.csv"))
    for file in possible_text_files:
        csv_path = file[:-4] + "_processed.csv"

        if csv_path not in possible_csv_files:

            csv_files_processed += 1
            converter(file)
        else:
            csv_files_that_exist += 1

        sys.stdout.write(f"\rCsv files created: {csv_files_processed} --- " \
                        f"Csv files that already exist: {csv_files_that_exist}")
    print()

def converter(path):
    """Creates an easier to work with txt file.
    Returns file path
    """
    list_of_months = ["January", "February", "March", "April", "May", \
                    "June", "July", "August", "September", "October", \
                    "Novmeber", "December"]

    output_path = path[:-4] + "_better.txt"
    list_of_lines=[]
    list_of_strings=[]
    line_input=""

    with open(path, 'r') as input, open(output_path, 'w') as output:
        for curr in input.readlines():
            list_of_lines.append(curr[:-1])
        enumerated_list = enumerate(list_of_lines)

        list_of_index = []
        curr_index = curr_next = 0
        for i,j in enumerated_list:
            if j in list_of_months:
                list_of_index.append(i)

        for i in range(len(list_of_index)):
            if list_of_index[i] == list_of_index[-1]:
                j = list_of_index[i]
                j = j - 1
                list_of_strings.append(list_of_lines[j:])
            else:
                j = list_of_index[i]
                j = j - 1
                k = list_of_index[i+1]
                k = k - 1
                list_of_strings.append(list_of_lines[j:k])

        query = "Customer Care: 0860 123 000"
        for i in range(len(list_of_strings)):
            index = list_of_strings[i].index(query) if query in list_of_strings[i] else -1
            if index != -1:
                list_of_strings[i] = list_of_strings[i][:6]

        for i in range(len(list_of_strings)):
            curr = list_of_strings[i]
            if len(curr) < 6:
                curr.append("##")
                curr[3], curr[-1] = curr[-1], curr[3]
                curr[4], curr[-1] = curr[-1], curr[4]
                list_of_strings[i] = curr

        for i in range(len(list_of_strings)):
            curr = list_of_strings[i]
            day = curr[0]
            month = curr[1]
            year = "2019"
            date = f"{year}-{month}-{day}"
            date_string = datetime.strptime(date, '%Y-%B-%d').strftime("%Y-%m-%d")
            curr[0] = date_string
            curr.pop(1)
            list_of_strings[i] = curr


        for i in range(len(list_of_strings)):
            str_input = " ".join(list_of_strings[i])
            output.writelines(str_input)
            output.write("\n")

        csv_path = path[:-4] + ".csv"
        with open(csv_path, "w", newline='') as output_csv:
            writer = csv.writer(output_csv)
            writer.writerows(list_of_strings)

    return output_path

def main():
    txt_file = r"C:\Users\Study\Documents\Budget_project\cache\combined.txt"
    print(txt_file)
    converter(txt_file)

if __name__ == "__main__":
    main()
