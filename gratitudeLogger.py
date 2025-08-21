from datetime import datetime
import tkinter as tk

# function to save gratitude
def save_gratitude():
    gratitude = entry.get() #get text from entry box
    if gratitude.strip(): #only save if not empty
        with open("gratitude_logger.txt", "a") as file:
            file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {gratitude}\n")
        status_label.config(text="Log saved 💙") #feedback in GUI
        entry.delete(0, tk.END) #clear input box
    else:
        status_label.config(text="Please enter something first.")

# GUI setup
root = tk.Tk()  # Create main application window
root.title("Petty Freedom Tracker")  # Title bar text
root.geometry("550x300")  # Size of window in pixels (Width x Height)
root.configure(bg="#f9f9f9")  # Background color

# Fonts
TITLE_FONT = ("Arial", 18, "bold")
ENTRY_FONT = ("Arial", 14)

#title label
title_label = tk.Label(root, text="What are you grateful for today?", font=TITLE_FONT, bg="#f9f9f9", fg="#333" )
title_label.pack(pady=20)

#entry box
entry = tk.Entry(root, font=ENTRY_FONT, width=40)
entry.pack(pady=10, ipadx=50, ipady=20)

#save button
save_button = tk.Button(root, text="Save Entry", font=("Arial", 14), command=save_gratitude)
save_button.pack(pady=10)

#status label
status_label = tk.Label(root, text="", font=("Arial", 12), bg="#f9f9f9", fg="#555")
status_label.pack(pady=10)

# run GUI loop
root.mainloop()