2026 Monthly Habit Dashboard Generator

📥 Download the App (No Coding Required)

If you do not want to run the Python code yourself, you can download the standalone Windows application directly from this repository:

Look for the "Releases" section on the right-hand sidebar of this page.

Click on the release titled Habit Tracker (Windows).

Scroll down to the "Assets" section.

Click on habit_tracker.exe to download the file.

Note: If Windows Defender warns you about an unrecognized app, click "More Info" > "Run Anyway". This occurs because this is a personal open-source tool not digitally signed by a major corporation.

📖 Project Overview
This project is an interactive Python tool that generates a complete set of 12 printable habit tracking dashboards for the year 2026. Version 3 introduces user customization, allowing you to input a specific social media handle or name at runtime. The script generates high-resolution, landscape-oriented PDF files designed to help users track daily habits, sleep patterns, and goals.

🛠 Tech Stack
Language: Python 3.x

Libraries: matplotlib, calendar, numpy, os

Distribution: Standalone Windows Executable (.exe)

✨ Key Features
Interactive Personalization (New in v3):

Prompts the user to enter a custom "Handle" (e.g., @MyName, GoalCrusher) upon launching.

Includes a smart default: if no name is entered, it automatically defaults to @Nidhijain.

Extended Tracking Capacity:

20-Row Habit Grid: Expanded layout to track extensive daily routines.![unnamed](https://github.com/user-attachments/assets/d3b02acf-ebb4-43d9-b7f4-81db6d4d2c8e)


Gamification: Includes a "Total Points" row to sum up daily wins.

Date-Accurate Layouts:

Automatically calculates correct days (including leap years/column adjustments) for every month in 2026.

Dynamic column sizing ensures perfect alignment for 28, 30, or 31-day months.

Integrated Sleep Tracker:

A dedicated 5-row sub-grid (5hrs–9hrs) positioned for easy correlation with daily habits.

🚀 How to Use (Code Version)
If you prefer to run the script from the source code:

Clone the repository.

Install dependencies:

Bash

pip install matplotlib numpy
Run the script:

Bash

python habit_tracker.py
Enter your handle when prompted in the terminal.

Find the generated PDFs in the newly created 2026_Trackers folder.

📝 Configuration details
Canvas: 14x10 inches (Landscape).

Output: Vector PDF (High quality for print).

📄 License
This project is open for personal use and modification.
