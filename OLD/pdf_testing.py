import PyPDF2

file_path = r'C:\Users\Study\Documents\budget_project\cache\xxxxx5076.pdf'
#file_path = r'C:\Users\Study\Documents\budget_project\cache\Christine Pile ER Session 6.pdf'
#input_pdf = PdfFileReader(file_path)
#input_pdf.decrypt('9604175075084')

with open(file_path, mode='rb') as f:
    reader = PyPDF2.PdfFileReader(f)
    if reader.isEncrypted:
        reader.decrypt('9604175075084')
        print(f"Number of pages: {reader.getNumPages()}")


page0 = input_pdf.getPage(0)
page0_text = page0.extractText()

print(page0_text)
