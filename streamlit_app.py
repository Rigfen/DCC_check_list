import streamlit as st

st.set_page_config(page_title="Monthly Evaluation Checklist", layout="wide")

st.title("MONTHLY EVALUATION CHECKLIST")

score = 0

def checklist_section(title, items):
    global score
    st.subheader(title)

    for item in items:
        choice = st.radio(
            item,
            ["Unsat", "Sat", "Excl"],
            horizontal=True,
            index=None
        )

        if choice == "Sat":
            score += 1
        elif choice == "Excl":
            score += 2


# --- Sections ---

checklist_section("AIRCRAFT EXTERIOR", [
    "All Decal Condition",
    "Windshield / Fuselage screens Condition/Cleanliness",
    "Landing Gear Wheel Wells - FOD",
    'Strut "X" Dimensions',
    "Tire Serviceability",
    "Brake / Brake line Condition",
    "Chocks / Ground Wire Condition",
    "Quick Access PNLs Hinges / Bonding Wire Condition",
    "Plugs and Covers Condition"
])

checklist_section("AIRCRAFT INTERIOR - FLIGHT DECK", [
    "Seat Belt Serviceability / Condition",
    "Crew Seat Condition",
    "Galley Condition",
    "Floorboard Seam Strips / Armor Condition",
    "Flight Deck Lighting",
    "Emergency Equipment Serviceability",
    "Overhead Panel Missing Hardware / Condition",
    "Overall Flight Deck Cleanliness"
])

checklist_section("AIRCRAFT INTERIOR - CARGO COMPARTMENT", [
    "Hydraulic Panels Condition",
    "Loose Equipment Condition",
    "Emergency Equipment Condition",
    "Troop Seats / Loadmaster Seats Condition"
])

st.divider()
st.header(f"TOTAL SCORE: {score}")
