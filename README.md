# 📰 Fake Newspaper Generator

## 📄 Project Description
A fun Python Tkinter-based app that generates fictional newspaper front pages with random headlines, images, and filler articles in a vintage style. Includes multi-column layout, date display, and image fetching.

**Short Description (30 words):**  
A Python Tkinter GUI app that creates a realistic fake newspaper front page with random headlines, filler articles, and images, styled like a vintage paper, complete with masthead and footer.

---

## 🎯 Features
- **Tkinter GUI** – User-friendly, interactive front-end.
- **Dynamic Headlines** – Randomly generated using predefined words and templates.
- **Random Images** – Pulled from `picsum.photos` to simulate real newspaper photos.
- **Multi-column Layout** – 3 neat columns for a realistic newspaper feel.
- **Date & Masthead** – Styled title and current date display.
- **Filler Articles** – Funny, pre-written short news snippets.
- **Footer Disclaimer** – Marks all stories as fictional.

---

## 📦 Requirements
Make sure you have these installed before running:
```bash
pip install pillow requests
🛠 How to Run
Save the script as fake_newspaper.py.

Install dependencies using pip.

Run the script:
python fake_newspaper.py

Click "Generate News" to create a new random newspaper layout.


🧠 Pseudocode

BEGIN
    DEFINE list of subjects, verbs, objects, adjectives, locations
    DEFINE templates for headline structure
    DEFINE list of filler articles

    FUNCTION generate_fake_news_headline:
        SELECT random template
        SELECT random subject, verb, adjective, object, location
        FORMAT template with selected words
        RETURN headline

    FUNCTION get_random_image(width, height):
        TRY
            FETCH image from picsum.photos
            CONVERT to Tkinter-compatible image
            RETURN image
        CATCH error
            RETURN None

    FUNCTION show_newspaper:
        CLEAR previous widgets
        DISPLAY masthead and date
        CALL generate_fake_news_headline
        DISPLAY headline in large font
        CALL get_random_image
        DISPLAY image if available
        ARRANGE filler articles in 3 columns
        DISPLAY footer

    CREATE Tkinter window
    CREATE "Generate News" button to call show_newspaper
    CALL show_newspaper once to load first layout
    RUN Tkinter main loop
END


📊 Flowchart

 ┌──────────────────────────┐
 │ Start Program            │
 └────────────┬─────────────┘
              ↓
 ┌──────────────────────────┐
 │ Initialize word lists     │
 └────────────┬─────────────┘
              ↓
 ┌──────────────────────────┐
 │ User clicks "Generate"    │
 └────────────┬─────────────┘
              ↓
 ┌──────────────────────────┐
 │ Generate random headline  │
 └────────────┬─────────────┘
              ↓
 ┌──────────────────────────┐
 │ Fetch random image        │
 └────────────┬─────────────┘
              ↓
 ┌──────────────────────────┐
 │ Arrange layout in GUI     │
 └────────────┬─────────────┘
              ↓
 ┌──────────────────────────┐
 │ Display in newspaper style│
 └────────────┬─────────────┘
              ↓
 ┌──────────────────────────┐
 │ Wait for next action      │
 └──────────────────────────┘
Mermaid Diagram (renders on GitHub)

flowchart TD
    A[Start Program] --> B[Initialize Word Lists]
    B --> C[User Clicks "Generate"]
    C --> D[Generate Random Headline]
    D --> E[Fetch Random Image]
    E --> F[Arrange Layout in GUI]
    F --> G[Display in Newspaper Style]
    G --> H[Wait for Next Action]
📚 Functionalities Used
Random Headline Generation – Uses random.choice() to pick elements from multiple word lists and templates.

Dynamic Image Fetching – Uses requests to get a random image from picsum.photos and PIL.ImageTk for Tkinter display.

GUI Layout – Tkinter Frame, Label, and Button widgets arranged for realistic newspaper appearance.

Text Wrapping & Styling – wraplength and justify for multi-column readability.

Multi-column Article Arrangement – Grid layout to create 3-column article structure.

Date Display – Uses datetime.now() for current date formatting.

Error Handling – Image fetching wrapped in try-except to prevent crashes.

Reusable Functions – Separated functionality into modular functions (generate_fake_news_headline, get_random_image, show_newspaper) for clarity.

📷 Example Output
(Random example layout)

⚠ Disclaimer
All headlines, articles, and stories generated by this application are purely fictional and created for entertainment purposes only.
