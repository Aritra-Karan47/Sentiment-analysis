import tkinter as tk
from tkinter import messagebox
from textblob import TextBlob

# Sentiment analysis function
def analyze_sentiment():
    text = text_input.get("1.0", tk.END).strip()
    if not text:
        messagebox.showwarning("Input Error", "Please enter some text to analyze.")
        return

    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0:
        sentiment = "Positive 😊"
    elif polarity < 0:
        sentiment = "Negative 😞"
    else:
        sentiment = "Neutral 😐"

    result_label.config(
        text=f"Sentiment: {sentiment}\nPolarity Score: {polarity:.2f}"
    )

# Create main window
root = tk.Tk()
root.title("Sentiment Analyzer")
root.geometry("400x300")
root.resizable(False, False)

# Text input area
tk.Label(root, text="Enter text to analyze:", font=("Arial", 12)).pack(pady=5)
text_input = tk.Text(root, height=5, width=40, font=("Arial", 10))
text_input.pack(pady=5)

# Analyze button
analyze_button = tk.Button(
    root,
    text="Analyze Sentiment",
    command=analyze_sentiment,
    bg="#4CAF50",
    fg="white",
    font=("Arial", 12, "bold"),
)
analyze_button.pack(pady=10)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 12), wraplength=350)
result_label.pack(pady=10)

# Run the app
root.mainloop()

