2026 Monthly Habit Dashboard Generator 

A Python automation tool that generates 12 high-capacity, date-accurate habit tracker PDFs for 2026 with a 20-habit grid and integrated sleep tracking. It runs silently to produce a full year of printable dashboards in seconds.

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

20-Row Habit Grid: Expanded layout to track extensive daily routines.

Gamification: Includes a "Total Points" row to sum up daily wins.

Date-Accurate Layouts:

Automatically calculates correct days (including leap years/column adjustments) for every month in 2026.

Dynamic column sizing ensures perfect alignment for 28, 30, or 31-day months.

Integrated Sleep Tracker:

A dedicated 5-row sub-grid (5hrs–9hrs) positioned for easy correlation with daily habits.

🚀 How to Use
Run the Tool: Double-click habit_tracker_v3.exe. A terminal window will open.

Enter Your Handle: The program will ask:

Enter your handle (e.g. @YourName):

Option A: Type your desired name (e.g., @SuperCoder) and press Enter.

Option B: Press Enter without typing to use the default (@Nidhijain).

Wait for Generation: The script will process each month. You will see:

Plaintext

Generating tracker for month 1/12...
...
Success! All 12 trackers have been generated in the '2026_Trackers' folder.
Print: Open the newly created 2026_Trackers folder in the same directory and print your files.

📝 Configuration details
Canvas: 14x10 inches (Landscape).

Output: Vector PDF (High quality for print).
