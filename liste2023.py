import csv
import re

# Raw text, cleaned version for demonstration (normally, parsed programmatically)
courses_raw = [
    (1, "Intro to Coding with Python Turtle [2022]", "1h 13m", "Entry Level", "https://academy.zenva.com/course/intro-to-coding-with-python-turtle-2022/", "73%"),
    (2, "Python Turtle Mini-Projects [2022]", "2h 10m", "-", "https://academy.zenva.com/course/python-turtle-mini-projects-2022/", ""),
    (3, "Build a Medical Diagnosis Bot with Python", "1h 48m", "Beginner", "https://academy.zenva.com/course/build-a-medical-diagnosis-bot-with-python/", ""),
    (4, "Python Projects – Object-Oriented Game", "2h 27m", "Beginner", "https://academy.zenva.com/course/create-an-escape-room-with-python/", ""),
    (5, "Prompt Engineering for Programmers", "41m", "Entry Level", "https://academy.zenva.com/course/ai-prompt-engineering-for-developers/", "75%"),
    (6, "The Complete AI Developer Course with Google Gemini Pro", "1h 37m", "Intermediate", "https://academy.zenva.com/course/the-complete-ai-developer-course-with-google-palm/", ""),
    (7, "Create a Bot with Python and ChatGPT", "41m", "Beginner", "https://academy.zenva.com/course/create-a-bot-with-python-and-chatgpt/", ""),
    (8, "Web-Based Chatbot with Python and ChatGPT", "52m", "Intermediate", "https://academy.zenva.com/course/web-based-chatbot-with-python-and-chatgpt/", ""),
    (9, "Retrieval Augmented Generation with LlamaIndex", "1h 1m", "Intermediate", "https://academy.zenva.com/course/llamaindex-course/", ""),
    (10, "Numpy Matrices and Vectors", "1h 36m", "Beginner", "https://academy.zenva.com/course/introduction-to-numpy/", ""),
    (11, "Machine Learning with Python and Tensorflow", "2h 34m", "Intermediate", "https://academy.zenva.com/course/machine-learning-for-beginners-with-tensorflow/", ""),
    (12, "Convolutional Neural Networks for Image Classification", "2h 17m", "Intermediate", "https://academy.zenva.com/course/convolutional-neural-networks-for-image-classification/", ""),
    (13, "Python Image Processing – Make Instagram-Style Filters", "3h 9m", "Intermediate", "https://academy.zenva.com/course/python-image-processing-by-making-instagram-style-filters/", ""),
    (14, "Intro to Web Scraping with Python", "1h 1m", "Beginner", "https://academy.zenva.com/course/intro-to-web-scraping-with-python/", ""),
    (15, "Web Scraping and Data Cleaning with Python", "1h 36m", "Intermediate", "https://academy.zenva.com/course/intermediate-web-scraping-and-data-cleaning-with-python/", ""),
    (16, "Intro to Regular Expressions in Python", "55m", "Beginner", "https://academy.zenva.com/course/python-regular-expressions-course/", ""),
    (17, "Python Automation Project – Scraping Tabular Data", "1h 51m", "Intermediate", "https://academy.zenva.com/course/python-automation-project-scraping-tabular-data/", ""),
    (18, "Reading Data from APIs with Python", "1h 24m", "Beginner", "https://academy.zenva.com/course/reading-data-from-apis-with-python/", ""),
    (19, "Intro to Pygame", "2h 32m", "Beginner", "https://academy.zenva.com/course/intro-to-pygame/", "2%"),
    (20, "Intermediate Python – Virtual Pet with Pygame", "2h 25m", "Intermediate", "https://academy.zenva.com/course/intermediate-python-virtual-pet-with-pygame/", ""),
    (21, "Beginning SQL – Store and Query Your Data", "1h 56m", "Beginner", "https://academy.zenva.com/course/beginning-sql-store-and-query-your-data/", ""),
    (22, "Intermediate SQL – Create and Alter Databases", "1h 21m", "Intermediate", "https://academy.zenva.com/course/intermediate-sql/", ""),
    (23, "Data Manipulation with Pandas", "1h 22m", "Beginner", "https://academy.zenva.com/course/data-manipulation-with-pandas/", ""),
    (24, "Data Analysis with Pandas", "1h 39m", "Intermediate", "https://academy.zenva.com/course/data-analysis-with-pandas/", ""),
    (25, "Data Insights with Cluster Analysis", "2h 17m", "Intermediate", "https://academy.zenva.com/course/data-insights-with-cluster-analysis/", ""),
    (26, "Probability Foundations for Data Science", "1h 30m", "Intermediate", "https://academy.zenva.com/course/probability-foundations-for-data-science/", ""),
    (27, "Hypothesis Testing for Data Science", "2h 48m", "Intermediate", "https://academy.zenva.com/course/hypothesis-testing-for-data-science/", ""),
    (28, "The Complete Python Data Visualization Course", "3h 3m", "Intermediate", "https://academy.zenva.com/course/the-complete-python-data-visualization-course/", ""),
    (29, "Intro to Object-Oriented Programming with Python", "2h 39m", "Beginner", "https://academy.zenva.com/course/python-programming-for-beginners/", ""),
    (30, "Bite-Sized Python Programming", "55m", "Entry Level", "https://academy.zenva.com/course/bite-sized-python-programming/", "100%")
]

header = ["Nom du cours", "Durée", "Niveau", "Lien", "Progression"]

with open("cours_zenva_python_bundle.csv", "w", encoding="utf-8-sig", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for c in courses_raw:
        writer.writerow([c[1], c[2], c[3], c[4], c[5]])

# For download: output CSV as text for display
import pandas as pd
df = pd.DataFrame([[c[1], c[2], c[3], c[4], c[5]] for c in courses_raw], columns=header)
df.to_csv("cours_zenva_python_bundle.csv", encoding="utf-8-sig", index=False)
with open("cours_zenva_python_bundle.csv", "r", encoding="utf-8-sig") as f:
    csv_content = f.read()
csv_content
