import os
from pypdf import PdfReader

folder = "data/resumes"

for file in os.listdir(folder):
    if file.endswith(".pdf"):
        path = os.path.join(folder, file)

        reader = PdfReader(path)
        text = ""

        for page in reader.pages:
            text += page.extract_text()

        lines = text.split("\n")

        print("\n" + "="*50)
        print("File:", file)
        print("Name:", lines[0])
        print("="*50)