import matplotlib.pyplot as plt
import calendar
import numpy as np
import os
if not os.path.exists("trackers"):
    os.makedirs("trackers")

def create_habit_tracker(month, year):
    # Configuration
    days_in_month = calendar.monthrange(year, month)[1]
    month_name = calendar.month_name[month]
    day_labels = [calendar.day_name[calendar.weekday(year, month, day)][0] for day in range(1, days_in_month + 1)]
    
    # Figure setup (Landscape for better fit, or Portrait to match sample. Sample is Portrait)
    # A4 Portrait is roughly 8.27 x 11.69 inches. 
    fig, ax = plt.subplots(figsize=(11, 8.5)) # Landscape fits the wide columns better, but let's try to pack it like the sample
    # Actually the sample is landscape oriented (width > height) or just a very wide grid? 
    # Looking at the sample, it's likely a Landscape page because of 31 columns.
    fig.set_size_inches(14, 10) 
    
    ax.set_axis_off()
    
    # --- Headers ---
    # Top Left: Month Year
    ax.text(0.0, 0.98, f"{month_name} {year}", fontsize=16, weight='bold', transform=ax.transAxes)
    
    # Top Center: Quote
    ax.text(0.5, 0.98, "Getting 1% Better Each Day", fontsize=14, style='italic', weight='bold', ha='center', transform=ax.transAxes)
    
    # Top Right: Handle
    ax.text(1.0, 0.98, "@Nidhijain", fontsize=10, ha='right', transform=ax.transAxes)

    # --- Main Table (Habits) ---
    # Rows: 20 Habits + 1 Total Points
    # Cols: Habits label + 31 days
    n_habit_rows = 20
    n_days = days_in_month
    n_cols = n_days + 1 # +1 for Habit Labels column
    
    # Column headers
    # "Habit/Rules" is now the header for the first column
    col_labels = ["Habit/Rules"] + [str(i) for i in range(1, n_days + 1)]
    
    # Labels
    # We will build cell text where the first column is the label 
    
    cell_text = []
    for i in range(n_habit_rows):
        cell_text.append(['' for _ in range(n_cols)]) # First col empty for user to write
    
    # Total Points Row
    cell_text.append(['  Total Points'] + ['' for _ in range(n_days)])
    
    # Main Table
    the_table = plt.table(cellText=cell_text,
                          colLabels=col_labels,
                          loc='center',
                          bbox=[0.02, 0.20, 0.96, 0.72], 
                          cellLoc='center')
    
    # --- Styling & Column Widths ---
    the_table.auto_set_font_size(False)
    the_table.set_fontsize(10)
    
    cells = the_table.get_celld()
    
    # Define Widths
    # We want Col 0 to be wider.
    habit_col_width = 0.25
    day_col_width = (1.0 - habit_col_width) / n_days 
    
    # Iterate all cells to set geometry and style
    # Header is row 0 in cells dict (if we assume mpl logic, but header is usually (0, col))
    # Data rows start from 1? 
    # Let's inspect: header rows are usually (0, j). Data rows (1..N, j).
    
    total_rows = len(cell_text) + 1 # +1 for header
    
    for i in range(total_rows):
        for j in range(n_cols):
            if (i, j) not in cells: continue
            
            c = cells[(i, j)]
            
            # Widths
            if j == 0:
                c.set_width(habit_col_width)
                c.set_text_props(ha='left') 
                # if i > 0: c.set_text_props(padx=0.02) # padx not supported
            else:
                c.set_width(day_col_width)
            
            # Heights
            if i == 0: # Header
                c.set_height(0.05)
                c.set_text_props(weight='bold')     
            else:
                c.set_height(0.035)
                
    # Bold the Total Points Row (last row) - first column already bold?
    last_row_idx = total_rows - 1
    cells[(last_row_idx, 0)].set_text_props(weight='bold')
    
    # --- Dashboard Title ---
    # Moved up to create space
    ax.text(0.5, 0.94, "31 Day Dashboard" if days_in_month==31 else f"{days_in_month} Day Dashboard", 
            fontsize=12, weight='bold', ha='center', transform=ax.transAxes)

    # --- Sleep Table ---
    # Rows: 9hrs, 8hrs, ..., 5hrs
    # We use same column structure as Main Table for alignment
    sleep_labels = ["9hrs", "8hrs", "7hrs", "6hrs", "5hrs"]
    n_sleep_rows = len(sleep_labels)
    
    sleep_data = []
    for lbl in sleep_labels:
        # Col 0 is label, Col 1..31 are empty
        sleep_data.append([lbl] + ['' for _ in range(n_days)])
    
    # Sleep Table
    # Position: Below main table.
    sleep_table = plt.table(cellText=sleep_data,
                            colLabels=None, # No column header needed
                            loc='center',
                            bbox=[0.02, 0.04, 0.96, 0.10], # Match x, w of Main Table, Compact height
                            cellLoc='center')
    
    sleep_table.auto_set_font_size(False)
    sleep_table.set_fontsize(10)
    
    # Style Sleep Table Cells to match Main Table widths
    sleep_cells = sleep_table.get_celld()
    for i in range(n_sleep_rows):
        for j in range(n_cols):
             if (i, j) not in sleep_cells: continue
             c = sleep_cells[(i, j)]
             
             # Widths
             if j == 0:
                 c.set_width(habit_col_width)
                 c.set_text_props(ha='left', weight='bold') 
                 # c.set_text_props(padx=0.02) # Not supported
             else:
                 c.set_width(day_col_width)
                 
             c.set_height(0.2 / n_sleep_rows) 
    
    # Adding "Sleep" label closer to table
    ax.text(0.02, 0.15, "Sleep", fontsize=10, weight='bold', transform=ax.transAxes)

    # --- Note Section ---
    ax.text(0.01, 0.01, "Note:", fontsize=10, weight='bold', transform=ax.transAxes)
    # Draw a line or box for notes? Sample just has whitespace. 
    
    # Adjust layout
    plt.tight_layout()
    
    # Show
    plt.show()
    
    # Save the figure
    plt.savefig(f"trackers/Habit_Tracker_2026_{m}.pdf", format='pdf', bbox_inches='tight')
    plt.close()

# Generate January 2026
#create_habit_tracker(1, 2026)
for m in range(1, 13):
    create_habit_tracker(m, 2026)