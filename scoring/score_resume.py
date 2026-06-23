import os
from pypdf import PdfReader

folder = "data/resumes"

skills = [
    "Python",
    "Machine Learning",
    "SQL",
    "Java",
    "Deep Learning",
    "Data Science"
]

for file in os.listdir(folder):

    if file.endswith(".pdf"):

        path = os.path.join(folder, file)

        reader = PdfReader(path)

        text = ""

        for page in reader.pages:
            text += page.extract_text()

        score = 0

        for skill in skills:

            if skill.lower() in text.lower():
                score += 10

        print("\n" + "="*50)
        print("Resume:", file)
        print("Score:", score)
        print("="*50)