2026 Monthly Habit Dashboard Generator
📖 Project Overview
This project is a Python-based automation tool designed to generate high-resolution, print-ready habit trackers for the entire year of 2026. Inspired by the philosophy of "Getting 1% Better Each Day," the script dynamically creates 12 individual monthly dashboards. Each dashboard is formatted for A4/Letter printing and serves as an analog tool for tracking daily habits, sleep patterns, and monthly goals.

🎯 Objective
To eliminate the need for manually drawing or purchasing generic habit trackers by programmatically generating custom, date-accurate layouts for any specific year.

🛠 Tech Stack
Language: Python 3.x

Libraries:

matplotlib: Used as the primary plotting engine to draw the grids, tables, and text elements with precision.

calendar: Utilized to calculate the accurate number of days per month and determine the correct day-of-the-week initials (M, T, W, etc.) for specific dates in 2026.

numpy: Used for array handling within the plotting logic.

✨ Key Features
Dynamic Date Calculation:

The script automatically adjusts the number of columns (28, 29, 30, or 31) based on the month.

It correctly aligns day initials (Mon, Tue, Wed) for every specific date in 2026.

Structured Layout:

Main Dashboard: Space for 12 distinct habits/rules.

Sleep Tracker: A dedicated sub-grid to plot sleep duration (5hrs to 9hrs).

Total Points Row: A gamification element to sum up daily wins.

Notes Section: Free space for monthly reflections.

High-Resolution Output:

Generates crisp vector-based PDFs or high-DPI PNGs suitable for physical printing without pixelation.

Customizable Elements:

Users can easily modify the code to change the "Quote of the Month," the social media handle, or the specific habits pre-filled in the rows.

🚀 How It Works
The script iterates through a loop of integers (1–12), representing the months. For each iteration:

It queries the calendar module to get the range of days for that month/year.

It initializes a matplotlib figure without axes.

It constructs two table objects: one for habits and one for sleep.

It populates the headers with the correct day initials.

you can save the final visual as a file (e.g., January_2026.png) in the local directory.
