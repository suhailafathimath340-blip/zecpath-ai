from pypdf import PdfReader
import os

folder = "data/resumes"

files = os.listdir(folder)

for file in files:
    path = os.path.join(folder, file)

    reader = PdfReader(path)

    text = ""

    for page in reader.pages:
        text += page.extract_text()

    lines = text.split("\n")

    print("\n" + "="*50)
    print("File:", file)
    print("Name:", lines[0])