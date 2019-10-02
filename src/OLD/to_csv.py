import csv

def convert_to_csv(path):
    csv_path = path[:-4] + "_csv.csv"
    with open(csv_path, "w", newline='') as output_csv:
        writer = csv.writer(output_csv)
        writer.writerows(list_of_strings)

def main():
    path = r"C:\Users\Study\Documents\Budget_project\cache\SBSA_Statement_25-08-2019_0_unecrypted_better.txt"
    convert_to_csv(path)

if __name__ == "__main__":
    main()
