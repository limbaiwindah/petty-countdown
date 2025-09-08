# code to find days left to finishing internship
import random
import datetime
import tkinter as tk # For GUI creation
from tkinter import messagebox # For popup error messages (not actually used in this auto-countdown version)

# ------------------- SETTINGS -------------------

# Start and end date of my internship
START_DATE = datetime.date(2025, 7, 21)
END_DATE = datetime.date(2025, 10, 21)

# quotes to cycle through
QUOTES = [
    "I can do all things through him who strengthens me. - Philippians 4:13",
    "Fear not, for I am with you; be not dismayed, for I am your God; I will strengthen you, I will help you, I will uphold you with my righteous right hand. - Isaiah 41:10",
    "My flesh and my heart may fail, but God is the strength of my heart and my portion forever. - Psalm 73:26",
    "Be strong and courageous. Do not fear or be in dread of them, for it is the Lord your God who goes with you. He will not leave you or forsake you. - Deuteronomy 31:6",
    "The Lord is my strength and my song, and he has become my salvation; this is my God, and I will praise him, my father's God, and I will exalt him. - Exodus 15:2",
    "I have told you these things, so that in me you may have peace. In this world you will have trouble. But take heart! I have overcome the world. - John 16:33"
]

# ------------------- GUI SETUP -------------------

root = tk.Tk()  # Create main application window
root.title("Internship Finishline")  # Title bar text
root.geometry("550x300")  # Size of window in pixels (Width x Height)
root.configure(bg="#f9f9f9")  # Background color

# Fonts for labels
LABEL_FONT = ("Arial", 24)
QUOTE_FONT = ("Arial", 20)
RESULT_FONT = ("Arial", 24)

# Label to display countdown numbers
# wraplength = pixels before text wraps to next line
# justify = center-align the wrapped text
result_label = tk.Label(
    root,
    text="",
    font=RESULT_FONT,
    bg="#f9f9f9",
    wraplength=450,
    justify="center"
)
result_label.pack(pady=(30, 10))  # Add to window with vertical padding

# Label to display quotes
quote_label = tk.Label(
    root,
    text="",
    font=QUOTE_FONT,
    bg="#f9f9f9",
    wraplength=450,
    justify="center"
)
quote_label.pack(pady=(10, 0))

# ------------------- FUNCTIONS -------------------

def update_countdown():
    """Updates the countdown timer every 50 milliseconds."""
    now = datetime.datetime.now()  # Current date and time
    end_datetime = datetime.datetime.combine(END_DATE, datetime.time())  # End date at midnight
    time_left = end_datetime - now  # Time difference

    # If countdown has reached zero
    if time_left.total_seconds() <= 0:
        result_label.config(text="🎉 YOU ARE FREEEEEE 🕊️🎉", fg="green")
        return  # Stop updating

    # Break time_left into days, hours, minutes, seconds
    days = time_left.days
    hours, remainder = divmod(time_left.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    # Calculate weeks and leftover days
    weeksLeft = days // 7
    leftoverDays = days % 7

    # color changing label depending on weeks left
    if weeksLeft > 12:
        color = "#4B0000"   # almost black-red (absolute despair)
    elif 11 < weeksLeft <= 12:
        color = "#660000"   # very dark red
    elif 10 < weeksLeft <= 11:
        color = "#8B0000"   # dark red
    elif 9 < weeksLeft <= 10:
        color = "#A52A2A"   # brownish red
    elif 8 < weeksLeft <= 9:
        color = "#B22222"   # firebrick
    elif 7 < weeksLeft <= 8:
        color = "#DC143C"   # crimson
    elif 6 < weeksLeft <= 7:
        color = "#FF4500"   # reddish orange
    elif 5 < weeksLeft <= 6:
        color = "#FF6347"   # tomato
    elif 4 < weeksLeft <= 5:
        color = "#FF8C00"   # dark orange
    elif 3 < weeksLeft <= 4:
        color = "#FFA500"   # orange
    elif 2 < weeksLeft <= 3:
        color = "#FFD700"   # gold
    elif 1 < weeksLeft <= 2:
        color = "#FFFF00"   # bright yellow
    elif 0.5 < weeksLeft <= 1:
        color = "#ADFF2F"   # yellow-green
    elif 0 < weeksLeft <= 0.5:
        color = "#7CFC00"   # lawn green
    else:
        color = "#32CD32"   # lime green (victory!)

    # Build the display message
    message = (
        f"🎯 {weeksLeft} weeks and {leftoverDays} days left!\n\n"
        f" 🌻 {days} days {hours:02d} hours {minutes:02d} minutes and {seconds:02d} seconds to freedom 🌻"
    )

    # Update the countdown label with new text and color
    result_label.config(text=message, fg=color)

    # Schedule this function to run again after 50 milliseconds
    root.after(50, update_countdown)


def update_quote():
    """Changes the displayed quote every 7 seconds."""
    quote_label.config(text=f"📢 {random.choice(QUOTES)}")  # Pick a random quote
    root.after(7000, update_quote)  # Call this function again in 3 seconds

# ------------------- START UPDATES -------------------

update_countdown()  # Start the countdown loop
update_quote()      # Start the quote slideshow

# Keep the window running
root.mainloop()
