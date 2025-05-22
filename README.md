🎮 Quizzy Crafter Simulator

**Quizzy Crafter** is a creative and fun GUI-based quiz application built using Python’s Tkinter and OOP principles. It allows users to **create**, **take**, and **score** custom quizzes — all wrapped in a stylish, interactive interface with sound and visuals!

---

## 📦 Features

- 🎨 Start screen with clickable image-based buttons
- 🛠️ Create custom quizzes (title, description, questions, choices)
- 📁 Save and load quizzes from JSON files
- 🧠 Take quizzes with randomized questions
- 📊 Score display with correct answers summary
- 💾 Save results to text files
- 🔊 Includes sound effects and styled UI

🛠️ Requirements

Make sure the following are set up before running the app:

- Python 3 installed
- Pillow library (PIL fork) for handling images in the GUI


📦 Installing Pillow

You need to install Pillow in your terminal (or command prompt) before running the application. Here's how:

Open Terminal (or Command Prompt on Windows, or the Terminal panel in VS Code).
Run this command: pip install pillow

⚠️ Without Pillow installed, running the app will raise an ImportError, and image components like buttons and backgrounds won't display properly.

📂 Setup Instructions

*Download Assets: Make sure to download all the files inside the assets/ folder. These include the GUI images such as buttons, backgrounds, and custom text visuals required for the interface to display correctly.
Run the main Python file using the terminal: main.py

🧠 How It Works

The app uses object-oriented programming with inheritance. Each screen (Start, Create, Take Quiz, etc.) inherits from a base class that handles shared logic like loading images and switching frames.

Data like quiz title, questions, and answers are managed via the QuizManager class, saved as .json files, and user results are stored as .txt files in the quiz_results folder.

📂 Folder Structure
quizzy_crafter_oop_conversion/
├── base_screen.py # Base class for all screen UIs

├── create_quiz.py # Handles quiz creation flow

├── main.py # Entry point for the application

├── quiz_manager.py # Loads, saves, resets quiz data

├── quiz_questions.py # Displays and tracks questions/answers

├── score_screen.py # Shows final score and saves results

├── start_menu.py # Main start screen

├── take_quiz.py # Name input and quiz selection

├── quizzes/ # Contains created quizzes (JSON)

├── quiz_results/ # Contains quiz results (JSON)

└── README.md # This file

- The quizzes/ folder stores all quizzes created using the app.
- The quiz_results/ folder stores results when a quiz is taken.
- These folders are automatically created if they don't already exist.

🎨 Assets
assets/
├── start_bg.png

├── create_bg.png

├── take_bg.png

├── score_bg.png

├── click.wav

├── create_button.png

├── take_button.png

├── next_button.png

├── add_question_button.png

├── save_button.png

├── back_button.png

├── submit_button.png
