from pikepdf import Pdf
from PyPDF2 import PdfFileReader
import os
import csv
from glob import glob
from src.better_txt import better_txt_converter
import sys

files_processed = 0
files_that_exist = 0

def process_files(password, download_path, unencrypted_path, csv_path):
    """Driver of individual processes that ultimately convert an
    encrypted pdf into a csv file.
    """
    unencrypt(password, download_path, unencrypted_path)
    convert_to_text(unencrypted_path, csv_path)
    better_txt_converter(csv_path)
    clean_up(csv_path)

def unencrypt(password, download_path, unencrypted_path):
    """Unencrypts pdf file, password must be provided.
    Also checks if file has already been unencrypted.
    """

    global files_processed
    global files_that_exist

    possible_download_files = os.path.join(download_path, "*.pdf")
    possible_unencrypted_files = glob(os.path.join(unencrypted_path, "*.pdf"))
    for file_name in glob(possible_download_files):

        output_pdf_path = os.path.join(unencrypted_path, file_name[-39:])
        output_pdf_path = output_pdf_path[:-4] + ".pdf"

        if output_pdf_path not in possible_unencrypted_files:
            input_pdf = Pdf.open(file_name, password)
            output_pdf = Pdf.new()
            output_pdf.pages.extend(input_pdf.pages)
            output_pdf.save(output_pdf_path)
            files_processed += 1

        else:
            files_that_exist += 1

        sys.stdout.write(f"\rPdf Files processed: {files_processed} --- " \
                        f"Pdf files that already exist: {files_that_exist}")
    print()

def convert_to_text(unencrypted_path, csv_path):
    """Converts pdf file to a text file.
    Also checks if file has already been converted
    """

    possible_unencrypted_files = glob(os.path.join(unencrypted_path, "*.pdf"))
    possible_text_files = glob(os.path.join(csv_path, "*.txt"))

    for file_name in possible_unencrypted_files:

        output_txt = os.path.join(csv_path, file_name[-39:])
        output_txt = output_txt[:-4] + ".txt"

        if output_txt not in possible_text_files:
            with open(file_name, "rb") as pdf, open(output_txt,"w", newline='')\
                as text_file:

                input_pdf = PdfFileReader(pdf)
                for page in input_pdf.pages:
                    text_file.write(page.extractText())

    return csv_path

def clean_up(csv_path):
    """Deletes text files that were created in processing, keeps csv files"""
    possible_text_files = glob(os.path.join(csv_path, "*.txt"))
    for file in possible_text_files:
        os.remove(file)
