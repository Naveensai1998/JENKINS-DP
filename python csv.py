

#Text file
f=open("C:/Users/User/OneDrive/Desktop/file.txt")
print("f")

# csv file
import csv
def read_csv_file(file_path):
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            print(row)
read_csv_file("C:/Users/User/OneDrive/Desktop/file.csv")
print("PDF file")

#pdf file
from PyPDF2 import PdfReader
# Replace 'filename.pdf' with the path to your PDF file
file_path = 'C:/Users/User/OneDrive/Desktop/resume.pdf'
# Open the PDF file using PdfReader
pdf_reader = PdfReader(file_path)
# Loop through all pages and extract text
for page_num in range(len(pdf_reader.pages)):
    page = pdf_reader.pages[page_num]
    text = page.extract_text()
    print(f"Page {page_num + 1}:\n{text}\n")
print("Excel file")

#read excel file
import pandas as pd
def read_excel_file(C:/Users/User/OneDrive/Desktop):
    df = pd.read_excel(C:/Users/User/OneDrive/Desktop)
    print(df)
# Usage example
file_path_excel = 'C:/Users/User/OneDrive/Desktop/excel_file.xlsx'
read_excel_file(file_path_excel)
print("Json file")

#Read JSON file:
import json
def read_json_file(file_path):
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
        print(data)
# Usage example
file_path_json = 'C:/Users/User/OneDrive/Desktop/file.json'
read_json_file(file_path_json)

# image file
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def show_image(image_path):
    img = mpimg.imread(image_path)
    plt.imshow(img)
    plt.axis('off')
    plt.show()

# Replace 'path_to_your_image.jpg' with the actual path to your image file.
image_path = 'C:/Users/User/OneDrive/Desktop/image.jpg'
show_image(image_path)




