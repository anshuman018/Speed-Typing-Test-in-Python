import random
import time
import tkinter as tk
from tkinter import messagebox

# List of sample sentences
sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "Programming is fun and challenging.",
    "Python is a versatile programming language.",
    "Practice makes perfect!",
    "Type as fast as you can!"
]

class SpeedTypingTestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Speed Typing Test")
        self.root.geometry("400x300")

        self.sentence_label = tk.Label(root, text="", font=("Helvetica", 14))
        self.sentence_label.pack(pady=20)

        self.entry = tk.Entry(root, font=("Helvetica", 12))
        self.entry.pack(pady=10)
        self.entry.bind("<Return>", self.check_typing_speed)

        self.start_button = tk.Button(root, text="Start", command=self.start_test, font=("Helvetica", 12))
        self.start_button.pack()

        self.elapsed_time = 0
        self.start_time = 0
        self.sentence = ""

    def get_random_sentence(self):
        return random.choice(sentences)

    def start_test(self):
        self.sentence = self.get_random_sentence()
        self.sentence_label.config(text=f"Type the following sentence:\n{self.sentence}")
        self.entry.delete(0, tk.END)
        self.start_time = time.time()
        self.elapsed_time = 0
        self.entry.config(state="normal")
        self.start_button.config(state="disabled")

    def check_typing_speed(self, event):
        typed_text = self.entry.get()
        end_time = time.time()
        self.elapsed_time = end_time - self.start_time
        correct_word_count, words_per_minute = self.calculate_typing_speed(self.sentence, typed_text, self.elapsed_time)

        if words_per_minute >= 10:
            message = f"Elapsed Time: {self.elapsed_time:.2f} seconds\nCorrect Words: {correct_word_count}/{len(self.sentence.split())}\nTyping Speed: {words_per_minute:.2f} words per minute"
            messagebox.showinfo("Results", message)
        else:
            messagebox.showinfo("Results", "Keep practicing to improve your typing speed.")

        self.entry.config(state="disabled")
        self.start_button.config(state="normal")

    def calculate_typing_speed(self, sentence, typed_text, elapsed_time):
        words = sentence.split()
        typed_words = typed_text.split()
        correct_words = [w1 == w2 for w1, w2 in zip(words, typed_words)]
        correct_word_count = sum(correct_words)

        words_per_minute = (correct_word_count / elapsed_time) * 60 if elapsed_time > 0 else 0
        return correct_word_count, words_per_minute

if __name__ == "__main__":
    root = tk.Tk()
    app = SpeedTypingTestApp(root)
    root.mainloop()
