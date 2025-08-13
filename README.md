# Petty Countdown 
I built this on my freetime during internshp at my University. Yes, it was that boring lol.

## 📖 Features
- **Live countdown** with millisecond precision (you can add it if you want).
- **Automatic quote slideshow** — quotes change every few seconds.
- **Customizable target date** for any event, not just internships.
- Clean and simple **Tkinter GUI**.
- Fully **offline** — no internet required.

## How to run
1. clone this repo
```
git clone https://github.com/limbaiwindah/petty-countdown.git
cd petty-countdown
```
2. run it (the triangle shape if you use vsc or `python internDayCountdown.py`

## Configuration
you can customize your start and end date here:
```
START_DATE = datetime.date(2025, 7, 21)
END_DATE = datetime.date(2025, 10, 19)
```

to change the quotes, you can go to:
```
QUOTES = [
    "Remember: They can extend your days, but not your soul.",
    "Every tick of the clock is one less meeting with them (lol)",
    "Internship: because free labor sounds better than slavery (lmao)",
    "Soon you'll be telling this story like a war veteran 😂"
]
```

to change window size:
```
root.geometry("500x300")  # width x height
```

## 🛠️ Technologies Used
- Python 3
- Tkinter (GUI framework)

## 🎀 Acknowledgements
Motivational quotes sourced from various authors.
Created with 😭, ⏳, and a lot of excitement for the internship to end BAHAHAHA
