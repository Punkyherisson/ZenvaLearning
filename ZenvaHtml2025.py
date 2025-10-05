import csv

courses = [
    ["Intro to Web Development with HTML and CSS", "Intro Coding 2025", "2h 7m", "Entry Level", "https://academy.zenva.com/course/intro-to-web-development-with-html-and-css/"],
    ["Create Your First Responsive Website", "Intro Coding 2025", "58m", "Beginner", "https://academy.zenva.com/course/create-your-first-responsive-website/"],
    ["HTML Foundations", "Intro Coding 2025", "1h 13m", "Entry Level", "https://academy.zenva.com/course/html-foundations/"],
    ["CSS Foundations", "Intro Coding 2025", "1h 12m", "Beginner", "https://academy.zenva.com/course/css-foundations/"],
    ["JavaScript Programming for Beginners", "Intro Coding 2025", "2h 17m", "Entry Level", "https://academy.zenva.com/course/javascript-programming-for-beginners/"],
    ["JavaScript Mini-Projects – Language Learning Game", "Intro Coding 2025", "56m", "Beginner", "https://academy.zenva.com/course/javascript-mini-projects-language-learning-game/"],
    ["JavaScript Foundations", "Intro Coding 2025", "1h 18m", "Entry Level", "https://academy.zenva.com/course/javascript-foundations/"],
    ["Intermediate JavaScript – Build a Dynamic Data Table", "Intro Coding 2025", "1h 8m", "Intermediate", "https://academy.zenva.com/course/intermediate-javascript-build-a-dynamic-data-table/"],
    ["Build 3D Web Apps with Babylon.js", "Intro Coding 2025", "1h 30m", "Beginner", "https://academy.zenva.com/course/build-3d-web-apps-with-babylon-js/"],
    ["Intro to SQL and Databases with MySQL", "Intro Coding 2025", "1h 35m", "Entry Level", "https://academy.zenva.com/course/intro-to-sql-course/"],
    ["Learn Rust Programming for Beginners", "Intro Coding 2025", "2h 3m", "Beginner", "https://academy.zenva.com/course/intro-to-rust-course/"],
    ["Data Structures with Rust", "Intro Coding 2025", "1h 8m", "Beginner", "https://academy.zenva.com/course/rust-data-structures-course/"],
    ["Rust Parallel Computing Project – Image Processor", "Intro Coding 2025", "1h 8m", "Beginner", "https://academy.zenva.com/course/rust-image-processor/"],
    ["Practical Rust – CLI Tools with Clap and Indicatif", "Intro Coding 2025", "1h 32m", "Intermediate", "https://academy.zenva.com/course/rust-command-line-app-course/"],
    ["Rust Web App Project – Collaborative Document Editing", "Intro Coding 2025", "1h 33m", "Intermediate", "https://academy.zenva.com/course/rust-web-app-collab-document/"],
    ["Rust Web App Project – Real-Time Video Broadcasting", "Intro Coding 2025", "2h 20m", "Intermediate", "https://academy.zenva.com/course/rust-rtc-video-web-app-course/"],
    ["Intro to Coding with Python Turtle", "Intro Coding 2025", "59m", "Entry Level", "https://academy.zenva.com/course/intro-to-coding-with-python-turtle/"],
    ["Python Turtle Mini-Projects", "Intro Coding 2025", "1h 36m", "Beginner", "https://academy.zenva.com/course/python-turtle-mini-projects/"],
    ["Python Projects – Object-Oriented Game", "Intro Coding 2025", "2h 27m", "Beginner", "https://academy.zenva.com/course/create-an-escape-room-with-python/"],
    ["Python Image Processing with Pillow", "Intro Coding 2025", "1h 1m", "Beginner", "https://academy.zenva.com/course/intro-to-pillow/"],
    ["Intro to Developing AI Agents with Python & CrewAI", "Intro Coding 2025", "1h 12m", "Beginner", "https://academy.zenva.com/course/crewai-intro-course/"],
    ["AI Agent Project with Python & CrewAI", "Intro Coding 2025", "1h 41m", "Intermediate", "https://academy.zenva.com/course/crewai-study-buddy-app-course/"],
    ["Intermediate Python – Virtual Pet with Pygame", "Intro Coding 2025", "2h 25m", "Intermediate", "https://academy.zenva.com/course/intermediate-python-virtual-pet-with-pygame/"],
    ["Intermediate Python – Learn Pygame by Making a Game", "Intro Coding 2025", "2h 34m", "Intermediate", "https://academy.zenva.com/course/learn-python-and-pygame-by-making-a-game/"],
    ["Python Data Structures for Beginners", "Intro Coding 2025", "1h 10m", "Beginner", "https://academy.zenva.com/course/python-data-structures-course/"],
    ["Intro to Algorithms with Python", "Intro Coding 2025", "1h 15m", "Beginner", "https://academy.zenva.com/course/algorithms-with-python/"],
    ["Graphs Data Structure and Algorithms with Python", "Intro Coding 2025", "1h 24m", "Beginner", "https://academy.zenva.com/course/python-graphs-algorithms/"],
    ["Intro to Regular Expressions in Python", "Intro Coding 2025", "55m", "Beginner", "https://academy.zenva.com/course/python-regular-expressions-course/"],
    ["Pandas Project – Flight Data Analysis", "Intro Coding 2025", "1h 13m", "Intermediate", "https://academy.zenva.com/course/pandas-data-analysis/"],
    ["Intro to Object-Oriented Programming with Python", "Intro Coding 2025", "2h 39m", "Beginner", "https://academy.zenva.com/course/python-programming-for-beginners/"],
    ["Intro to Django for Python Web App Development", "Intro Coding 2025", "1h 43m", "Beginner", "https://academy.zenva.com/course/intro-to-django-course/"],
    ["Intro to Flask for Web App Development", "Intro Coding 2025", "43m", "Beginner", "https://academy.zenva.com/course/intro-to-flask/"],
    ["Build a Web Application with Flask", "Intro Coding 2025", "1h", "Intermediate", "https://academy.zenva.com/course/flask-web-app-project/"],
    ["Learn Vibe Coding with Cursor", "Intro Coding 2025", "47m", "Beginner", "https://academy.zenva.com/course/vibe-coding-course/"],
    ["The Complete Introduction to C++", "Intro Coding 2025", "3h 24m", "Entry Level", "https://academy.zenva.com/course/the-complete-introduction-to-c/"],
    ["Intro to C++ Data Structures", "Intro Coding 2025", "1h 56m", "Beginner", "https://academy.zenva.com/course/intro-to-c-data-structures/"],
    ["Learn Object-Oriented C++ by Building a Game", "Intro Coding 2025", "3h 58m", "Beginner", "https://academy.zenva.com/course/learn-object-oriented-c-by-building-a-game/"],
    ["The Comprehensive Introduction to C# Programming", "Intro Coding 2025", "2h 42m", "Entry Level", "https://academy.zenva.com/course/intro-to-csharp/"],
    ["Intro to UI/UX Design", "Intro Coding 2025", "48m", "Entry Level", "https://academy.zenva.com/course/intro-to-ui-ux-design/"],
    ["Prompt Engineering for Programmers", "Intro Coding 2025", "41m", "Entry Level", "https://academy.zenva.com/course/ai-prompt-engineering-for-developers/"]
]

filename = "zenva_courses_formatted.csv"
with open(filename, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Titre du cours", "Groupe", "Durée", "Niveau", "Lien"])
    for c in courses:
        writer.writerow(c)
filename