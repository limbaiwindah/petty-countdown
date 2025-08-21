# code to find days left to finishing internship
import random
import datetime
import tkinter as tk # For GUI creation
from tkinter import messagebox # For popup error messages (not actually used in this auto-countdown version)

# ------------------- SETTINGS -------------------

# Start and end date of my internship
START_DATE = datetime.date(2025, 7, 21)
END_DATE = datetime.date(2025, 10, 21)

# Passive-aggressive quotes to cycle through
QUOTES = [
    "Remember: They can extend your days, but not your soul.",
    "Every tick of the clock is one less meeting with them (lol)",
    "Internship: because free labor sounds better than slavery (lmao)",
    "Soon you'll be telling this story like a war veteran 😂"
]

# ------------------- GUI SETUP -------------------

root = tk.Tk()  # Create main application window
root.title("Petty Freedom Tracker")  # Title bar text
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

    # Change text color depending on how close you are to freedom
    if weeksLeft > 6:
        color = "red"  # suffering stage lol
    elif 3 < weeksLeft <= 6:
        color = "orange"  # almost stage
    else:
        color = "green"  # final sprint

    # Build the display message
    message = (
        f"🎯 {weeksLeft} weeks and {leftoverDays} days left!\n\n"
        f" 🌝 {days} days {hours:02d} hours {minutes:02d} minutes and {seconds:02d} seconds to freedom 🌝"
    )

    # Update the countdown label with new text and color
    result_label.config(text=message, fg=color)

    # Schedule this function to run again after 50 milliseconds
    root.after(50, update_countdown)


def update_quote():
    """Changes the displayed quote every 3 seconds."""
    quote_label.config(text=f"📢 {random.choice(QUOTES)}")  # Pick a random quote
    root.after(3000, update_quote)  # Call this function again in 3 seconds

# ------------------- START UPDATES -------------------

update_countdown()  # Start the countdown loop
update_quote()      # Start the quote slideshow

# Keep the window running
root.mainloop()
