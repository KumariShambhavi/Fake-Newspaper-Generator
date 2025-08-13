import random
import tkinter as tk
from datetime import datetime
from PIL import Image, ImageTk
import requests
from io import BytesIO

# --- Fake news generator ---
def generate_fake_news_headline():
    subjects = [
        "Scientists", "Experts", "A new study", "Researchers", "Historians",
        "Government officials", "Space agencies", "Time travelers", "AI robots", "Secret societies"
    ]
    verbs = [
        "discover", "reveal", "uncover", "announce", "warn about",
        "confirm", "accidentally invent", "deny", "celebrate", "predict"
    ]
    objects = [
        "the truth about cats", "a new species of dinosaur", "the benefits of chocolate",
        "the dangers of social media", "how pizza can save the planet",
        "aliens living among us", "a portal to another dimension",
        "the world's smallest laptop", "how carrots improve night vision",
        "why Mondays should be illegal"
    ]
    adjectives = [
        "shocking", "groundbreaking", "mysterious", "unbelievable", "controversial",
        "mind-blowing", "unexpected", "bizarre", "historic", "record-breaking"
    ]
    locations = [
        "in New York", "on Mars", "in Antarctica", "under the Pacific Ocean",
        "inside a volcano", "in the White House", "at the North Pole", "in a secret lab"
    ]
    templates = [
        "{subject} {verb} {adjective} {object} {location}",
        "Breaking: {subject} {verb} {object} {location}",
        "Exclusive: {adjective} discovery as {subject} {verb} {object}",
        "{subject} {verb} {object} after {adjective} event {location}"
    ]
    template = random.choice(templates)
    headline = template.format(
        subject=random.choice(subjects),
        verb=random.choice(verbs),
        adjective=random.choice(adjectives),
        object=random.choice(objects),
        location=random.choice(locations)
    )
    return headline.title()

# --- Dummy filler news ---
filler_articles = [
    "Local cat becomes mayor of small town.",
    "Man claims to have invented a square wheel.",
    "Government considers replacing traffic lights with AI robots.",
    "Scientists debate if pineapple belongs on pizza.",
    "New law proposed to make Mondays optional.",
    "Farmer discovers 3-ton carrot in backyard.",
    "School bans homework, grades happiness instead.",
    "Archaeologists find USB drive in ancient pyramid."
]

# --- Fetch random image ---
def get_random_image(width=500, height=250):
    try:
        url = f"https://picsum.photos/{width}/{height}"
        response = requests.get(url)
        img = Image.open(BytesIO(response.content))
        return ImageTk.PhotoImage(img)
    except Exception as e:
        print("Error fetching image:", e)
        return None

# --- Main newspaper display ---
def show_newspaper():
    for widget in frame.winfo_children():
        widget.destroy()

    # Masthead with separators
    tk.Frame(frame, height=2, bg="black").pack(fill="x", pady=(0, 5))
    tk.Label(frame, text="📰 THE JUNO TIMES 📰", font=("Times New Roman", 28, "bold"), bg="#f4f4f4").pack()
    tk.Frame(frame, height=2, bg="black").pack(fill="x", pady=(5, 5))

    # Date
    tk.Label(frame, text=datetime.now().strftime("%A, %B %d, %Y"), font=("Arial", 12, "italic"), bg="#f4f4f4").pack()

    # Headline
    headline = generate_fake_news_headline()
    tk.Label(frame, text=headline, font=("Times New Roman", 22, "bold"), fg="black", wraplength=700, justify="center", bg="#f4f4f4").pack(pady=10)
    tk.Frame(frame, height=1, bg="black").pack(fill="x", pady=(0, 10))

    # Featured image
    img_tk = get_random_image()
    if img_tk:
        img_label = tk.Label(frame, image=img_tk, bg="#f4f4f4")
        img_label.image = img_tk
        img_label.pack(pady=5)
    else:
        tk.Label(frame, text="(Image not available)", font=("Arial", 12, "italic"), fg="red", bg="#f4f4f4").pack()

    tk.Frame(frame, height=1, bg="black").pack(fill="x", pady=(10, 10))

    # Articles in 3-column layout
    articles_frame = tk.Frame(frame, bg="#f4f4f4")
    articles_frame.pack()

    col_count = 3
    for i, article in enumerate([headline] + random.sample(filler_articles, 6)):
        lbl = tk.Label(articles_frame, text=article, font=("Arial", 11), wraplength=220, justify="left", anchor="nw", bg="#f4f4f4")
        lbl.grid(row=i // col_count, column=i % col_count, padx=10, pady=5, sticky="nw")

    tk.Frame(frame, height=2, bg="black").pack(fill="x", pady=10)

    # Footer
    tk.Label(frame, text="© 2025 The Python Times – All headlines are purely fictional", font=("Arial", 9, "italic"), fg="gray", bg="#f4f4f4").pack(pady=(0, 5))

# --- Tkinter setup ---
root = tk.Tk()
root.title("Fake Newspaper Generator")
root.configure(bg="#f4f4f4")

frame = tk.Frame(root, padx=20, pady=20, bg="#f4f4f4")
frame.pack()

tk.Button(root, text="📰 Generate News 📰", font=("Arial", 14, "bold"), command=show_newspaper, bg="black", fg="white").pack(pady=10)

# Show first newspaper
show_newspaper()

root.mainloop()
