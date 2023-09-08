import random
import time

# List of sample sentences
sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "Programming is fun and challenging.",
    "Python is a versatile programming language.",
    "Practice makes perfect!",
    "Type as fast as you can!"
]

def get_random_sentence():
    return random.choice(sentences)

def calculate_typing_speed(sentence, typed_text, elapsed_time):
    words = sentence.split()
    typed_words = typed_text.split()
    correct_words = [w1 == w2 for w1, w2 in zip(words, typed_words)]
    correct_word_count = sum(correct_words)
    
    words_per_minute = (correct_word_count / elapsed_time) * 60 if elapsed_time > 0 else 0
    return correct_word_count, words_per_minute

def main():
    print("Welcome to the Speed Typing Test!")

    input("Press Enter to start...")
    
    sentence = get_random_sentence()
    print(f"Type the following sentence as quickly as possible:\n{sentence}\n")

    start_time = time.time()
    typed_text = input("Start typing: ")
    end_time = time.time()

    elapsed_time = end_time - start_time

    correct_word_count, words_per_minute = calculate_typing_speed(sentence, typed_text, elapsed_time)

    print("\nResults:")
    print(f"Elapsed Time: {elapsed_time:.2f} seconds")
    print(f"Correct Words: {correct_word_count}/{len(sentence.split())}")
    print(f"Typing Speed: {words_per_minute:.2f} words per minute")

if __name__ == "__main__":
    main()
