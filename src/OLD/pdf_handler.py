from pikepdf import Pdf
from PyPDF2 import PdfFileReader
import os
import csv

def unencrypt(path, password):
    """Unecrypts pdf document and saves a copy in same directory.
    Returns the new path of the unencrypted file.
    """

    input_pdf = Pdf.open(path, password)
    output_pdf = Pdf.new()
    output_pdf.pages.extend(input_pdf.pages)
    output_pdf_path = path[:-4] + "_unecrypted.pdf"
    output_pdf.save(output_pdf_path)

    return output_pdf_path

def convert_to_text(path):
    """Converts pdf file to text
    Returns the new path of text file
    """
    
    output_txt = path[:-4] + ".txt"
    with open(path, "rb") as pdf, open(output_txt, "w", newline='') as text_file:
        input_pdf = PdfFileReader(pdf)
        for page in input_pdf.pages:
            text_file.write(page.extractText())

    return output_txt
    """
    output_csv = path[:-4] + ".csv"
    with open(path, "rb") as pdf, open(output_csv, "w", newline='') as csv_file:
        input_pdf = PdfFileReader(pdf)
        writer = csv.writer(csv_file)
        for page in input_pdf.pages:
            writer.writerows(page)
    """
def main():
    file_path = r'C:\Users\Study\Documents\budget_project\cache'
    encrypted_file = os.path.join(file_path, "SBSA_Statement (3).pdf")
    password = "Adamozbayr"

    unecrypted_file = unencrypt(encrypted_file, password)

    text_file = convert_to_text(unecrypted_file)

    print(f"Output unencrypted file:\n{unecrypted_file}\n\nOutput text_file:\n{text_file}")

if __name__ == "__main__":
    main()
