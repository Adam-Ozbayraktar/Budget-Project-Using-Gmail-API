import os

def better_txt(path):
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
        for curr in list_of_lines:
            if curr not in list_of_months:
                line_input = line_input + " " + curr
            else:
                line_input = line_input + "\n"
                list_of_strings.append(line_input[1:])
                line_input=""

        list_of_strings.pop(0)
        index = 0
        for curr in list_of_strings:
            search = curr.find("Customer Care: 0860 123 000 Website:")
            if search != -1:
                list_of_strings[index] = curr[:search] + "\n"
            index = index + 1
        output.writelines(list_of_strings)

def main():
    file_path = r"C:\Users\Study\Documents\budget_project\cache"
    txt_file = os.path.join(file_path, "SBSA_Statement_unecrypted.txt")
    better_txt(txt_file)

if __name__ == "__main__":
    main()
