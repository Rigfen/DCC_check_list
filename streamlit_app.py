import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Monthly Evaluation Checklist")
root.geometry("850x700")

# --- Scrollable Frame ---
container = ttk.Frame(root)
canvas = tk.Canvas(container)
scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
scroll_frame = ttk.Frame(canvas)

scroll_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

container.pack(fill="both", expand=True)
canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# --- Header ---
tk.Label(scroll_frame, text="MONTHLY EVALUATION CHECKLIST",
         font=("Arial", 14, "bold")).grid(row=0, column=0, columnspan=4, pady=10)

# Column Titles
headers = ["ITEM", "Unsat", "Sat", "Excl"]
for col, text in enumerate(headers):
    tk.Label(scroll_frame, text=text, font=("Arial", 10, "bold"))\
        .grid(row=1, column=col, padx=5)

row_num = 2
total_score = tk.IntVar(value=0)

# --- Score Update Function ---
def update_score(*args):
    score = 0
    for var in all_vars:
        value = var.get()
        if value == 2:  # Sat
            score += 1
        elif value == 3:  # Excl
            score += 2
    total_score.set(score)

all_vars = []

# --- Function to Add Section ---
def add_section(title):
    global row_num
    tk.Label(scroll_frame, text=title,
             font=("Arial", 10, "bold"), anchor="w")\
        .grid(row=row_num, column=0, sticky="w", pady=(12, 2))
    row_num += 1

# --- Function to Add Checklist Row ---
def add_item(text):
    global row_num

    tk.Label(scroll_frame, text=text, anchor="w",
             justify="left", wraplength=500)\
        .grid(row=row_num, column=0, sticky="w", padx=5)

    # Use ONE IntVar per row (ensures only one choice)
    var = tk.IntVar(value=0)

    unsat = ttk.Radiobutton(scroll_frame, variable=var, value=1, command=update_score)
    sat   = ttk.Radiobutton(scroll_frame, variable=var, value=2, command=update_score)
    excl  = ttk.Radiobutton(scroll_frame, variable=var, value=3, command=update_score)

    unsat.grid(row=row_num, column=1)
    sat.grid(row=row_num, column=2)
    excl.grid(row=row_num, column=3)

    all_vars.append(var)
    row_num += 1

# --- Sections & Items ---
add_section("DEDICATED CREW CHIEF / AIRCRAFT TAIL NUMBER")

add_section("AIRCRAFT EXTERIOR")
add_item("All Decal Condition")
add_item("Windshield / Fuselage screens Condition/Cleanliness")
add_item("Landing Gear Wheel Wells - FOD")
add_item('Strut "X" Dimensions')
add_item("Tire Serviceability")
add_item("Brake / Brake line Condition")
add_item("Chocks / Ground Wire Condition")
add_item("Quick Access PNLs Hinges / Bonding Wire Condition")
add_item("Plugs and Covers Condition")

add_section("AIRCRAFT INTERIOR - FLIGHT DECK")
add_item("Seat Belt Serviceability / Condition")
add_item("Crew Seat Condition")
add_item("Galley Condition")
add_item("Floorboard Seam Strips / Armor Condition")
add_item("Flight Deck Lighting")
add_item("Emergency Equipment Serviceability")
add_item("Overhead Panel Missing Hardware / Condition")
add_item("Overall Flight Deck Cleanliness")

add_section("AIRCRAFT INTERIOR - CARGO COMPARTMENT")
add_item("Hydraulic Panels Condition")
add_item("Loose Equipment Condition")
add_item("Emergency Equipment Condition")
add_item("Troop Seats / Loadmaster Seats Condition")

# --- Total Score Display ---
ttk.Separator(scroll_frame, orient="horizontal").grid(
    row=row_num, columnspan=4, sticky="ew", pady=15)
row_num += 1

tk.Label(scroll_frame, text="TOTAL SCORE:",
         font=("Arial", 12, "bold")).grid(row=row_num, column=0, sticky="e")

tk.Label(scroll_frame, textvariable=total_score,
         font=("Arial", 12, "bold")).grid(row=row_num, column=1, sticky="w")

root.mainloop()
